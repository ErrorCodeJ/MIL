import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 그래프 창을 띄우기 위한 백엔드 설정

# 데이터 읽기
df = pd.read_csv('battery_data.csv')
print("읽어온 데이터:")
print(df)

# 상황 분류
df['State'] = 'Unknown'
df.loc[df['Current'] > 2.0, 'State'] = 'Lifting'
df.loc[(df['Current'].between(1.0, 1.5)) & (df['PackVolt'] > 11.0), 'State'] = 'Driving'
df.loc[df['Current'] < 0, 'State'] = 'Charging'

# 결과 출력
print("상황별 데이터 분포:")
print(df.groupby(['State', 'BatteryType']).mean())

# 시각화
for state in ['Lifting', 'Driving', 'Charging']:
    subset = df[df['State'] == state]
    plt.figure()
    for battery in ['A', 'B']:
        data = subset[subset['BatteryType'] == battery]
        plt.plot(data['Time'], data['PackVolt'], label=f'Battery {battery}')
    plt.title(f'{state} 상황에서의 전압 변화')
    plt.xlabel('Time')
    plt.ylabel('PackVolt')
    plt.legend()
    plt.show()