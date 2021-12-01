"""
Travail et calculs en tout genre sur la base de données finale
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import shapely.geometry as geo

##########
########## variables
##########

nom_AD = "outs/emissions_final_par_AD"
nom_SM = "outs/emissions_final_par_SM"



##########
########## import
##########

print("import base")
AD = gpd.read_file(nom_AD).drop(columns=['geometry'])
SM = gpd.read_file(nom_SM).drop(columns=['geometry'])
print("importé\n")




##########
########## Stats globales
##########
"""
print("aperçu de la base :\n")
print(AD, '\n')
print(SM)

print("\n\n\n\nStatistiques sur les variables :\n")
print(AD.describe(), '\n')
print(SM.describe())

#"""
##########
########## Visus
##########
"""


emiss.plot.scatter("aires", y="kgCO2/pers")
emiss.plot.scatter(x="aires", y="gCO2/km")
#plt.scatter(emiss["emiss_tot"], emiss["nb_pers"], label = 'groupe {}'.format(i), alpha = 0.4, s = taille)

plt.show()

#"""
##########
########## Stats 1
##########
"""
print(emiss.rename(columns={'tCO2/pers':'filtre'}).query("filtre > 5").ADIDU.iloc[0])

od_a_tester = pd.read_pickle(fic_od)

od_a_tester = od_a_tester.query('ADIDU == "24650514"')
print(od_a_tester.head(10))

lignes = []

for i in range(len(od_a_tester)):
	geo.LineString([(od_a_tester.LONORIG.iloc[i], od_a_tester.LATORIG.iloc[i]), (od_a_tester.LONDEST.iloc[i], od_a_tester.LATDEST.iloc[i])])
	lignes.append(geo.LineString([(od_a_tester.LONORIG.iloc[i], od_a_tester.LATORIG.iloc[i]), (od_a_tester.LONDEST.iloc[i], od_a_tester.LATDEST.iloc[i])]))

map_de_test = gpd.GeoDataFrame(od_a_tester.drop(['LISTE_SEQ'], 1), geometry = lignes, crs = CRS_lonlat)

map_de_test.to_file('tests/AD_high_emiss.shp')
#"""


##########
########## Stats 2 : calcul des émissions totales
##########

"""
print("\n\nNb de personnes \n\tbase AD : {}\n\tbase SM : {}\n".format(AD.nb_pers.sum(), SM.nb_pers.sum()))

print("Emissions de CO2 (en tonnes) \n\tbase AD : {}\n\tbase SM : {}\n".format(AD["tCO2/an/AD"].sum(), SM["tCO2/an/SM"].sum()))

print("km par personne \n\tbase AD : {}\n\tbase SM : {}\n".format(AD["km_totaux"].sum()/AD["nb_pers"].sum(), SM["km_totaux"].sum()/SM["nb_pers"].sum()))

print("Emissions annuelles par personne (en tonnes)\n\tBase AD : {}\n\tBase SM : {}".format(AD["tCO2/an/AD"].sum()/AD["nb_pers"].sum(), SM["tCO2/an/SM"].sum()/SM["nb_pers"].sum()))

#"""

##########
########## Stats 3 : Densité de pop
##########
"""
AD['densite'] = AD.aires / AD.nb_pers
SM['densite'] = SM.aires / SM.nb_pers

print(AD.densite.describe())
print(SM.densite.describe())

AD.densite.hist()
plt.figure()
SM.densite.hist()

pd.DataFrame(AD).plot.scatter(y="densite", x="aires")
plt.ylim([0, 100000])
plt.xlim([0, 500000])
pd.DataFrame(SM).plot.scatter(y="densite", x="aires")
plt.ylim([0, 10000])
plt.show()

#"""
##########
########## Stats 4 : Véhicules
##########
"""
pd.DataFrame(SM).hist('frac_veh')
plt.show()

print(SM.frac_veh.describe())

#"""
##########
########## Stats 5 : Résultats article
##########

print(SM.nb_pers.min(), SM.nb_pers.max())
a=SM.nb_pers.min()
b = SM.nb_pers.max()
print(SM.query("nb_pers==@a or nb_pers == @b"))

"""
res = SM[["veh/pers", "gCO2/km", "km/hab", "km/jr/ve", "tCO2/an/pe", "tCO2/an/ve", "tCO2/an/SM"]].describe()
print(res)
#res.to_csv('outs/stats_SM.csv')

print("pour le total :")
print("MtCO2/an : ", SM['tCO2/an/SM'].sum()/1000000, "\ntCO2/an/ve : ", SM['tCO2/an/SM'].sum()/SM.nb_veh.sum(), "\ntCO2/an/pe : ", SM['tCO2/an/SM'].sum()/SM.nb_pers.sum())

#"""
