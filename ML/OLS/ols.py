import pandas as pd
import numpy as np
nx = input("Enter elements in X: ")
xl = nx.split()
for i in range(len(xl)):
    xl[i] = float(xl[i])
print (xl)
ny = input("Enter elements in Y: ")
yl = ny.split()
for i in range(len(yl)):
    yl[i] = float(yl[i])
print (yl)

data = {'X':xl,'Y':yl}
df = pd.DataFrame(data)
xm = df['X'].mean()
ym = df['Y'].mean()

df['xi - xb'] = df['X'] - xm
df['yi - yb'] = df['Y'] - ym
df['xi - xb * yi - yb'] = (df['xi - xb']*df['yi - yb'])
df['xi - xb * xi - xb'] = (df['xi - xb']*df['xi - xb'])

nsum = df['xi - xb * yi - yb'].sum()
dsum = df['xi - xb * xi - xb'].sum()

p1 = round(nsum/dsum,3)
p0 = round(ym - p1*(xm),3)
print("\n -------------------------------\n" )
print(f'line is : y^ = {p1}*x + {p0}')
print("\n -------------------------------\n" )
n = int(input("Enter how many values need to be predicted: "))
for i in range(0,n):
    xv = float(input("Enter the x value: "))
    value = round(p1*xv + p0,3)
    print(f'The value at {xv} is: {value}')








