import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('/kaggle/input/datasets/arvindnagaonkar/flight-delat/Flight_Delay.parquet')

# 기본 정보
print("데이터 크기:", df.shape)

# 항공사별 평균 지연
airline_delay = df.groupby('Marketing_Airline_Network')['DepDelayMinutes'].mean().sort_values(ascending=False)
airline_delay.plot(kind='bar', figsize=(10,5), color='steelblue')
plt.title('항공사별 평균 출발 지연시간 (분)')
plt.xlabel('항공사')
plt.ylabel('평균 지연시간 (분)')
plt.tight_layout()
plt.show()

# 월별 평균 지연
monthly_delay = df.groupby('Month')['DepDelayMinutes'].mean()
monthly_delay.plot(kind='line', figsize=(10,5), color='steelblue', marker='o')
plt.title('월별 평균 출발 지연시간 (분)')
plt.xlabel('월')
plt.ylabel('평균 지연시간 (분)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 출발 도시별 평균 지연시간 상위 10개
city_delay = df.groupby('OriginCityName')['DepDelayMinutes'].mean().sort_values(ascending=False).head(10)
print(city_delay)
