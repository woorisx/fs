import numpy as np

data = [10, 20, 20, 25, 30, 1000] # 1000이라는 이상치가 포함됨

print(f"산술 평균: {np.mean(data)}")   # 216.0 (이상치 때문에 높게 나옴)
print(f"중앙값: {np.median(data)}")     # 20.0 중간이 되는 값 : 중앙값 (실제 데이터의 중심을 더 잘 반영)


'''
산술평균: 184.1666
중앙값 : 22.5
'''

from scipy import stats
import numpy as np

data = [10, 30, 30, 30, 20, 20, 1000]
mode_result = stats.mode(data, keepdims=True) # keepdims 차원을 유지하다.

print(f"최빈값: {mode_result.mode}") # 30 
print(f"최빈값: {mode_result.mode[0]}") # 20
print(f"출현 횟수: {mode_result.count[0]}") # 2

'''
최빈값 : 20
출현 횟수 : 2
'''


import pandas as pd

data = [10, 30, 30, 20, 20, 1000]
series = pd.Series(data)

print(f"최빈값: {series.mode()}") # 20
print(f"최빈값: {series.mode()[0]}") # 20
print(f"최빈값: {series.mode()[1]}") # 30

'''
최빈값: 0    20
1    30
dtype: int64
최빈값: 20
최빈값: 30
'''

import statistics

data = [10, 20, 20, 30, 30, 1000]
print(f"최빈값: {statistics.mode(data)}") # 최빈값: 20


# 모든 최빈값을 리스트로 반환
all_modes = statistics.multimode(data)

print(all_modes)      # [20, 30]
print(all_modes[0])   # 20
print(all_modes[1])   # 30 (이제 [1] 사용 가능!)