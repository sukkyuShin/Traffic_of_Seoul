import csv
import numpy as np
import matplotlib.pyplot as plt

f1=open('C:\python\day8\\traffic\\foodrank.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
Rank1 = []
for row in data1:
    if row[3].startswith('?„œ?š¸ë§Œë‚¨'):
        Rank1.append(row[5:8:2])


SeoulRank = {1:Rank1[0],2:Rank1[1],3:Rank1[2],4:Rank1[3],5:Rank1[4]}


for i in range(len(SeoulRank)):
        print(SeoulRank[i+1])
