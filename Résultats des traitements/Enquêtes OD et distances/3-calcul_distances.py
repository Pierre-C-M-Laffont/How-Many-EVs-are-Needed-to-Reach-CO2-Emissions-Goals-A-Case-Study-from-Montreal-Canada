"""
Calcul des distances parcourues avec la base donnee
"""

print('import biblios')
import os
import pandas as pd
import requests
import geopy
import matplotlib.pyplot as plt
import pickle as pk

print('importé\n')



##########
########## Variables utilisées
##########


dossier_enreg = "outs_V2/"
current_path = os.getcwd()
doc_od18 = "outs_V2/semibrut_od18_multimodal.pkl"

# pour faire les calculs sur un truc plus petit
echantillon = False
taille_ech = 200

# Stockage intermédiaire des résu
nom_liste_distances = "liste_distances_script_3.pkl"
nom_liste_erreurs = "liste_erreurs_script_3.pkl"
enreg_liste = dossier_enreg + nom_liste_distances
enreg_err = dossier_enreg + nom_liste_erreurs

# Enregistrement des résu
enregistre = True
nom_enreg = "outs_V2/calculé_od18_multimodal.pkl"




##########
########## import des bases de donnees de tavail
##########

print("import OD 18")
od18 = pd.read_pickle(doc_od18)

if echantillon:
	od18 = od18.head(taille_ech)
print("importé")
print("longueur :", len(od18))
print()
print(od18.head(10))


##########
########## Fonctions de calculs de distances et de verification
##########

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
			return 1, -2, ([], [], [], []) # code erreur 1 : 'routes' pas dans les cles ET ['code'] == 'InvalidQuery'
		else:
			return 2, -2, ([], [], [], []) # code erreur 2 : 'routes' pas dans les cles
	
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
	if probleme:
		return 3, distance, (x, y, pto0, ptd0) # code erreur 3 : O ou D trop loin des trucs calcules
	else:
		return 0, distance, (x, y, pto0, ptd0) # code erreur 0 : tout s'est bien passe


def repere_arret(l):
	# renvoie le plus petit indice a partir duquel ya que des zeros, utile pour reprendre la liste intermédiaire
	i = 1
	while l[-i] == 0:
		i += 1
	return len(l) - i




##########
########## calcul des distances
##########

print("calc des dist")

print("recuperation de la liste des distances deja calculees...")
if nom_liste_distances in os.listdir(dossier_enreg):
	travail = pk.load(open(enreg_liste, "rb"))
	deb = repere_arret(travail)
	err = pk.load(open(enreg_err, "rb"))
else :
	travail = [0] * len(od18)
	err = [0] * len(od18)
	deb = 0

print('on commence les calculs a la ligne {} de la base.'.format(deb))

for i in range(deb, len(od18)):

	# enregistrment regulier des calculs
	if i % 100 == 0:
		print(i) # compteur pour voir l'avancee des calculs
		with open(enreg_liste, "wb") as fic:
			pk.dump(travail, fic)
		with open(enreg_err, "wb") as fic:
			pk.dump(err, fic)
		print("enregistré")
	# fin enregistrement regulier des calculs

	# requete serveur
	prob, dist, donnees = (tripdist('driving', od18['LONORIG'].iloc[i], od18['LATORIG'].iloc[i], od18['LONDEST'].iloc[i], od18['LATDEST'].iloc[i]))
	if prob == 0:
		travail[i] = dist
	else:
		travail[i] = -1
		err[i] = prob
		
	# fin requete serveur

with open(enreg_liste, "wb") as fic:
	pk.dump(travail, fic)
with open(enreg_err, "wb") as fic:
	pk.dump(err, fic)



od18['dist_calc'] = travail
od18['code_err'] = err

print("calculé\n")
#"""

##########
########## enregistrement dans le dossier
##########

if enregistre:
	print("enregistrement")
	od18.to_pickle(nom_enreg)
	print("enregistré dans", nom_enreg)
	print()
#"""




