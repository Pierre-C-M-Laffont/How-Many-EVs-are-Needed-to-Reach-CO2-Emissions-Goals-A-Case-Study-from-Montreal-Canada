"""
Modifie les trajets des bases multimodales pour en faire une base de trajets unimodaux qu'on calculera avec la fonction de base (du coup plusieurs lignes potentiellement pour un meme trajet)
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


# pour voir si une sequence doit etre prise en compte ou non
condition_filtre = "('1' in modes or '2' in modes or '11' in modes or '12' in modes) and '13' not in modes and '4' not in modes and '16' not in modes"

CRS_lonlat = "EPSG:4326"
CRS_domiciles = "EPSG:2950"

on_enregistre = True
nom_enreg = "outs_V2/semibrut_od18_multimodal.pkl"

# pour faire des tests
echantillon = False
taille_ech = 10

# a supprimer
les_bons = {}
les_pas_bons = {}



##########
########## import des bases
##########

print("import des bases")
od18 = pd.read_pickle(nom_OD)
if echantillon:
	od18 = od18.head(taille_ech)
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
	for modes in sousseq:
		if eval(condition_filtre):
			res.append(modes)
			inds.append(i)
			if str(modes) not in les_bons.keys():
				les_bons[str(modes)] = 1
			else:
				les_bons[str(modes)] += 1
		else:
			if str(modes) not in les_pas_bons.keys():
				les_pas_bons[str(modes)] = 1
			else:
				les_pas_bons[str(modes)] += 1
		i += 1
	return res, inds

def liste_coord(data, jonc, i):
	# pour une base data, jonctions et un indice de ligne, renvoie la liste des coordonnees a passer dans le tripdist
	feu = data.FEUILLET.iloc[i]
	rang = data.RANG.iloc[i]
	nodep = data.NODEPLAC.iloc[i]
#	print(feu, rang, nodep)
#	print(rearrange(data.SEQ_MODES.iloc[i], '', []))
	test, inds = filtre_sousseq(sousseq(data.LISTE_SEQ.iloc[i]))
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



##########
########## Debut des calculs
##########

# creation de la nouvelle base
dico = dict()
for col in od18.columns:
	dico[col] = []
dico['no_segment'] = []


print('creation de la nouvelle base...')
for i in range(len(od18)):
	if i % 100 == 0:
		print(i)
	l = liste_coord(od18, geojon, i)
	j = 0
	for x in l:
		# copie de la ligne dans le dico
		for col in od18.columns:
			dico[col].append(od18[col].iloc[i])
		#mise a jour des coordonnees
		dico['LONORIG'][-1] = x[0]
		dico['LATORIG'][-1] = x[1]
		dico['LONDEST'][-1] = x[2]
		dico['LATDEST'][-1] = x[3]
		dico['no_segment'].append(j)
		j += 1
print('fin\n')

od182 = pd.DataFrame(dico)

print("les bons")
for x in les_bons.keys():
	print("\t", x, "\t", les_bons[x])
print("\nLes pas bons")
for x in les_pas_bons.keys():
	print("\t", x, "\t", les_pas_bons[x])

print("\n\nLongueur base finale : {}".format(len(od182)))

##########
########## Enregistrement
##########

if on_enregistre:
	print("enregistrement...")
	od182.to_pickle(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))


