"""
Recalcule les distances avec le triplab (on autorise 5km d'ecart entre la demande et le resultat du cemin donne)
"""

import requests
#import geopandas as gpd
import pandas as pd
import shapely.geometry as geo
import matplotlib.pyplot as plt
import geopy.distance


##########
########## variables
##########

fic_od18 = 'outs_V2/calculé_od18_complet.pkl'	# le fichier de base pour les rendus GQIS
#fic_od18 = 'tests/traj_erreurs.shp'	# le fichier créé par ce script

on_enreg = True
nom_enreg = 'outs_V2/calculé_od18_completV2.pkl'
#nom_enreg_traj = 'tests/traj_erreurs_calcules_du_lab.shp'

CRS_lonlat = "EPSG:4326"


#"""

##########
########## import des bases
##########

print('import des bases...')
od18 = pd.read_pickle(fic_od18)
print('importé, longueur = {}\n'.format(len(od18)))



#"""

##########
########## fonctions
##########


"""
def filtre(dist, LOO, LAO, LOD, LAD):
	# donne si oui ou non on garde cette ligne
	if dist not in [-1, 0]:
		return False
	elif (LOO, LAO) == (0, 0) or (LOD, LAD) == (0, 0):
		return True
	elif (abs(LOO + 69.7505) < 0.001 and abs(LAO - 45.0783) < 0.001):
		#print(LOO, LAO)
		return False
	elif  (abs(LOD + 69.7505) < 0.001 and abs(LAD - 45.0783) < 0.001):
		#print(LOD, LAD)
		return False
	else:
		return False



def calcul_distance(pt1, pt2):
	# pour 2 couples de coordonnees renvoie la distance
	return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)
"""
def calcul_distance(pt1, pt2):
	# pour 2 couples de coordonnees renvoie la distance
	if pt1[0] < -90 or pt1[0] > 90 or pt2[0] < -90 or pt2[0] > 90:
		return 1000000
	else:
		return geopy.distance.geodesic(pt1, pt2).km





def tripdist(mode,olat,olon,dlat,dlon):
	# renvoie la distance au reseau pour des coordonnees longitude et latitude donnees
	dist_query = 'https://mapper.triplab.ca/osrm/route/v1/{}/{},{};{},{}?geometries=geojson'.format(mode,format(olat, 'f'),format(olon, 'f'),format(dlat, 'f'),format(dlon, 'f'))
	query = requests.get(dist_query)
	
	cles_dispo = query.json().keys()
	if 'routes' not in cles_dispo:	
		print(dist_query)
		print(query.json())
		if query.json()['code'] == 'InvalidQuery':
			return 1, -2, ([], [], [], []), -1 # code erreur 1 : 'routes' pas dans les cles ET ['code'] == 'InvalidQuery'
		else:
			return 2, -2, ([], [], [], []), -1 # code erreur 2 : 'routes' pas dans les cles
	
	distance = query.json()['routes'][0]['distance']
	pto0, pto1 = (olat, olon), query.json()['routes'][0]['geometry']['coordinates'][0]
	ptd0, ptd1 = (dlat, dlon), query.json()['routes'][0]['geometry']['coordinates'][-1]
	ecart_o = calcul_distance(pto0, pto1)
	ecart_d = calcul_distance(ptd0, ptd1)
	x, y = [], []
	probleme = (ecart_o + ecart_d > 5)
	if probleme:
		#print('\t\t', ecart_o, ecart_d)
		for pt in query.json()['routes'][0]['geometry']['coordinates']:
			x.append(pt[0])
			y.append(pt[1])
	if probleme:
		return 3, distance, (x, y, pto0, ptd0), 0 # code erreur 3 : O ou D trop loin des trucs calcules
	else:
		return 0, distance, (x, y, pto0, ptd0), (ecart_o + ecart_d) # code erreur 0 : tout s'est bien passe

def revoit_lgn(data, i):
	# regarde la ligne de la base de donnees et revoit la distance calculee si ya eu un probleme precedemment, renvoie nouvelle distance et nouveau code erreur et l'ecart entre les deux pts de dep et les deux pts d'arrivee, plus si oui ou non la base a ete modifiee
	err = data.code_err.iloc[i]
	if err != 0:
		nouv_err, nouv_dist, nouv_donn, nouv_ecart = tripdist('driving', data['LONORIG'].iloc[i], data['LATORIG'].iloc[i], data['LONDEST'].iloc[i], data['LATDEST'].iloc[i])
		if nouv_err == 0:
			return nouv_dist, nouv_err, nouv_ecart, 1
		else:
			return data.dist_calc.iloc[i], data.code_err.iloc[i], 0, 0
	else:
		return data.dist_calc.iloc[i], data.code_err.iloc[i], 0, 0
		
