"""
Merge les differentes bases creees depuis cree_base et dont les distances ont ete claculees separement
"""

import pandas as pd
import geopandas as gpd



### variables utilisées

trajets_de_base = "outs_V2/calculé_od18_unimodal.pkl"
trajets_multi = "outs_V2/calculé_od18_multimodal.pkl"

bases_a_concat = [trajets_de_base, trajets_multi] # tous les trucs a concatener

on_enregistre = True
nom_final = "outs_V2/calculé_od18_complet.pkl"





### import bases

print("import bases")
od18s = [pd.read_pickle(n) for n in bases_a_concat]
print("importé\n")




### tests
cols = [[x for x in od18s[i].columns] for i in range(len(od18s))]
drops = [[] for i in range(len(od18s))]

print("de base pas presents :")
for i in range(len(cols)):
	print("base {}".format(i))
	for x in cols[i]:
		for b2 in cols:
			if x not in b2 and x not in drops[i]:
				print(x)
				drops[i].append(x)
	print()


print("\nLongueurs des bases :")
c = 0
for b in od18s:
	c += len(b)
	print(len(b))
print("somme = ", c)




### merge de toutes les bases
print("\nCreation final")
#final = od18s[0].drop(drops[0], 1).append([od18s[i].drop(drops[i], 1) for i in range(1, len(od18s))])
final = od18s[0].append([od18s[i] for i in range(1, len(od18s))], sort=False)

print("créé, longueur : {}\n".format(len(final)))



### enregistrement
if on_enregistre:
	print("enregistrement")
	final.to_pickle(nom_final)
	print("enregistré sous {}".format(nom_final))
