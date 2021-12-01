"""
Cree la base AD-SM
"""

print("import biblios...")
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

print("importé\n")


##########
########## Variables
##########

fichier_AD = 'aires_diff/lad_000b16a_f.shp' # aires de diffusion
trucs_a_garder_fichier_AD = ['ADIDU', 'geometry'] # colonnes a garder
CRS_AD = 'EPSG:3347'

fichier_ARTM = '../eod18_geomatique/shapefile-SM' # secteurs municipaux
trucs_a_garder_fichier_ARTM = ['Sm100', 'Descrip', 'MI_Sup_km2', 'geometry'] # colonnes a garder
CRS_ARTM = 'EPSG:32188'


nom_distances = "Enquêtes OD et distances/outs_V2/calculé_od18_complet_AD.pkl"
nom_fic = "tests/tests_overlay.shp"

on_enreg = True
nom_enreg = "outs/equivalence_AD_SM.pkl"

petits_ratios = {'24663371':105, '24662992':136, '24662419':136, '24660984':128, '24663437':102, '24661591':120, '24670028':543}


##########
########## import des bases
##########

print('import base...')
geodiff = gpd.read_file(fichier_AD).query("PRNOM == 'Quebec / Québec'")[trucs_a_garder_fichier_AD]
ARTM = gpd.read_file(fichier_ARTM)[trucs_a_garder_fichier_ARTM]
distances = pd.read_pickle(nom_distances)['ADIDU']
print('importé\n')




##########
########## Code
##########


print("calcul overlay...")
over = gpd.overlay(geodiff, ARTM.to_crs(CRS_AD), how='intersection').merge(distances)
print("longueur overlay avant coupage :", len(over))

over["aire"] = over.area

print("reassignement des AD")


#d = {"ADIDU" : [], "aire_AD" : []}

final = {"ADIDU":[], "Sm100":[]}

for ADIDU, data in over.groupby('ADIDU'):
	final["ADIDU"].append(ADIDU)
	#d["ADIDU"].append(ADIDU)
	#d["aire_AD"].append(data.aire.sum())
	l = list(data.aire)
	l.sort()
	if len(l) > 1:
		if l[-1]/l[-2] <= 4:
			final["Sm100"].append(petits_ratios[ADIDU])
		else:
			final["Sm100"].append(data.query("aire == @l[-1]").Sm100.iloc[0])
	else:
		final["Sm100"].append(data.Sm100.iloc[0])

df_fin = pd.DataFrame(final)
print(len(df_fin))


if on_enreg:
	print("enregistrement...")
	df_fin.to_pickle(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))

#"""

