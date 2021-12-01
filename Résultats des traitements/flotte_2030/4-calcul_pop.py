import pandas as pd

##########
########## Variables
##########


fic_pers = "../../Prévisions futur/pop_municip_2011-2018.csv"
fic_mun = "municipalites_od.csv"

facteur = 1.102514

##########
########## Imports
##########

pers = pd.read_csv(fic_pers, encoding = "ISO-8859-1")
mun = pd.read_csv(fic_mun)[["MUS_CO_GEO", "MUS_NM_MUN"]].rename(columns={"MUS_CO_GEO":'CG_FIXE'})


##########
########## Code
##########

pers = pers.query("SEXE == 3 and CG_FIXE != '?' and ANNEE == 2018")


pers["CG_FIXE"] = pd.to_numeric(pers["CG_FIXE"])


pers = mun.merge(pers)

hab_2018 = pers.TOTAL.sum()

hab_2030 = hab_2018 * facteur

pd.DataFrame({"annee":[2018, 2030], "pop":[hab_2018, hab_2030]}).to_csv("population_2030.csv")
