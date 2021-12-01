import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

##########
########## Variables
##########

fic = "veh_ownership_qc.csv"


##########
########## Imports
##########

df = pd.read_csv(fic)

##########
########## Fonctions
##########

def flin(x, A, B):
	# la fonction a ajuster
	return A*x + B

def reglin(df):
	# renvoie les param A et B
	x = np.array(df["an"])
	y = np.array(df["veh_own"])
	params, params_covariance = optimize.curve_fit(flin, x, y)
	return params

def em2030(df, gr):
	A, B = reglin(df)
	return flin(2030, A, B)

##########
########## Code
##########

df['veh_own'] = df["veh"] / df["pop"]

a, b = reglin(df)
print(a, b)
print("2026", flin(2026, a, b))
print("2030", flin(2030, a, b))

plt.plot(df["an"], df["veh_own"])
plt.show()

