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