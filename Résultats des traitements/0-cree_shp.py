"""
Cree le fichier des emissions par aire de de diffusion (en shp)
"""


import pandas as pd
import geopandas as geopd
import matplotlib.pyplot as plt

emiss = pd.read_csv('emissions_groupe.csv')
secteurs = pd.read_csv('GO_PAU_par_groupe.csv')
geodiff = geopd.read_file('aires_diff/lad_000b16a_f.shp')
# ADIDU et Shape


emiss.set_index('groupe')

emoy = []
for i in range(len(secteurs)): # lignes des secteurs
	som = 0
	tot = 0
	for j in range(10): # les diffs groupes
		som += secteurs['gr{}'.format(j)].iloc[i] * emiss.emission[j]
		tot += secteurs['gr{}'.format(j)].iloc[i] * 1
	if tot == 0:
		print(som, tot)
		emoy.append(som / tot)
		print(emoy[-1])
	else:
		emoy.append(som / tot)

secteurs['emiss_moyenne'] = emoy

fin = geodiff.merge(secteurs[['ADIDU', 'emiss_moyenne']])

fin.to_file("outs/CO2_par_km_par_AD")

emoy.sort()
print(emoy[0], emoy[-1])

