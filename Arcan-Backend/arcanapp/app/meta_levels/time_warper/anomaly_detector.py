import numpy as np

def detect_anomalies(time_series):
    threshold = np.std(time_series) * 2
    mean = np.mean(time_series)
    anomalies = [(i, val) for i, val in enumerate(time_series) if abs(val - mean) > threshold]
    return anomalies
