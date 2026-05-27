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

# 지연 원인별 분석
delay_causes = df[['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']].mean()

print(delay_causes)

delay_causes.plot(kind='bar', figsize=(10,5), color=['steelblue', 'skyblue', 'lightblue', 'navy', 'royalblue'])
plt.title('지연 원인별 평균 지연시간 (분)')
plt.xlabel('지연 원인')
plt.ylab

# 시간대별 평균 지연시간
df['Hour'] = df['CRSDepTime'] // 100

hourly_delay = df.groupby('Hour')['DepDelayMinutes'].mean()

hourly_delay.plot(kind='line', figsize=(12,5), color='steelblue', marker='o')
plt.title('시간대별 평균 출발 지연시간 (분)')
plt.xlabel('출발 시간 (시)')
plt.ylabel('평균 지연시간 (분)')
plt.xticks(range(0,24))
plt.grid(True)
plt.tight_layout()
plt.show()
