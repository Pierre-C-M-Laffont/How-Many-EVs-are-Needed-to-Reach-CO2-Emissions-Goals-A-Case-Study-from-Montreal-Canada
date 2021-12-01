"""
Pour l'ajout de variables comme les émissions annuelles, la suppression de variables ou bien un simple aperçu
"""


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##########
########## Variables
##########

nom_carte_AD = "outs/emissions_final_par_AD"
nom_carte_SM = "outs/emissions_final_par_SM"
nom_veh_SAAQ = "GO_PAU_par_groupe.csv"
nom_eq_AD_SM = "outs/equivalence_AD_SM.pkl"
nom_SM_brut = "../eod18_geomatique/shapefile-SM"
nom_veh_selon_OD = "Enquêtes OD et distances/donnees_geo/veh_AD.pkl"

on_enreg = False

##########
########## Import des bases
##########

print("import des bases...")
AD = gpd.read_file(nom_carte_AD)
SM = gpd.read_file(nom_carte_SM)
print("importé\n")

########## Imports supplémentaires
"""
print('import vehicules selon AD...')
veh = pd.read_pickle(nom_veh_selon_OD).rename(columns={'AD':"ADIDU", 'nb_veh_AD':'nb_veh_OD'})

print("import SAAQ...")
SAAQ = pd.read_csv(nom_veh_SAAQ)
print("importé")	

print('import equivalences AD SM...')
AD_SM = pd.read_pickle(nom_eq_AD_SM)
print("importé\n")

print('import SM brut (pour les noms)...')
SM_brut = gpd.read_file(nom_SM_brut)[["Sm100", "Descrip"]]
print("importé\n")

#"""
##########
########## Fonctions utiles
##########

def suppr_extremes(valeur, valeur_max, remplacement):
	if valeur > valeur_max:
		print("1 remplacement")
		return remplacement
	else:
		return valeur

##########
########## Code
##########

