"""
Cree de nouvelles cartes a partir de celle de base, par exemple des aggregations aux secteurs municipaux
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

##########
########## Variables
##########

nom_carte_base = "outs/emissions_final_par_AD"

# LE truc a changer (colonnes ADIDU et 'truc_sur_quoi_grouper')
nom_equivalence = "outs/equivalence_AD_SM.pkl"
truc_sur_quoi_grouper = 'Sm100'

nom_emiss = 'emissions_groupe.csv'

nom_secteurs = 'GO_PAU_par_groupe.csv'

on_enreg = True
nom_enreg = 'outs/emissions_final_par_SM'

##########
########## Import des bases
##########

print("import des bases...")
equivalence = pd.read_pickle(nom_equivalence)
emiss = pd.read_csv(nom_emiss)
secteurs = pd.read_csv(nom_secteurs)
base = gpd.read_file(nom_carte_base)[['ADIDU', 'km_totaux', 'nb_pers', 'aires', 'geometry']]
print("importé\n")



##########
########## Fonctions utiles
##########

def calcule_moyenne(df, emiss):
	# pour une base df donnee, calcule et retourne les emissions moyennes
	som = 0
	tot = 0
	for i in range(len(df)): # lignes des secteurs
		for j in range(10): # les diffs groupes
			som += df['gr{}'.format(j)].iloc[i] * emiss.emission[j]
			tot += df['gr{}'.format(j)].iloc[i] * 1
	if som == 0:
		print(som, tot)
	return (som / tot)



##########
########## Code
##########



print("calcul des emissions moyennes...")
travail = secteurs.merge(equivalence)

final = {truc_sur_quoi_grouper: [], "gCO2/km":[]}

for code, df in travail.groupby(truc_sur_quoi_grouper):
	final[truc_sur_quoi_grouper].append(code)
	final["gCO2/km"].append(calcule_moyenne(df, emiss))

emiss_moyennes = pd.DataFrame(final)
print(emiss_moyennes)




print("merge et calcul des emissions totales...")
resultat = base.merge(equivalence).drop(columns=['ADIDU']).dissolve(by=truc_sur_quoi_grouper, as_index=False, aggfunc = 'sum').merge(emiss_moyennes) # aggfunc

#resultat["aires"] = resultat.to_crs({'proj':'cea'})['geometry'].area
resultat['tCO2/SM'] = resultat.apply(lambda x : x['gCO2/km'] * x['km_totaux']/1000000, axis=1)
print('fait\n')

print('calcul des variables dérivées...')
resultat["km/hab"] = resultat["km_totaux"] / resultat["nb_pers"]
resultat["gCO2/m2"] = resultat["tCO2/SM"] / resultat["aires"]*1000000
resultat["kgCO2/pers"] = resultat["tCO2/SM"] / resultat["nb_pers"]*1000


if on_enreg:
	print("enregistrement")
	resultat.to_file(nom_enreg)
	print("enregistré dans {}".format(nom_enreg))

#"""
