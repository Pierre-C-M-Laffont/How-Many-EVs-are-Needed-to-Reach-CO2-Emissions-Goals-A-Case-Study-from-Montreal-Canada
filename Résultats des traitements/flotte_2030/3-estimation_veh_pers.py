import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

##########
########## Variables
##########

fic_groupes = "prevision_SAAQ.csv"
fic_pers = "../../Prévisions futur/pop_municip_2011-2018.csv"
fic_mun = "municipalites_od.csv"

##########
########## Imports
##########

saaq = pd.read_csv(fic_groupes).query("an != 2030")
pers = pd.read_csv(fic_pers, encoding = "ISO-8859-1")
mun = pd.read_csv(fic_mun)[["MUS_CO_GEO", "MUS_NM_MUN"]].rename(columns={"MUS_CO_GEO":'CG_FIXE'})

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

def reglin(y):
	# renvoie les param A et B
	x = np.array(range(2011, 2019))
	params, params_covariance = optimize.curve_fit(flin, x, y)
	return params

def em2030(y):
	A, B = reglin(y)
	return flin(2030, A, B)

##########
########## Code
##########


# Filtre sur les municipalités pop totale
pers = pers.query("SEXE == 3 and CG_FIXE != '?' and ANNEE >= 2011 and ANNEE <= 2018")


pers["CG_FIXE"] = pd.to_numeric(pers["CG_FIXE"])


pers = mun.merge(pers)

print(pers)


print(pers.groupby("ANNEE").sum()["TOTAL"])

df = pers.groupby("ANNEE").sum()["TOTAL"]
print(saaq.veh_tot)

df = np.array(saaq.veh_tot)/df

print(df)

em = em2030(df)

df[2030] = em


plt.plot(df)
plt.show()

print(df)

df.to_csv("possession_auto.csv", header=True)

