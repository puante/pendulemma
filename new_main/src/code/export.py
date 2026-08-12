# export.py
import numpy as np
import pandas as pd
from openpyxl import Workbook


def _compute_kinematics(pendulum):
    """기록된 각도/각속도/각가속도로부터 위치·속도(x,y) 계산"""
    hist = pd.DataFrame(pendulum.history)
    L1 = pendulum.p1["length"]
    L2 = pendulum.p2["length"]

    t1, t2 = hist["theta1"].values, hist["theta2"].values
    w1, w2 = hist["omega1"].values, hist["omega2"].values

    # 위치
    x1 = L1 * np.sin(t1)
    y1 = -L1 * np.cos(t1)
    x2 = x1 + L2 * np.sin(t2)
    y2 = y1 - L2 * np.cos(t2)

    # 속도
    vx1 = L1 * np.cos(t1) * w1
    vy1 = L1 * np.sin(t1) * w1
    vx2 = vx1 + L2 * np.cos(t2) * w2
    vy2 = vy1 + L2 * np.sin(t2) * w2

    hist["p1pos_x"], hist["p1pos_y"] = x1, y1
    hist["p2pos_x"], hist["p2pos_y"] = x2, y2
    hist["p1v_x"], hist["p1v_y"] = vx1, vy1
    hist["p2v_x"], hist["p2v_y"] = vx2, vy2

    return hist


def export_to_excel(pendulum, filepath):
    hist = _compute_kinematics(pendulum)

    wb = Workbook()
    ws = wb.active

    # 1행: 초기조건 헤더
    header1 = ["p1mass", "p1velocity", "p1theta0", "p1omega0",
               "p2mass", "p2velocity", "p2theta0", "p2omega0"]
    for col, text in zip("BCDEFGHI", header1):
        ws[f"{col}1"] = text
    ws["K1"] = "dt"

    # 2행: Default (초기조건 값)
    ws["A2"] = "Default"
    ws["B2"] = pendulum.p1["mass"]
    ws["C2"] = pendulum.p1["omega0"]      # p1velocity = 초기 각속도(omega0)와 동일하게 기록
    ws["D2"] = pendulum.p1["theta0"]
    ws["E2"] = pendulum.p1["omega0"]
    ws["F2"] = pendulum.p2["mass"]
    ws["G2"] = pendulum.p2["omega0"]      # p2velocity = 초기 각속도(omega0)와 동일하게 기록
    ws["H2"] = pendulum.p2["theta0"]
    ws["I2"] = pendulum.p2["omega0"]
    ws["K2"] = pendulum.dt

    # 3행: 시계열 데이터 헤더
    header3 = ["p1pos_x", "p1pos_y", "p2pos_x", "p2pos_y",
               "p1v_x", "p1v_y", "p2v_x", "p2v_y"]
    for col, text in zip("BCDEFGHI", header3):
        ws[f"{col}3"] = text

    # 4행: time 라벨
    ws["A4"] = "time"

    # 5행부터: 실제 시계열 데이터
    cols_order = ["time", "p1pos_x", "p1pos_y", "p2pos_x", "p2pos_y",
                  "p1v_x", "p1v_y", "p2v_x", "p2v_y"]

    for row_idx, row in enumerate(hist[cols_order].itertuples(index=False), start=5):
        for col_letter, value in zip("ABCDEFGHI", row):
            ws[f"{col_letter}{row_idx}"] = value

    wb.save(filepath)


def export_to_csv(pendulum, filepath):
    """CSV는 병합 레이아웃 없이 표 형태로 단순하게"""
    hist = _compute_kinematics(pendulum)
    cols_order = ["time", "theta1", "theta2", "omega1", "omega2",
                  "p1pos_x", "p1pos_y", "p2pos_x", "p2pos_y",
                  "p1v_x", "p1v_y", "p2v_x", "p2v_y"]
    hist[cols_order].to_csv(filepath, index=False)


if __name__ == "__main__":
    from pendulum_calculate import Pendulum
    # 테스트 데이터
    test_data = {
        "system_data": {"g": 9.80665, "dt": 0.001},
        "pendulum_data": {
            "p1": {"mass": 1.0, "length": 1.0, "theta0": 1.5, "omega0": 0.0},
            "p2": {"mass": 1.0, "length": 1.0, "theta0": 1.0, "omega0": 0.0},
        }
    }

    p = Pendulum(test_data)

    # 몇 스텝 돌려서 history를 채움
    for _ in range(200):
        p.update()

    print(f"기록된 스텝 수: {len(p.history)}")

    # 실제로 내보내기 실행
    export_to_excel(p, "test_output.xlsx")
    export_to_csv(p, "test_output.csv")

    print("완료: test_output.xlsx, test_output.csv 생성됨")