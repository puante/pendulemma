import matplotlib.pyplot as plt
import matplotlib.animation as animation


class PendulumDrawer:
    def __init__(self, xlim=(-7, 7), ylim=(-7, 7), trail_length=200, trail_draw=1):
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.ax.set_xlim(*xlim)
        self.ax.set_ylim(*ylim)
        self.ax.set_aspect('equal')
        self.ax.grid(True)

        self.line, = self.ax.plot([], [], 'o-', linewidth=2, markersize=8)
        self.trail_line, = self.ax.plot([], [], '-', linewidth=1, alpha=0.5, color='orange')

        # 자취를 그릴 것인지 안 그릴것인지에 대한 내용.
        # 0번은 아예 안 그리고, 1번은 2번 진자만, ~~(2번은 1,2번 둘 다.)~~
        self.trail_draw = trail_draw

        self.trail_length = trail_length  # 궤적 최대 길이 (너무 길면 화면이 지저분해짐)
        self.trail_x = []
        self.trail_y = []

    def update_positions(self, p1_pos, p2_pos):
        x = [0, p1_pos[0], p2_pos[0]]
        y = [0, p1_pos[1], p2_pos[1]]
        self.line.set_data(x, y)

        if self.trail_draw:
            # 궤적 기록 (p2 끝단 위치만)
            self.trail_x.append(p2_pos[0])
            self.trail_y.append(p2_pos[1])

            # 너무 길어지면 앞부분 잘라내기
            # if len(self.trail_x) > self.trail_length:
            #     self.trail_x = self.trail_x[-self.trail_length:]
            #     self.trail_y = self.trail_y[-self.trail_length:]

            self.trail_line.set_data(self.trail_x, self.trail_y)

        return self.line, self.trail_line