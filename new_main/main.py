import sys
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QProgressDialog
from PySide6.QtCore import QTimer, QThread, Signal
from numpy.linalg import LinAlgError

from gui import Ui_mainWindow
import src.code.pendulum_calculate as pecal
import src.code.draw as draw
import src.code.export as export
import src.code.analysis as analysis


class ExportWorker(QThread):
    progress = Signal(int)
    finished_ok = Signal(str)
    failed = Signal(str)

    def __init__(self, pendulum, filepath, file_format):
        super().__init__()
        self.pendulum = pendulum
        self.filepath = filepath
        self.file_format = file_format

    def run(self):
        try:
            def report(pct):
                self.progress.emit(pct)

            if self.file_format == "csv":
                export.export_to_csv(self.pendulum, self.filepath, progress_callback=report)
            else:
                export.export_to_excel(self.pendulum, self.filepath, progress_callback=report)

            self.finished_ok.emit(self.filepath)
        except Exception as e:
            self.failed.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_simulation)
        self.ani = None
        self.Pc = None
        self.Dr = None
        self.export_worker = None
        self.progress_dialog = None
        self.reference_filepath = None

        self.ui.selectRefButton.clicked.connect(self.select_reference_file)
        self.ui.lyapunovButton.clicked.connect(self.compute_and_show_lyapunov)

    def select_reference_file(self):
        print("버튼 눌림!")  # 디버깅용
        filepath, _ = QFileDialog.getOpenFileName(
            self, "기준 파일 선택", "", "CSV Files (*.csv)"
        )
        print(f"선택된 파일: {filepath}")  # 디버깅용
        if filepath:
            self.reference_filepath = filepath
            self.ui.referenceLabel.setText(f"기준: {filepath.split('/')[-1]}")

    def get_float(self, line_edit, field_name):
        text = line_edit.text().strip()
        if text == "":
            QMessageBox.warning(self, "입력값 오류", f"'{field_name}' 값이 비어 있습니다.\n값을 입력해주세요.")
            return None
        try:
            return float(text)
        except ValueError:
            QMessageBox.warning(self, "입력값 오류", f"'{field_name}' 값이 숫자가 아닙니다: '{text}'")
            return None

    @staticmethod
    def make_default_filename(extension):
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        return f"PendullemaData_{timestamp}.{extension}"

    def start_simulation(self):
        fields = [
            (self.ui.p1_mass, "진자1 질량"),
            (self.ui.p1_line, "진자1 줄 길이"),
            (self.ui.p1_theta0, "진자1 초기각"),
            (self.ui.p1_omega0, "진자1 각속도"),
            (self.ui.p2_mass, "진자2 질량"),
            (self.ui.p2_line, "진자2 줄 길이"),
            (self.ui.p2_theta0, "진자2 초기각"),
            (self.ui.p2_omega0, "진자2 각속도"),
        ]

        values = []
        for widget, name in fields:
            v = self.get_float(widget, name)
            if v is None:
                return
            values.append(v)

        p1_mass, p1_length, p1_theta0, p1_omega0, p2_mass, p2_length, p2_theta0, p2_omega0 = values

        data = {
            "system_data": {"g": 9.80665, "dt": 0.0001},
            "pendulum_data": {
                "p1": {"mass": p1_mass, "length": p1_length, "theta0": p1_theta0, "omega0": p1_omega0},
                "p2": {"mass": p2_mass, "length": p2_length, "theta0": p2_theta0, "omega0": p2_omega0},
            }
        }

        for key in ["p1", "p2"]:
            if data["pendulum_data"][key]["mass"] <= 0 or data["pendulum_data"][key]["length"] <= 0:
                QMessageBox.warning(
                    self, "입력값 오류",
                    f"{key}의 질량과 길이는 0보다 커야 합니다."
                )
                return

        self.Pc = pecal.Pendulum(data)
        self.Dr = draw.PendulumDrawer()

        self.Dr.fig.canvas.mpl_connect('close_event', self.on_simulation_closed)

        self.ani = animation.FuncAnimation(
            self.Dr.fig, self.animate, interval=20, blit=True,
            cache_frame_data=False
        )
        plt.show(block=False)

    def animate(self, _frame):
        steps_per_frame = self.ui.Public_FrameAmount.value()

        try:
            for _ in range(steps_per_frame):
                self.Pc.update()
        except LinAlgError:
            self.show_error("계산 중 특이행렬(Singular matrix) 오류가 발생했습니다.\n입력값을 확인해주세요.")
            return self.Dr.line, self.Dr.trail_line
        except Exception as e:
            self.show_error(f"예상치 못한 오류가 발생했습니다:\n{e}")
            return self.Dr.line, self.Dr.trail_line

        return self.Dr.update_positions(self.Pc.p1_pos, self.Pc.p2_pos)

    def show_error(self, message):
        if self.ani is not None:
            self.ani.event_source.stop()
        QMessageBox.critical(self, "시뮬레이션 오류", message)

    def on_simulation_closed(self, _event):
        """matplotlib 창이 닫힐 때 호출됨. 창 정리가 끝난 뒤 저장창을 띄우려고 한 박자 늦춤."""
        if self.Pc is None or len(self.Pc.history) == 0:
            return
        QTimer.singleShot(150, self.ask_export)

    def compute_and_show_lyapunov(self):
        if self.reference_filepath is None:
            QMessageBox.warning(self, "기준 파일 없음", "먼저 비교할 기준 파일을 선택해주세요.")
            return
        if self.Pc is None or len(self.Pc.history) == 0:
            QMessageBox.warning(self, "데이터 없음", "먼저 시뮬레이션을 실행해주세요.")
            return

        try:
            ref_df = analysis.load_reference(self.reference_filepath)
            slope, t, log_diff = analysis.compute_lyapunov(self.Pc.history, ref_df)
            QMessageBox.information(
                self, "리아푸노프 지수",
                f"계산된 리아푸노프 지수 λ ≈ {slope:.4f}\n\n"
                f"(양수: 카오스/발산, 음수 또는 0에 가까움: 수렴/유사한 궤적)"
            )
        except Exception as e:
            QMessageBox.critical(self, "계산 오류", f"리아푸노프 지수 계산 중 오류:\n{e}")

    def ask_export(self):
        if self.ui.radioButton.isChecked():
            file_format = "csv"
            default_name = self.make_default_filename("csv")
            filepath, _ = QFileDialog.getSaveFileName(self, "CSV로 저장", default_name, "CSV Files (*.csv)")
        elif self.ui.radioButton_2.isChecked():
            file_format = "excel"
            default_name = self.make_default_filename("xlsx")
            filepath, _ = QFileDialog.getSaveFileName(self, "Excel로 저장", default_name, "Excel Files (*.xlsx)")
        else:
            return  # 내보내지 않음

        if not filepath:
            return  # 사용자가 취소

        self.progress_dialog = QProgressDialog("파일 저장 중...", None, 0, 100, self)
        self.progress_dialog.setWindowTitle("내보내기")
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setValue(0)
        self.progress_dialog.show()

        self.export_worker = ExportWorker(self.Pc, filepath, file_format)
        self.export_worker.progress.connect(self.progress_dialog.setValue)
        self.export_worker.finished_ok.connect(self.on_export_finished)
        self.export_worker.failed.connect(self.on_export_failed)
        self.export_worker.start()

    def on_export_finished(self, filepath):
        self.progress_dialog.close()
        QMessageBox.information(self, "내보내기 완료", f"{filepath}로 저장되었습니다.")

    def on_export_failed(self, error_message):
        self.progress_dialog.close()
        QMessageBox.critical(self, "내보내기 실패", f"저장 중 오류가 발생했습니다:\n{error_message}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())