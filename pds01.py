import csv     # imports the csv module
import sys      # imports the sys module
import pandas as pd
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    print(row)

n = 0 # number of rows
s = 0 #sum of row 6
for row in open('TB_burden_countries_2014-09-29.csv'):
    n=n+1;
print(n)

f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    try:
        row[6]=float(row[6])
        s=s+row[6]
    except:
        next(f)
print(s)

a = s/n
print(a)
#%%

si = 0
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    if row[5] == '1990':
        try:
            row[6]=float(row[6])
            si=si+row[6]
        except:
            next(f)
print(si)
ai = si/n
print(ai)

#%%
se = 0
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    if row[5] == '2011':
        try:
            row[6]=float(row[6])
            se=se+row[6]
        except:
            next(f)
print(se)
ae = se/n
print(ae)



#%%
import numpy as np

ar = []
for i in range(5,16,1):
    ar.append(i) 
print(ar)

av = []
for j in range(0,23,7):
    av.append(j) 
print(av)

ak=[]
for j in range(11):
    ak.append(np.random.uniform(low=-1.0, high=1.0, size=None))
print(ak)
#%%
import matplotlib.pyplot as plt

plt.hist(ak,bins=10)


#%%
a=[]
for i in range(10):
    a.append(np.random.uniform(low=-1.0, high=1.0, size=None))

b=[]
for j in range(10):
    b.append(np.random.uniform(low=-1.0, high=1.0, size=None))

d =np.sqrt(np.sum(np.square(a[i]-b[j])))
print(d)
    

