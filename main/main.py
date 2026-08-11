import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. 물리 상수 및 초기 조건
g = 9.81  # 중력 가속도 (m/s^2)
L = 1.0  # 줄 길이 (m)
dt = 0.03  # 시간 간격

theta = np.pi / 4  # 초기 각도 (45도)
omega = 0.0  # 초기 각속도
damping = 0.999  # 오차 방지용 미세 공기저항

# 2. 그래프 창 및 축 설정
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-L - 0.2, L + 0.2)
ax.set_ylim(-L - 0.2, 0.2)
ax.set_aspect('equal')  # 비율 1:1 고정
ax.grid(True)

# 진자 실과 추 (고정점 0,0 기준)
line, = ax.plot([], [], 'o-', lw=2, color='crimson', markersize=12)


def init():
    line.set_data([], [])
    return line,


# 3. 매 프레임 업데이트 함수
def update(frame):
    global theta, omega

    # 각가속도 계산 및 심플렉틱 오일러 업데이트
    alpha = -(g / L) * np.sin(theta)
    omega += alpha * dt
    omega *= damping
    theta += omega * dt

    # 좌표 변환 (Matplotlib: 아래 방향이 -y)
    x = L * np.sin(theta)
    y = -L * np.cos(theta)

    line.set_data([0, x], [0, y])
    return line,


# 4. 애니메이션 실행 (interval=30ms)
ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=30)

plt.title("Simple Pendulum (Matplotlib)")
plt.show()