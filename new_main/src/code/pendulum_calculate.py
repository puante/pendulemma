import numpy as np

class Pendulum:
    def __init__(self, data):
        # 원점이 (0,0)
        self.data = data

        self.g = self.data["system_data"]["g"]
        self.dt = self.data["system_data"]["dt"]
        self.time = 0

        self.p1 = self.data["pendulum_data"]["p1"]
        self.p2 = self.data["pendulum_data"]["p2"]

        self.p1_pos = [self.p1["length"] * np.sin(self.p1["theta0"]), -1 * self.p1["length"] * np.cos(self.p1["theta0"])]
        self.p2_pos = [self.p1_pos[0] + self.p2["length"] * np.sin(self.p2["theta0"]),
                       self.p1_pos[1] + -1 * self.p2["length"] * np.cos((self.p2["theta0"]))]

        self.p1_angle = self.data["pendulum_data"]["p1"]["theta0"]
        self.p2_angle = self.data["pendulum_data"]["p2"]["theta0"]

        self.p1_angle_velocity = self.data["pendulum_data"]["p1"]["omega0"]
        self.p2_angle_velocity = self.data["pendulum_data"]["p2"]["omega0"]

        self.p1_angle_accelation = 0
        self.p2_angle_accelation = 0

    def get_accelaration(self):
        # (m₁+m₂)L₁θ̈₁ + m₂L₂θ̈₂cos(θ₁-θ₂) + m₂L₂θ̇₂²sin(θ₁-θ₂) + (m₁+m₂)g sinθ₁ = 0
        # L₂θ̈₂ + L₁θ̈₁cos(θ₁-θ₂) - L₁θ̇₁²sin(θ₁-θ₂) + g sinθ₂ = 0

        delta = self.p1_angle - self.p2_angle

        m1 = self.data["pendulum_data"]["p1"]["mass"]
        m2 = self.data["pendulum_data"]["p2"]["mass"]
        l1 = self.data["pendulum_data"]["p1"]["length"]
        l2 = self.data["pendulum_data"]["p2"]["length"]
        theta1 = self.p1_angle
        theta2 = self.p2_angle
        omega1 = self.p1_angle_velocity
        omega2 = self.p2_angle_velocity

        A = np.array([
            [(m1 + m2) * l1, m2 * l2 * np.cos(delta)],
            [l1 * np.cos(delta), l2]
        ])
        b = np.array([
            -m2 * l2 * omega2 ** 2 * np.sin(delta) - (m1 + m2) * self.g * np.sin(theta1),
            l1 * omega1 ** 2 * np.sin(delta) - self.g * np.sin(theta2)
        ])

        theta1_dd, theta2_dd = np.linalg.solve(A, b)
        return theta1_dd, theta2_dd

    def update(self):
        # 가속도 계산
        a1, a2 = self.get_accelaration()

        # 속도 계산
        self.p1_angle_velocity += a1 * self.dt
        self.p2_angle_velocity += a2 * self.dt

        # 각 정정
        self.p1_angle += self.p1_angle_velocity * self.dt
        self.p2_angle += self.p2_angle_velocity * self.dt

        # 위치 조정
        self.p1_pos = [self.p1["length"] * np.sin(self.p1_angle), -1 * self.p1["length"] * np.cos(self.p1_angle)]
        self.p2_pos = [self.p1_pos[0] + self.p2["length"] * np.sin(self.p2_angle),
                       self.p1_pos[1] + -1 * self.p2["length"] * np.cos(self.p2_angle)]

        # 시간 더함
        self.time += self.dt

    def get_value(self):
        return [self.p1_pos, self.p2_pos]