import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from numpy.linalg import LinAlgError

from gui import Ui_mainWindow
import src.code.pendulum_calculate as pecal
import src.code.draw as draw


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_simulation)
        self.ani = None

    def start_simulation(self):
        data = {
            "system_data": {"g": 9.80665, "dt": 0.0001},
            "pendulum_data": {
                "p1": {
                    "mass": self.ui.p1_mass.value(),
                    "length": self.ui.p1_length.value(),
                    "theta0": self.ui.p1_theta0.value(),
                    "omega0": self.ui.p1_omega0.value(),
                },
                "p2": {
                    "mass": self.ui.p2_mass.value(),
                    "length": self.ui.p2_length.value(),
                    "theta0": self.ui.p2_theta0.value(),
                    "omega0": self.ui.p2_omega0.value(),
                }
            }
        }

        # 시작 전 입력값 자체를 미리 검증 (0이면 특이행렬 원인이 되니 여기서 먼저 차단)
        for key in ["p1", "p2"]:
            if data["pendulum_data"][key]["mass"] <= 0 or data["pendulum_data"][key]["length"] <= 0:
                QMessageBox.warning(
                    self, "입력값 오류",
                    f"{key}의 질량과 길이는 0보다 커야 합니다."
                )
                return

        self.Pc = pecal.Pendulum(data)
        self.Dr = draw.PendulumDrawer()

        self.ani = animation.FuncAnimation(
            self.Dr.fig, self.animate, interval=20, blit=True,
            cache_frame_data=False  # 아까 뜬 경고도 같이 해결
        )
        plt.show(block=False)

    def animate(self, frame):
        try:
            for _ in range(50):
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
            self.ani.event_source.stop()  # 애니메이션 멈추기
        QMessageBox.critical(self, "시뮬레이션 오류", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())