def verifie_modifs(l1, l2):
	# compte le nombre d'elements differents
	cpt = 0
	for i in range(max(len(l1), len(l2))):
		if l1[i] != l2[i]:
			cpt += 1
	return cpt

"""
def trajet(mode, olat, olon, dlat, dlon):
	dist_query = 'https://mapper.triplab.ca/osrm/route/v1/{}/{},{};{},{}?geometries=geojson'.format(mode,format(olat, 'f'),format(olon, 'f'),format(dlat, 'f'),format(dlon, 'f'))
	query = requests.get(dist_query)

	cles_dispo = query.json().keys()	
	if 'routes' not in cles_dispo:
		if query.json()['code'] == 'InvalidQuery':
			return geo.LineString([(-1, -1), (1, 1)])
		else:
			return geo.LineString([(-1, 1), (1, -1)])
	distance = query.json()['routes'][0]['distance']
	traj = geo.LineString(query.json()['routes'][0]['geometry']['coordinates'])
	return traj, distance




#"""
##########
########## Filtrage des trajets qui nous intéressent
##########
"""

print('filtrage des erreurs...')
od18_err = pd.DataFrame(od18.drop('geometry', 1))
od18_err['filtre'] = od18_err.apply(lambda x : filtre(x['distances_'], x['LONORIG'], x['LATORIG'], x['LONDEST'], x['LATDEST']), axis=1)
od18_err = od18_err.query('filtre == True')
print('filtré, longueur : {}\n'.format(len(od18_err)))



#"""
##########
########## Calcul des trajets
##########
print("nombre d'erreurs actuel : {}".format(len(od18.query('code_err != 0'))))

print('revue des lignes...')
erreurs = []
dists = []
ecart_accumule = 0
nb_modifs = 0

for i in range(len(od18)):
	if i % 1000 == 0:
		print(i)
	travail = revoit_lgn(od18, i)
	dists.append(travail[0])
	erreurs.append(travail[1])
	ecart_accumule += travail[2]
	nb_modifs += travail[3]
print('fin des requetes\n')


print('verifications...')
modifs = verifie_modifs(list(od18.dist_calc), dists)

print("l'ecart accumule est de {} km".format(ecart_accumule))
print("{} lignes ont ete modifiees".format(modifs))
print("{} km par ligne".format(ecart_accumule/modifs))

if modifs == nb_modifs:
	print("modification de la base...")
	od18['dist_calc'] = dists
	od18['code_err'] = erreurs
else:
	print("les modifs collent pas : {} selon le prgm et {} comptees".format(nb_modifs, modifs))

print("nombre d'erreurs actuel : {}".format(len(od18.query('code_err != 0'))))



if on_enreg:
	print("Enregistrement...")
	od18.to_pickle(nom_enreg)
	print('les vrais trajets enregistrés sous {}'.format(nom_enreg))


"""

od18_err2 = gpd.GeoDataFrame(od18_err, geometry = ([geo.LineString([(c[0], c[1]), (c[2], c[3])]) for c in zip(od18_err.LONORIG, od18_err.LATORIG, od18_err.LONDEST, od18_err.LATDEST)]), crs = CRS_lonlat) # on reprend la base avec comme geometrie une droite OD

if on_enreg:
	print('enregistrement...')
	od18_err2.to_file(nom_enreg_droits)
	print('les droites enregistrées sous {}'.format(nom_enreg_droits))


# apply(lambda x: tripdist(m,hall_bldg[0],hall_bldg[1],x['Longitude'],x['Latitude']),axis=1)

#"""
### Tests





#"""
### modif des erreurs






#"""
### enregistrement




#"""
"""
Ce qui est fait :
une base avec les trajets calcules, une avec les droits. Tout le reste c'est la copie conforme (dont feuillet, rang, nodeplac)

Les trajets de Maine ou au (0, 0) sont pas pris dans la base
	-> Il faudra les prendre en compte plus tard !

certains ne marchent toujours pas, ils auront un trajet calculé de [(0, 0), (1, 1)]
	-> Il faudra les prendre en compte plus tard !

Pour décider ce qu'on fait on peut voir quels trajets sont à accepter (genre l'aéroport) et lesquels ne le sont pas

"""
