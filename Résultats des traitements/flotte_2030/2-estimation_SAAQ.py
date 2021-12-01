import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

##########
########## Variables
##########

fic_groupes = "groupes_SAAQ.csv"


##########
########## Imports
##########

saaq = pd.read_csv(fic_groupes)

##########
########## Fonctions
##########

def nlles_col(df):
	for i in range(10):
		trav = pd.Series(df['gr0'])
		for j in range(1, i+1):
			trav += df['gr{}'.format(j)]
		df['cumul{}'.format(i)] = trav

def flin(x, A, B):
	# la fonction a ajuster
	return A*x + B

def reglin(df, gr):
	# renvoie les param A et B
	x = np.array(df["an"])
	y = np.array(df["gr{}".format(gr)])
	params, params_covariance = optimize.curve_fit(flin, x, y)
	return params

def em2030(df, gr):
	A, B = reglin(df.query("an >=2015"), gr)
	return flin(2030, A, B)

##########
########## Code
##########

saaq["veh_tot"] = saaq["gr0"] + saaq["gr1"] + saaq["gr2"] + saaq["gr3"] + saaq["gr4"] + saaq["gr5"] + saaq["gr6"] + saaq["gr7"] + saaq["gr8"] + saaq["gr9"]


for i in range(10):
	saaq['gr{}'.format(i)] = saaq['gr{}'.format(i)] / saaq.veh_tot

plt.figure()
for i in range(10):
	plt.plot(saaq.an, saaq['gr{}'.format(i)])

nlles_col(saaq)

plt.figure()
for i in range(10):
	plt.plot(saaq.an, saaq['cumul{}'.format(i)])

print(saaq)



d = {"an" : [2030]}

for i in range(10):
	d["gr{}".format(i)] = [em2030(saaq, i)]


saaq = saaq.append(pd.DataFrame(d))

saaq = saaq.set_index("an")

saaq.loc[2030, "gr8"] += saaq.loc[2030, "gr9"]
saaq.loc[2030, "gr9"] -= saaq.loc[2030, "gr9"]

plt.figure()
for i in range(10):
	plt.plot(saaq.index, saaq['gr{}'.format(i)])

nlles_col(saaq)

plt.figure()
for i in range(10):
	plt.plot(saaq.index, saaq['cumul{}'.format(i)])

print(saaq)

plt.show()

#saaq.to_csv("prevision_SAAQ.csv")
