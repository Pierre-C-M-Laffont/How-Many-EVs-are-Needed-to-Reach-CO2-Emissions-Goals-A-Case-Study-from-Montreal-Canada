import pandas as pd
import os


##########
########## Variables
##########

dossier_SAAQ = "../../Travail et modif des bases/Python/estimation_evolution/"
fic_mun = "municipalites_od.csv"

##########
########## Imports
##########

mun = pd.read_csv(fic_mun)[["MUS_CO_GEO", "MUS_NM_MUN"]].rename(columns={"MUS_CO_GEO":'CG_FIXE'})

##########
########## Fonctions
##########

def compte_groupes_an(an):
	# donne le nb de vehicules de chaque groupe pour une annee donnee
	cpt = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	veh = 0
	n = len(os.listdir(dossier_SAAQ + str(an)))
	for i in range(n):
		nom = dossier_SAAQ + '{}/{}_part{}.csv'.format(an, an, i)
		trav = pd.read_csv(nom).query('NA != True')
		print(len(trav))
		trav['NA'] = trav.CG_FIXE.isna()
		trav = trav.query('NA != True')
		print(len(trav))
		trav['CG_FIXE'] = trav.CG_FIXE.astype(int)
		trav = trav.merge(mun)
		veh += len(trav)
		for j in range(len(trav)):
			cpt[trav.GROUPES.iloc[j]] += 1
		print()
	print(veh)
	print(sum([cpt[d] for d in cpt.keys()]))
	print(cpt)
	return cpt

def stats_mun_nulle(an):
	# donne des stats sur les veh dont la municipalite n'est pas renseignee
	veh_tot = 0
	veh_na = 0
	n = len(os.listdir(dossier_SAAQ + str(an)))
	for i in range(n):
		nom = dossier_SAAQ + '{}/{}_part{}.csv'.format(an, an, i)
		trav = pd.read_csv(nom).query('NA != True')
		veh_tot += len(trav)
		trav['NA'] = trav.CG_FIXE.isna()
		trav = trav.query('NA == True')
		veh_na += len(trav)
	print(an)
	print(veh_na/veh_tot)
	print()



def progression():
	# pour toutes les annees donne le nb de vehicules au format dataframe (index : annee, puis 1 colonne par groupe)
	dico = {"an":[i for i in range(2019, 2020)]}
	for i in range(10):
		dico["gr{}".format(i)] = []
	for an in range(2019, 2020):
		d = compte_groupes_an(an)
		for i in range(10):
			dico['gr{}'.format(i)].append(d[i])
	return pd.DataFrame(dico)


##########
########## Code
##########

fin = progression().set_index("an")
fin.to_csv("groupes_SAAQ_2019.csv")


