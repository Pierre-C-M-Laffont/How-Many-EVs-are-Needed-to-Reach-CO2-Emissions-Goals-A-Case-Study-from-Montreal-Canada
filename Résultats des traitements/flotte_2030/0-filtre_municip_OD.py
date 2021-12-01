"""
Objectif : crérer un csv avec les vcodes de municip à garder dans les bases de la province
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

##########
########## Variables
##########

fic_OD = "../../eod18_geomatique/shapefile-limiteOD"
fic_municip = "../../municipalites_all_Qc/munic_s.shp"

nom_a_enreg = "municipalites_od.csv"

CRS_municip = 'EPSG:4269'
CRS_ARTM = 'EPSG:32188'

##########
########## Imports
##########

od = gpd.read_file(fic_OD)
mun = gpd.read_file(fic_municip)


##########
########## Fonctions
##########




##########
########## Code
##########
print(mun.columns)
print(od.columns)


print("jointure...")
new = gpd.sjoin(mun.to_crs(CRS_ARTM), od[["geometry"]], op='intersects')
new["AIRE"] = new.geometry.area
print("join2")
new = gpd.overlay(new, od[["geometry"]], how="intersection")


new["test"] = new.geometry.area / new["AIRE"]

"""
part1 = new.query("test < 0.3")
part2 = new.query('test >= 0.3 and test < 0.8')
part3 = new.query("test >= 0.8")

part1.to_file("p1.shp")
part2.to_file("p2.shp")
part3.to_file("p3.shp")


l = list(new["test"])
l.sort()
v = [l[i+1]/l[i] for i in range(len(l)-1)]

print(l)

plt.plot(l)

print(new["test"].describe())
#pd.DataFrame(new).aire.plot.hist()
plt.show()

"""
print("enregistrement...")
pd.DataFrame(new.query("test > 0.8")[["MUS_CO_GEO", "MUS_NM_MUN"]]).to_csv(nom_a_enreg)
print("enregistré")
"""
#"""