########## Suppression de colonnes
"""
print("suppression de colonnes...")
colonnes_a_supprimer_SM = ["tCO2/an/pe"]
colonnes_a_supprimer_AD = ["tCO2/an/pe"]

AD = AD.drop(columns = colonnes_a_supprimer_AD)
SM = SM.drop(columns = colonnes_a_supprimer_SM)

print("fait\n")
#"""
########## Emissions annuelles par secteur
"""
print("calcul des emissions annuelles...")
facteur_multi = 335

AD["tCO2/an/AD"] = AD.apply(lambda x : x["tCO2/AD"] * facteur_multi, axis=1)
SM["tCO2/an/SM"] = SM.apply(lambda x : x["tCO2/SM"] * facteur_multi, axis=1)

print("fait\n")
#"""
########## Emissions annuelles par personne
"""	
print("calcul des emissions annuelles par personne...")

AD["tCO2/an/pe"] = AD.apply(lambda x : x["tCO2/an/AD"] / x["nb_pers"], axis=1)
SM["tCO2/an/pe"] = SM.apply(lambda x : x["tCO2/an/SM"] / x["nb_pers"], axis=1)

print("fait\n")
#"""
########## Nb de véhicules par AD / SM (fait le 7 mai)
"""
print("calcul du nombre de véhicules par AD ou SM...")

SAAQ["nb_veh"] = SAAQ.apply(lambda x : x["no_corr"] + x["gr0"] + x["gr1"] + x["gr2"] + x["gr3"] + x["gr4"] + x["gr5"] + x["gr6"] + x["gr7"] + x["gr8"] + x["gr9"], axis=1)
SAAQ2 = SAAQ[["ADIDU", "nb_veh"]]
AD = AD.merge(SAAQ2)

veh_SM = SAAQ.merge(AD_SM).groupby('Sm100', as_index=False).agg("sum", as_index=False)[["Sm100", "nb_veh"]]
SM = SM.merge(veh_SM)

print("vérification : nombre de véh au total sur le territoire = {} = {} = {}\n\n\n".format(AD.nb_veh.sum(),SM.nb_veh.sum() ,sum([SAAQ.merge(AD_SM)['gr{}'.format(i)].sum() for i in range(10)]) + SAAQ.merge(AD_SM).no_corr.sum()))
print("fait\n")
#"""
########## tCO2/veh/an (fait le 7 mai)
"""
print("calcul des tCO2 par véhicule par an...")

AD['tCO2/an/ve'] = AD.apply(lambda x : x['tCO2/an/AD'] / max(x["nb_veh"], 0.0000000000000001), axis=1)
SM['tCO2/an/ve'] = SM.apply(lambda x : x['tCO2/an/SM'] / max(x["nb_veh"], 0.0000000000000001), axis=1)

print("fait\n")
#"""
########## km/veh/an (fait le 7 mai)
"""
print("calcul des km par véhicule par jour...")

AD['km/jr/ve'] = AD.apply(lambda x : x['km_totaux'] / max(x["nb_veh"], 0.0000000000000001), axis=1)
SM['km/jr/ve'] = SM.apply(lambda x : x['km_totaux'] / max(x["nb_veh"], 0.0000000000000001), axis=1)

print("fait\n")
#"""
########## rectification km/veh/an (fait le 12 mai)
"""
print("rectification des km/veh/jour...")
AD['km/jr/ve'] = AD.apply(lambda x : suppr_extremes(x['km/jr/ve'], 1000000, 0), axis=1)

print("fait\n")
#"""
########## veh/pers (fait le 12 mai)
"""
print("calcul du nb de vehicules par personne...")
AD['veh/pers'] = AD.apply(lambda x : x['nb_veh']/x['nb_pers'], axis=1)
SM['veh/pers'] = SM.apply(lambda x : x['nb_veh']/x['nb_pers'], axis=1)

print("fait\n")
#"""
########## Nom des SM (fait le 12 mai)
"""
print("ajout des noms des SM...")
SM = SM.merge(SM_brut)

print("fait\n")
#"""
########## Vehicules selon OD (fait le 26 mai)
"""
print("calcul du nb de vehicules selon AD...")
AD = AD.merge(veh)

trav = AD_SM.merge(AD)
#trav['nb_veh_AD'] = trav.apply(lambda x : int(x['nb_veh_AD']), axis=1)
trav = trav.groupby('Sm100', as_index=False).sum()

SM = SM.merge(trav[['Sm100', 'nb_veh_OD']])

print("fait\n")
#"""
########## Diff relative véhicules (fait le 27 mai)
"""
AD['frac_veh'] = AD.apply(lambda x : x['nb_veh_OD'] / max(0.0000000001, x['nb_veh']), axis=1)
SM['frac_veh'] = SM.apply(lambda x : x['nb_veh_OD'] / max(0.0000000001, x['nb_veh']), axis=1)
#"""
########## Aperçu

print("aperçu\n\n")
print(AD.head(10))
print(SM.head(10))

print("\n\n")
#"""
########## Rearrangement des colonnes (fait le 12 mai)
"""
print("rearrangement des colonnes...")
AD = AD[['ADIDU', 'aires', 'nb_pers', 'nb_veh', 'nb_veh_OD', 'frac_veh', 'veh/pers', 'gCO2/km', 'km_totaux', 'km/hab', 'km/jr/ve', 'tCO2/AD', 'kgCO2/pers', 'gCO2/m2', 'tCO2/an/AD', 'tCO2/an/pe', 'tCO2/an/ve', 'geometry']]

SM = SM[['Sm100', 'Descrip', 'aires', 'nb_pers', 'nb_veh', 'frac_veh', 'nb_veh_OD', 'veh/pers', 'gCO2/km', 'km_totaux', 'km/hab', 'km/jr/ve', 'tCO2/SM', 'kgCO2/pers', 'gCO2/m2', 'tCO2/an/SM', 'tCO2/an/pe', 'tCO2/an/ve', 'geometry']]

print('fait\n')
#"""
##########
########## enregistrement
##########


if on_enreg:
	print("enregistrement...")
	AD.to_file(nom_carte_AD)
	SM.to_file(nom_carte_SM)
	print("enregistré")
