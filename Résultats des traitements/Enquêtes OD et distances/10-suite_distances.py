"""
Renvoie la base de donnees AD avec les emissions associees

Mode operatoire :
	remplissage des taux d'occupation dans les voitures manquants
	Distance * facteur_menage / occupation -> distance reelle
	somme de la distance reelle sur les aires de diffusion

Ajoute une colonne avec le nombre d'habitants par AD aussi

"""

print("import biblios...")
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
print("importé\n")

##########
########## Variables utilisees
##########


dossier = "outs_V2/"
nom_od = "calculé_od18_completV4_SM.pkl"

nom_habitants = "donnees_geo/hab_AD.pkl"

enreg = True
nom_enreg = "calculé_od18_complet_AD.pkl"




##########
########## Import bases de travail
##########

print("import OD")
od18 = pd.read_pickle(dossier + nom_od)
print("importé, longueur : {}\n".format(len(od18)))

# apres ca on a perdu les lignes avec erreurs
od18 = od18.query('code_err == 0')

print("sans les erreurs : {}\n".format(len(od18)))

occupation_conduc = od18.query("PERS_AUTO != 0").PERS_AUTO.mean()
print("occupation_conduc : {}".format(occupation_conduc))
occupation_passager = occupation_conduc
print("occupation_passager : {}\n".format(occupation_passager))

print("import habitants...")
hab = pd.read_pickle(nom_habitants).rename(columns={"AD":"ADIDU"})
print('importé\n')

##########
########## Fonctions
##########

def remplace_occupation(occ, mode):
	if occ == 0:
		if mode == "1":
			return occupation_conduc
		elif mode == "2":
			return occupation_passager
		else :
			return occupation_conduc
	else:
		return occ


def distance_reelle(dist, fac, occ):
	if dist < 0:
		print('dist nulle')
		return 0
	else:
		return dist * fac / occ /1000 # passage de m à km



def base_personnes(data):
	# renvoie le nombre de personnes par aire de diff de la base donnee en argument

	# comptage des personnes
	d = {}
	for feu, df in data.groupby(["FEUILLET"]):
		if df.ADIDU.iloc[0] in d.keys():
			d[df.ADIDU.iloc[0]] += df.PERSLOGI.iloc[0] * df.FACLOG.iloc[0] # seulement la premiere ligne
		else:
			d[df.ADIDU.iloc[0]] = df.PERSLOGI.iloc[0] * df.FACLOG.iloc[0]
			
	# mise en forme pour un dataframe
	d2 = {"AD":[], "nb_pers":[]}
	for k in d.keys():
		d2["AD"].append(k)
		d2["nb_pers"].append(d[k])
	pers_par_aire = pd.DataFrame(d2)
	return pers_par_aire



##########
########## remplacement par les valeurs par defaut
##########

print("remplacement occupation...")
od18['PERS_AUTO'] = od18.apply(lambda x: remplace_occupation(x['PERS_AUTO'], x['SEQ_MODES']), axis=1)
print("fait\n")

print("calcul distance totale...")
od18["dist_tot"] = od18.apply(lambda x: distance_reelle(x['dist_calc'], x['FACLOG'], x['PERS_AUTO']), axis=1)
print("fait\n")

print('groupement par aire de diffusion...')
resultat = od18.groupby('ADIDU')["dist_tot"].sum().reset_index()
print("groupé\n")

print(resultat.head(20))

resultat = resultat.merge(hab)

print(resultat.head(20))

##########
########## enregistrement
##########

if enreg :
	print("enregistrement")
	resultat.to_pickle(dossier + nom_enreg)
	print("enregistré sous " + dossier + nom_enreg)








