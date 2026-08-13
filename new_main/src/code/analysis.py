# src/code/analysis.py
import numpy as np
import pandas as pd


def load_reference(filepath):
    """CSV 또는 Excel에서 기준 궤적 불러오기"""
    if filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath, header=None)
        header_row = df.iloc[2, 1:9].tolist()  # B~I열 (3행이 헤더)
        data_rows = df.iloc[4:, 0:9].copy()     # 5행부터 데이터
        data_rows.columns = ["time"] + header_row
        data_rows = data_rows.dropna(subset=["time"]).reset_index(drop=True)
        return data_rows


def compute_lyapunov(current_history, reference_df):
    """
    current_history: pendulum.history (theta1/theta2/omega1/omega2 포함하는 dict 리스트)
    reference_df: load_reference()로 불러온 DataFrame

    반환: (리아푸노프 지수, 사용된 시간 배열, 로그거리 배열)
    """
    current_df = pd.DataFrame(current_history)

    use_angles = all(c in reference_df.columns for c in ["theta1", "theta2", "omega1", "omega2"])
    if not use_angles:
        raise ValueError(
            "기준 파일에 theta1/theta2/omega1/omega2 데이터가 없습니다. "
            "리아푸노프 비교는 CSV로 저장된 파일을 사용해주세요."
        )

    n = min(len(current_df), len(reference_df))
    cur = current_df.iloc[:n].reset_index(drop=True)
    ref = reference_df.iloc[:n].reset_index(drop=True)

    diff = np.sqrt(
        (cur["theta1"] - ref["theta1"].astype(float)) ** 2 +
        (cur["theta2"] - ref["theta2"].astype(float)) ** 2 +
        (cur["omega1"] - ref["omega1"].astype(float)) ** 2 +
        (cur["omega2"] - ref["omega2"].astype(float)) ** 2
    ).values

    time = cur["time"].values

    valid = diff > 1e-12
    if valid.sum() < 2:
        raise ValueError("두 궤적이 거의 동일하거나 데이터가 부족해 계산할 수 없습니다.")

    log_diff = np.log(diff[valid])
    t_valid = time[valid]

    slope, intercept = np.polyfit(t_valid, log_diff, 1)
    return slope, t_valid, log_diff