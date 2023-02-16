# 수도권 교통량을 통한 휴게소 매출 전략
```
1. 수도권 교통량 분석(주간, 2023년 2월)
2. 서울 교통량 분석(1일 1시간 단위)
3. 서울 만남의 광장 휴게소 매출 순위
4. 데이터 분석을 통한 판매 전략
```
## 1. 수도권 교통량 분석
```python
import csv
import matplotlib.pyplot as plt
#------------------------------------------------------------------------day1 일
f1=open('C:\python\day8\\traffic\day5.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day1 = []
for row in data1:
    AllTrafic_day1.append(int(row[10]))
#------------------------------------------------------------------------day2 월
f1=open('C:\python\day8\\traffic\day6.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day2 = []
for row in data1:
    AllTrafic_day2.append(int(row[10]))
#------------------------------------------------------------------------day3 화
f1=open('C:\python\day8\\traffic\day7.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day3 = []
for row in data1:
    AllTrafic_day3.append(int(row[10]))
#------------------------------------------------------------------------day4 수
f1=open('C:\python\day8\\traffic\day8.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day4 = []
for row in data1:
    AllTrafic_day4.append(int(row[10]))
#------------------------------------------------------------------------day5 목
f1=open('C:\python\day8\\traffic\day9.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day5 = []
for row in data1:
    AllTrafic_day5.append(int(row[10]))
#------------------------------------------------------------------------day6 금
f1=open('C:\python\day8\\traffic\day10.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day6 = []
for row in data1:
    AllTrafic_day6.append(int(row[10]))
#------------------------------------------------------------------------day7 토
f1=open('C:\python\day8\\traffic\day11.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day7 = []
for row in data1:
    AllTrafic_day7.append(int(row[10]))

plt.subplot(2,4,1)
plt.plot(AllTrafic_day1)
plt.title('sunday')
plt.ylabel('traffic')
plt.subplot(2,4,2)
plt.plot(AllTrafic_day2)
plt.title('monday')
plt.ylabel('traffic')
plt.subplot(2,4,3)
plt.plot(AllTrafic_day3)
plt.title('tuesday')
plt.ylabel('traffic')
plt.subplot(2,4,4)
plt.plot(AllTrafic_day4)
plt.title('wendsday')
plt.ylabel('traffic')
plt.subplot(2,4,5)
plt.plot(AllTrafic_day5)
plt.title('thursday')
plt.ylabel('traffic')
plt.subplot(2,4,6)
plt.plot(AllTrafic_day6)
plt.title('friday')
plt.ylabel('traffic')
plt.subplot(2,4,7)
plt.plot(AllTrafic_day7)
plt.title('satarday')
plt.ylabel('traffic')


AllTrafic_day1 = sum(AllTrafic_day1)
AllTrafic_day2 = sum(AllTrafic_day2)
AllTrafic_day3 = sum(AllTrafic_day3)
AllTrafic_day4 = sum(AllTrafic_day4)
AllTrafic_day5 = sum(AllTrafic_day5)
AllTrafic_day6 = sum(AllTrafic_day6)
AllTrafic_day7 = sum(AllTrafic_day7)

AllTraffic = {'sun':AllTrafic_day1,'mon':AllTrafic_day2,'tue':AllTrafic_day3,'wed':AllTrafic_day4,'thu':AllTrafic_day5,'fri':AllTrafic_day6,'sat':AllTrafic_day7}

# plt.subplot(2,4,8)
plt.plot(AllTraffic.keys(),AllTraffic.values())
plt.title('All Traffic of week')
plt.xlabel('day of week')
plt.ylabel('traffic')
plt.show()
```
![TrafficOfWeek](https://user-images.githubusercontent.com/113449058/219298757-15aed1ed-f584-4cdd-880b-05864ba30156.png)
```
2023년 2월 5일부터 2023년 2월 11일까지의 1주간 데이터입니다.
8번째 image는 1주일간 총 교통량을 시각화한 그래프입니다.
```
## 2. 서울 교통량 분석
```python
import csv
import numpy as np
import matplotlib.pyplot as plt

f1=open('C:\python\day8\\traffic\mon_traffic.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
MonTraffic = []
for row in data1:
    if int(row[2]) == 101:
        MonTraffic.append(int(row[13]))

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

MonTraffic = list_chunk(MonTraffic,4)
MonTraffic = np.array(MonTraffic)
MonTraffic = np.sum(MonTraffic,axis=1)

plt.subplot(2,1,1)
plt.plot(MonTraffic)
plt.title('traffic of time (seoul, day2)')
plt.xlabel('time')
plt.ylabel('traffic')

#-----------------------------------------------------------------------

f1=open('C:\python\day8\\traffic\\fri_traffic.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
FriTraffic = []
for row in data1:
    if int(row[2]) == 101:
        FriTraffic.append(int(row[13]))

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

FriTraffic = list_chunk(FriTraffic,4)
FriTraffic = np.array(FriTraffic)
FriTraffic = np.sum(FriTraffic,axis=1)

plt.subplot(2,1,2)
plt.plot(FriTraffic)
plt.title('traffic of time (seoul, day6)')
plt.xlabel('time')
plt.ylabel('traffic')
plt.show()
```
```
수도권 중 가장 많은 교통량을 보인 서울을 중심으로 데이터를 분석했습니다.
1주간 총 교통량 그래프의 상승폭이 큰 두 요일을 선정했습니다.(월,금)
```
