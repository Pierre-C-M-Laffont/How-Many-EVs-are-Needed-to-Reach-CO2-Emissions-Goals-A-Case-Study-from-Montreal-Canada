import pandas as pd


##########
########## Variables
##########

fic_pop = "population_2030.csv"
fic_poss = "possession_auto.csv"
fic_prop = "prevision_SAAQ.csv"
fic_2018 = "../Changements_dans_flotte/veh_par_SM.csv"

##########
########## Imports
##########

pop = pd.read_csv(fic_pop).set_index("annee")
poss = pd.read_csv(fic_poss).set_index("ANNEE")
prop = pd.read_csv(fic_prop).set_index("an")
prop18 = pd.read_csv(fic_2018).set_index("Sm100").drop(columns=["nb_veh", "km_totaux", "Sm100.1"])
 

##########
########## Fonctions
##########

def cree_proportions(df):
	#pour ajouter les colonnes des proportions
	totaux = df.sum()
	for i in range(10):
		df["prop{}".format(i)] = df["gr{}".format(i)] / totaux["gr{}".format(i)]


##########
########## Code
##########

# pop
pop = pop['pop'][2030]

# nb d'autos
autos = pop * poss['TOTAL'][2030]
print(autos)

# repartition groupes
repartition = prop[["gr{}".format(i) for i in range(10)]].loc[2030] * autos

print(repartition.sum())

# repartition entre SM
cree_proportions(prop18)

for i in range(10):
	prop18["gr{}".format(i)] = (prop18["prop{}".format(i)] * repartition["gr{}".format(i)])

print(prop18[["gr{}".format(i) for i in range(10)]].sum().sum())

prop18[["gr{}".format(i) for i in range(10)]].to_csv("flotte2030.csv")


