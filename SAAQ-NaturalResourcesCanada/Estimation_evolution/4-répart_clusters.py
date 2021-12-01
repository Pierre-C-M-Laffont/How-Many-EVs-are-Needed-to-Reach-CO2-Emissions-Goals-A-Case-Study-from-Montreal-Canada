import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle as pk

coord_frontieres = pk.load(open("../Separateurs/frontieres-9", 'rb'))


d = {}

"""
for i in range(14):
	print(i)
	df = pd.read_csv('2018/2018_part{}.csv'.format(i))
	for j in range(len(df)):
		e = df["EMISSION"][j]
		if e in d.keys():
			d[e] += 1
		else:
			d[e] = 1
"""


for i in range(14):
	print(i)
	df = pd.read_csv('2018/2018_part{}.csv'.format(i))
	t = df.EMISSION.value_counts()
	for j in t.index:
		if j in d.keys():
			d[j] += t[j]
		else:
			d[j] = t[j]




x = [k for k in d.keys()]
x.sort()
x = np.array(x)


y = [d[k] for k in x]


plt.plot(x, y, 'b')
plt.xlabel('émissions (gCO2/km)')
plt.ylabel('nombre de véhicules')

for fr in coord_frontieres:
	plt.axvline(x=fr, c='r')


x2 = [k for k in d.keys() for i in range(d[k])]

plt.figure()
plt.hist(x2, 200)
plt.xlabel('émissions (gCO2/km)')
plt.ylabel('nombre de véhicules')
for fr in coord_frontieres:
	plt.axvline(x=fr, c='r')

plt.show()
