import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

# 1. 물리 상수 설정
g = 15.0
L1, L2 = 1.0, 0.8
m1, m2 = 2.0, 0.3
dt = 0.003
SUB_STEPS = 5
DAMPING = 0.9999  # 수치적 에너지 폭발을 막아주는 미세 감쇄

theta1, theta2 = 3.0, 3.0
omega1, omega2 = 2.0, -3.0

trail_x, trail_y = [], []


def get_derivatives(t1, t2, w1, w2):
    delta = t1 - t2
    den1 = L1 * (2 * m1 + m2 - m2 * np.cos(2 * t1 - 2 * t2))
    num1 = (
        -g * (2 * m1 + m2) * np.sin(t1)
        - m2 * g * np.sin(t1 - 2 * t2)
        - 2 * np.sin(delta) * m2 * (w2**2 * L2 + w1**2 * L1 * np.cos(delta))
    )
    alpha1 = num1 / den1

    den2 = L2 * (2 * m1 + m2 - m2 * np.cos(2 * t1 - 2 * t2))
    num2 = (
        2
        * np.sin(delta)
        * (
            w1**2 * L1 * (m1 + m2)
            + g * (m1 + m2) * np.cos(t1)
            + w2**2 * L2 * m2 * np.cos(delta)
        )
    )
    alpha2 = num2 / den2
    return alpha1, alpha2


fig, ax = plt.subplots(figsize=(7, 7), facecolor='black')
lim = L1 + L2 + 0.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

(line,) = ax.plot([], [], 'o-', lw=2, color='white', markersize=6)
lc = LineCollection([], linewidths=1.2, alpha=0.8)
ax.add_collection(lc)


def update(frame):
    global theta1, theta2, omega1, omega2

    for _ in range(SUB_STEPS):
        a1, a2 = get_derivatives(theta1, theta2, omega1, omega2)

        omega1 += a1 * dt
        omega2 += a2 * dt

        # 에너지가 무한대로 터지는 것 방지
        omega1 *= DAMPING
        omega2 *= DAMPING

        theta1 += omega1 * dt
        theta2 += omega2 * dt

        # 핵심: 각도가 무한히 커지지 않게 -pi ~ pi 범위로 정규화 (Overflow 방지)
        theta1 = (theta1 + np.pi) % (2 * np.pi) - np.pi
        theta2 = (theta2 + np.pi) % (2 * np.pi) - np.pi

        x1 = L1 * np.sin(theta1)
        y1 = -L1 * np.cos(theta1)
        x2 = x1 + L2 * np.sin(theta2)
        y2 = y1 - L2 * np.cos(theta2)

        trail_x.append(x2)
        trail_y.append(y2)

    line.set_data([0, x1, x2], [0, y1, y2])

    if len(trail_x) > 1:
        points = np.array([trail_x, trail_y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        hues = (np.arange(len(segments)) % 300) / 300.0
        colors = plt.cm.rainbow(hues)

        lc.set_segments(segments)
        lc.set_color(colors)

    return line, lc


ani = animation.FuncAnimation(
    fig, update, interval=15, blit=True, cache_frame_data=False
)

plt.show()