"""
Pareil que le 3 mais avec les distances multimodales

Le truc c'est de faire pareil mais en découpant les trajets en morceaux avec les jonctions. Ce sera plus dur de gerer les erreurs du coup.
"""

import pandas as pd
import geopandas as gpd
import requests
import geopy

##########
########## Nom des varaibles
##########

nom_OD = "outs_V2/brut_od18_multimodal.pkl"
nom_jonctions = "Fichiers_bruts/jonctions.csv"

ens_ok = {"['2']", "['1']", "['11', '1']", "['1', '2']", "['11', '2']", "['11']", "['2', '2']", "['1', '11']", "['2', '1']", "['2', '11']", "['2', '1', '2']"}

CRS_lonlat = "EPSG:4326"
CRS_domiciles = "EPSG:2950"

on_enregistre = False
nom_enreg = "outs_V2/calculé_od18_mulltimodal.shp"

##########
########## import des bases
##########

print("import des bases")
od18 = pd.read_pickle(nom_OD)
print("longueur OD  {}".format(len(od18)))

jon = pd.read_csv(nom_jonctions)
geojon = gpd.GeoDataFrame(jon, geometry = gpd.points_from_xy(jon.XJONC, jon.YJONC), crs = CRS_domiciles)
print("longueur jonctions  {}".format(len(geojon)))
print("importé\n")

print("modif coordonnees")
geojon["XJONC"] = geojon.to_crs(CRS_lonlat).geometry.x
geojon["YJONC"] = geojon.to_crs(CRS_lonlat).geometry.y
print("modifié\n\n")


##########
########## Fonctions utiles
##########
"""
def rearrange(seq, current, resu):
	# liste des modes utilises
	if seq == '':
		return [current] + resu
	elif current == '':
		return rearrange(seq[:-1], seq[-1], resu)
	elif len(current) == 2:
		return rearrange(seq[:-1], seq[-1], [current] + resu)
	elif seq[-1] == " ":
		return rearrange(seq[:-2], seq[-2], [current] + resu)
	else:
		return rearrange(seq[:-1], seq[-1] + current, resu)
"""

def sousseq(seq):
	# coupe la liste de base selon les '17'
	res = []
	travail = seq
	while '17' in travail:
		i = travail.index('17')
		res.append(travail[:i])
		travail = travail[i+1:]
	res.append(travail)
	return res

def filtre_sousseq(sousseq):
	# selectionne les sous-listes qui correspondent a ce qu'on veut prendre en compte
	i = 0
	res = []
	inds = []
	for l in sousseq:
		if str(l) in ens_ok:
			res.append(l)
			inds.append(i)
		i += 1
	return res, inds

"""
recup origine -> en premier
recup le deplacement
pour toutes les jonctions :
	convertir les x y en lat lon
	ajouter a la liste
ajouter la destination
faire une liste de coordonnees lon lat pour les jonctions
on appelle avec la liste des indices
requete
"""

def liste_coord(data, jonc, i):
	# pour une base data, jonctions et un indice de ligne, renvoie la liste des coordonnees a passer dans le tripdist
	feu = data.FEUILLET.iloc[i]
	rang = data.RANG.iloc[i]
	nodep = data.NODEPLAC.iloc[i]
#	print(feu, rang, nodep)
#	print(rearrange(data.SEQ_MODES.iloc[i], '', []))
	test, inds = filtre_sousseq(sousseq(rearrange(data.SEQ_MODES.iloc[i], '', [])))
#	print(test)
	jon = jonc.query('FEUILLET == @feu and RANG == @rang and NODEPLAC == @nodep')
#	print(jon)
	coord = [(0, 0)]*(2+len(jon))
	coord[0] = (data.LONORIG.iloc[i], data.LATORIG.iloc[i])
	for j in range(len(jon)):
		coord[jon.NO_JONC.iloc[j]] = (jon.XJONC.iloc[j], jon.YJONC.iloc[j])
	coord[-1] = (data.LONDEST.iloc[i], data.LATDEST.iloc[i])
	res = []
	for i in inds:
		res.append((coord[i][0], coord[i][1], coord[i+1][0], coord[i+1][1]))
	return res


def calcul_distance(pt1, pt2):
	# pour 2 couples de coordonnees renvoie la distance
	return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)


def tripdist(mode,olat,olon,dlat,dlon):
	# renvoie la distance au reseau pour des coordonnees longitude et latitude donnees
	dist_query = 'https://mapper.triplab.ca/osrm/route/v1/{}/{},{};{},{}?geometries=geojson'.format(mode,olat,olon,dlat,dlon)
	query = requests.get(dist_query)
	
	cles_dispo = query.json().keys()
	if 'routes' not in cles_dispo:	
		print(dist_query)
		print(query.json())
		if query.json()['code'] == 'InvalidQuery':
			return True, -2, ([], [], [], [])
	
	distance = query.json()['routes'][0]['distance']
	pto0, pto1 = (olat, olon), query.json()['routes'][0]['geometry']['coordinates'][0]
	ptd0, ptd1 = (dlat, dlon), query.json()['routes'][0]['geometry']['coordinates'][-1]
	ecart_o = calcul_distance(pto0, pto1)
	ecart_d = calcul_distance(ptd0, ptd1)
	x, y = [], []
	probleme = (ecart_o > 0.00001 or ecart_d > 0.00001)
	if probleme:
		print('\t\t', ecart_o, ecart_d)
		for pt in query.json()['routes'][0]['geometry']['coordinates']:
			x.append(pt[0])
			y.append(pt[1])
#		plt.plot(x, y, 'r')
#		plt.plot(pto0[0], pto0[1], 'b+')
#		plt.plot(ptd0[0], ptd0[1], 'b+')
#		plt.show()
	# renvoie si ca a declenche une erreur, la distance calculee, puis les donnees relatives a l'erreur (coordonnees x et y du chemin, plus depart et arrivee)
	return probleme, distance, (x, y, pto0, ptd0)


#def distance_trajet(

### Debut des calculs



"""
print(geojon.geometry.iloc[0])
print(geojon.to_crs(CRS_lonlat).geometry.iloc[0])
print(geojon.to_crs(CRS_lonlat).geometry.iloc[0].y)
print(geojon.YJONC.iloc[0])



for i in range(len(od18)):
	_, inds = filtre_sousseq(sousseq(rearrange(od18.SEQ_MODES.iloc[i], '', [])))
	if len(inds) > 1:
		print(liste_coord(od18, geojon, i))
		print("\n\n")
"""

print("calcul des distances")
travail = [0] * len(od18)
nb_err = 0
for i in range(len(od18)):
	if i % 100 == 0:
		print(i)
	l = liste_coord(od18, geojon, i)
	cpt = 0
	for x in l:
		prob, dist, donnees = (tripdist('driving', x[0], x[1], x[2], x[3]))
		if not prob:
			cpt += dist
		else:
			nb_err += 1
	travail[i] = dist

od18['distances_calculees'] = travail
print("calculé\n\nNombre d'erreurs : {}".format(nb_err))

if on_enregistre:
	print("enregistrement")
	od18.to_file(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))
#"""
