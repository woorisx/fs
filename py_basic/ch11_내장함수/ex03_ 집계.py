from scipy import stats
import numpy as np

data = [10, 20, 20, 30, 1000]
mode_result = stats.mode(data, keepdims=True)

print(f"최빈값: {mode_result.mode[0]}") # 20
print(f"출현 횟수: {mode_result.count[0]}") # 2