"""
Recalcule les distances aves HERE (necessite une cle API pour faire les requetes)
"""




"""
maxi = 9

def arbol(i, li):
	if i > maxi:
		print(i*'---'+'***')
	else:
		print(i*'---'+'liste:')
		for j in li:
			if type(j) == list:
				arbol(i+1, j)
			elif type(j) == dict:
				arbod(i+1, j)
			else:
				print((i+1)*'---'+str(type(j)))

def arbod(i, dico):
	if i > maxi:
		print(i*'---'+'***')
	else:
		print(i*'---'+'dico :')
		for k in dico.keys():
			print((i+1)*'---'+str(k)+':')
			if type(dico[k]) == list:
				arbol(i+2, dico[k])
			elif type(dico[k]) == dict:
				arbod(i+2, dico[k])
			else:
				print((i+2)*'---'+str(type(dico[k])))

"""


print('import biblios...')
import time
import pandas as pd
import shapely.geometry as geo
import requests
import geopy.distance
print('importé\n')


##########
########## variables
##########

# cle api
cle_api = open('HERE/cle_api.txt').read()[:-1]


fic_a_voir = 'outs_V2/calculé_od18_completV2.pkl'

on_enreg = True
nom_enreg = 'outs_V2/calculé_od18_completV3.pkl'

ligne_acceptee = '(data.LONORIG.iloc[i], data.LATORIG.iloc[i]) != (0, 0) and (data.LONDEST.iloc[i], data.LATDEST.iloc[i]) != (0, 0)'


##########
########## Import des bases
##########

print('import bases...')
od18 = pd.read_pickle(fic_a_voir)
print('importé, longueur : {}\n'.format(len(od18)))



##########
########## Fonctions
##########

def calcul_distance(pt1, pt2):
	# pour 2 couples de coordonnees renvoie la distance
	if pt1[0] < -90 or pt1[0] > 90 or pt2[0] < -90 or pt2[0] > 90:
		return 1000000
	else:
		return geopy.distance.geodesic(pt1, pt2).km



def get_path(req):
	# renvoie ttes les infos necessaires (ligne droite, chemin, distance, temps)
	if 'response' in req.keys():
		trav = req['response']['route'][0]['leg'][0]
		trav2 = trav['start']['mappedPosition']
		pt_dep = trav2['longitude'], trav2['latitude']
		trav2 = trav['end']['mappedPosition']
		pt_arr = trav2['longitude'], trav2['latitude']
		dist = trav['length']
		tps = trav['travelTime']
		trav2 = trav['maneuver']
		l = []
		for x in trav2:
			l.append((x['position']['longitude'],x['position']['latitude']))
		return ((pt_dep, pt_arr), l, dist, tps)
	else :
		return (0, 0, 0, 0)
		




def requete(olon, olat, dlon, dlat):
	# renvoie le resu de la requete
#	url = 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json?apiKey={}&waypoint0=geo!{},{}&waypoint1=geo!{}\
#,{}&mode=shortest;car;traffic:disabled'.format(cle_api, olat, olon, dlat, dlon)
	url = 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json?apiKey={}&waypoint0=geo!{},{}&waypoint1=geo!{},{}&mode=fastest;car;traffic:disabled'.format(cle_api, format(olat, 'f'),format(olon, 'f'),format(dlat, 'f'),format(dlon, 'f'))
	return requests.get(url).json()

"""
def recup_geoms(req):
	# renvoie la geom en lgn droite et la geom en chemin comme il faut, plus la distance
	res = get_path(req)
	if res == (0, 0, 0, 0):
		print(req)
		return geo.LineString([(1, 1), (-1, -1)]), geo.LineString([(1, 1), (-1, -1)]), -1
	else :
		return geo.LineString([xy for xy in res[0]]), geo.LineString([xy for xy in res[1]]), res[2]
"""




def revoit_lgn(data, i):
	# regarde la ligne de la base de donnees et revoit la distance calculee si ya eu un probleme precedemment, renvoie nouvelle distance et nouveau code erreur et l'ecart entre les deux pts de dep et les deux pts d'arrivee, plus si oui ou non la base a ete modifiee
	err = data.code_err.iloc[i]
	if err != 0 and eval(ligne_acceptee): # ligne acceptee pour filtrer sur les lignes qu'on veut pas calculer
		nouv_donnees = get_path(requete(data.LONORIG.iloc[i], data.LATORIG.iloc[i], data.LONDEST.iloc[i], data.LATDEST.iloc[i]))
		if nouv_donnees == (0, 0, 0, 0):
			print("pas de reponse...")
			return data.dist_calc.iloc[i], data.code_err.iloc[i], 0, 0
		else:
			extremites = nouv_donnees[0]
			ecart_tot = calcul_distance(extremites[0], (data.LONORIG.iloc[i], data.LATORIG.iloc[i])) + calcul_distance(extremites[1], (data.LONDEST.iloc[i], data.LATDEST.iloc[i]))
			if ecart_tot > 5:
				return data.dist_calc.iloc[i], data.code_err.iloc[i], 0, 0
			else:
				return nouv_donnees[2], 0, ecart_tot, 1
	else:
		return data.dist_calc.iloc[i], data.code_err.iloc[i], 0, 0


def verifie_modifs(l1, l2):
	# compte le nombre d'elements differents
	cpt = 0
	for i in range(max(len(l1), len(l2))):
		if l1[i] != l2[i]:
			cpt += 1
	return cpt



##########
########## Code
##########


"""print('tests clé api')
print(cle_api)
print('https://route.ls.hereapi.com/routing/7.2/calculateroute.json?apiKey={}&waypoint\n\n'.format(cle_api))"""

print("nombre d'erreurs actuel : {}\n".format(len(od18.query('code_err != 0'))))

print("debut calculs")
code_err = []
dist = []
ecart_tot = 0
nb_modif = 0

for i in range(len(od18)):
	if i % 1000 == 0:
		print(i)
	n_dist, n_code_err, n_ecart, n_modif = revoit_lgn(od18, i)
	dist.append(n_dist)
	code_err.append(n_code_err)
	ecart_tot += n_ecart
	nb_modif += n_modif



print('\nverifications...')
modifs = verifie_modifs(list(od18.dist_calc), dist)

print("l'ecart accumule est de {} km".format(ecart_tot))
print("{} lignes ont ete modifiees".format(modifs))
print("{} km par ligne\n".format(ecart_tot/modifs))

if modifs == nb_modif:
	print("modification de la base...")
	od18['dist_calc'] = dist
	od18['code_err'] = code_err
else:
	print("les modifs collent pas : {} selon le prgm et {} comptees".format(nb_modif, modifs))

print("nombre d'erreurs actuel : {}\n".format(len(od18.query('code_err != 0'))))


if on_enreg:
	print("enregistrement...")
	od18.to_pickle(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))


	
