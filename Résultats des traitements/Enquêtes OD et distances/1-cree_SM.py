"""
Récupère le fichier OD de base et y associe les SM associés à chaque déplacement, enregistre
"""

import os
import pandas as pd
import geopandas as gpd

##########
########## Chemins vers les documents
##########

path_od18 = "Fichiers_bruts/OD18_brut.pkl"

path_SM = "../../eod18_geomatique/shapefile-SM"

current_path = os.getcwd()


##########
########## Variables utilisees
##########

CRS_AD = "EPSG:3347"
CRS_domiciles = "EPSG:2950"

colonnes_SM = ['Sm100', 'Descrip', 'geometry']
colonnes_od18 = ["IPERE", "FEUILLET", "NODEPLAC", "RANG", "XDOMI", "YDOMI"]
colonnes_a_enreg = ["IPERE", "FEUILLET", "RANG", "NODEPLAC", 'Sm100', 'Descrip']


on_enreg = True
nom_enreg = 'outs_V2/SM_des_deplac.pkl'

##########
########## import od18
##########

print("import OD18...")
od18 = pd.read_pickle(path_od18)
print("importé")
print("longueur", len(od18))
print()


print("filtrage sur les colonnes")
od18 = od18[colonnes_od18]
print()
#"""

##########
########## Fusion avec aires de diff
##########

print("traitement geo des domiciles de l'OD...")
geoOD18 = gpd.GeoDataFrame(od18, geometry = gpd.points_from_xy(od18.XDOMI, od18.YDOMI), crs = CRS_domiciles)

print("import aires de diffusion...")
geoSM = gpd.read_file(path_SM).to_crs(CRS_domiciles)[colonnes_SM]

print("Merging...")
od18 = gpd.sjoin(geoOD18, geoSM, how="inner", op='intersects')[colonnes_a_enreg]
print("Mergé\n")

print(od18.head(10))
#"""

##########
########## Enregistrement
##########

if on_enreg:
	print("\n\nenregistrement")
	od18.to_pickle(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))

