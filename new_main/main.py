import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from numpy.linalg import LinAlgError

from gui import Ui_mainWindow
import src.code.pendulum_calculate as pecal
import src.code.draw as draw
import src.code.export as export


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_simulation)
        self.ani = None
        self.Pc = None

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

    def animate(self, frame):
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

    def on_simulation_closed(self, event):
        """시뮬레이션 창을 닫으면, 선택된 라디오버튼에 따라 자동으로 데이터를 내보냄"""
        if self.Pc is None or len(self.Pc.history) == 0:
            return

        if self.ui.radioButton.isChecked():          # CSV로 내보내기
            filepath = "output.csv"
            export.export_to_csv(self.Pc, filepath)
            QMessageBox.information(self, "내보내기 완료", f"{filepath}로 저장되었습니다.")
        elif self.ui.radioButton_2.isChecked():       # Excel로 내보내기
            filepath = "output.xlsx"
            export.export_to_excel(self.Pc, filepath)
            QMessageBox.information(self, "내보내기 완료", f"{filepath}로 저장되었습니다.")
        # radioButton_3("내보내지 않음")이 선택된 경우 아무 것도 안 함


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())