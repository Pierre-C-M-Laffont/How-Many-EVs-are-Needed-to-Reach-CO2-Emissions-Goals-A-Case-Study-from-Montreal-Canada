
print("import biblios...")
import geopandas as gpd
import pandas as pd
import os
import matplotlib.pyplot as plt
print("importé\n")


##########
########## Chemins vers les differents docs
##########


fichier_distances = "Enquêtes OD et distances/outs_V2/calculé_od18_complet_AD.pkl"
fichier_emissions = "outs/CO2_par_km_par_AD"
#fichier_habitants = "Enquêtes OD et distances/donnees_AD/hab_AD.pkl"

nom_enreg = "outs/emissions_final_par_AD"

enreg = True


##########
########## import des bases
##########


print("import distances...")
dist = pd.read_pickle(fichier_distances).rename(columns={"dist_tot":"km_totaux"})
#print("import personnes...")
#pers = pd.read_pickle(fichier_habitants)
print("impory emissions...")
emiss = gpd.read_file(fichier_emissions)[["ADIDU", "emiss_moye", "geometry"]].rename(columns={"emiss_moye":"gCO2/km"})
print("importé\n")





##########
########## calculs
##########


print("merge et calcul des emissions totales...")
resultat = emiss.merge(dist)
resultat["aires"] = resultat.to_crs({'proj':'cea'})['geometry'].area
resultat['tCO2/AD'] = resultat.apply(lambda x : x['gCO2/km'] * x['km_totaux']/1000000, axis=1)
print("mergé\n")



resultat["km/hab"] = resultat["km_totaux"] / resultat["nb_pers"]
resultat["gCO2/m2"] = resultat["tCO2/AD"] / resultat["aires"]*1000000
resultat["kgCO2/pers"] = resultat["tCO2/AD"] / resultat["nb_pers"]*1000

print(resultat.head(10))

resultat['kgCO2/pers'].hist()
plt.show()

if enreg:
	print("enregistrement")
	resultat.to_file(nom_enreg)
	print("enregistré dans {}".format(nom_enreg))
