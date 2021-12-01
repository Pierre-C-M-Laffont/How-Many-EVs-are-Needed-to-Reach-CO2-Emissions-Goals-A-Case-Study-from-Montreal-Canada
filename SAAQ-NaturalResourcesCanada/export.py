import pandas as pd

exec(open('outils.py').read())

#colonnes_init = [﻿"AN", "NOSEQ_VEH", "CLAS", "TYP_VEH_CATEG_USA", "MARQ_VEH", "MODEL_VEH", "ANNEE_MOD", "MASSE_NETTE", "NB_CYL", "CYL_VEH", "NB_ESIEU_MAX", "COUL_ORIG", "TYP_DOSS_PERS", "PHYS_SEX", "PHYS_AGE", "REG_ADM", "MRC"," CG_FIXE"]#, "THERMIQUE", "HYB", "ELEC", 'EMISSION']
colonnes_init = ['AN', 'NOSEQ_VEH', 'CLAS', 'TYP_VEH_...', 'MARQUE', 'MODELE', 'ANNEE', 'MASSE', 'NB_CYL', 'CYLINDREE', 'ESIEU', 'COUL', 'TYP_DOSS', 'SEX', 'AGE', 'REG_ADM', 'MRC', 'CG_FIXE', "THERMIQUE", "HYB", "ELEC", 'EMISSION']

colonnes_voulues = ['ANNEE', 'MARQUE', 'MODELE', 'NB_CYL', 'CYLINDREE', 'EMISSION']

chemin_fin = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python'

def est_dans(memo, ligne):
# retourne True si la ligne est dans la liste memo
	ok = False
	i = 0
	fin = len(memo)
	while not ok and i < fin:
		ok = ligne == memo[i]
		i +=1
	return ok


def cree_csv(nom = '/vehicules_et_emissions.csv'):
# retourne le csv avec les colonnes voulues
	os.chdir(doss_circul)
	res = []
	for n in range(133):
		print('base ', n)
		liste = enreg('PAU' + str(n))
		for lgn in liste:
			test = [lgn[i] for i in [6, 4, 5, 8, 9, 21]]
			if not est_dans(res, test):
				res.append(test)
				print('longueur : ', len(res))
	data = pd.DataFrame(res, columns=colonnes_voulues)
	data.to_csv(path_or_buf=chemin_fin + nom, index=False)

"""
def ecrit_csv_txt():
# avec des docs txt et des write
	os.chdir('/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python')
	fic = open('vehicules_et_emissions.csv', 'w')
	for mot in colonnes_voulues:
		fic.write(mot + ',')
	fic.write('\n')
	os.chdir(doss_circul)
	cpt = 0
	for n in range(13):
		print(n)
		trav = enreg('PAU' + str(n))
		for lgn in trav:
			for i in [6, 4, 5, 8, 9, 21]:
				fic.write(str(lgn[i]) + ',')
			fic.write('\n')
			cpt += 1
	fic.close()
	print(cpt, ' lignes ecrites')"""

#cree_csv()


def parcourt_liste(frontieres, emission):
# donne le groupe auquel le vehicule appartient
	i = 0
	fin = len(frontieres)
	while i < fin and float(emission) > frontieres[i]:
		i +=1
	return i


def csv_groupes(nb_groupes, zeros):
# enregistre les groupes dans un fichier (on ajoute juste une colonne pour les groupes)
# si on n'a pas zeros dans les groupes (donc un groupe est dedie aux veh elec), il faut ajouter un groupes avec les emiss 0 DONC on prend un groupe en moins
	d = pd.read_csv('vehicules_et_emissions.csv')
	groupes = []
	nb = nb_groupes
	if not zeros:
		nb -= 1
		num = str(nb) + '(-0)'
	else:
		num = str(nb)
	os.chdir(sep)
	l = enreg('frontieres-' + num)
	for i in range(len(d)):
		if not zeros:
			if d['EMISSION'][i] == 0:
				groupes.append(0)
			else:
				groupes.append(parcourt_liste(l, d['EMISSION'][i]) + 1)
		else:
			groupes.append(parcourt_liste(l, d['EMISSION'][i]))
	d['GROUPES'] = groupes
	nom = 'vehicules_et_emissions_2018_' + str(nb_groupes) + 'gr'
	if not zeros:
		nom += '_dont_elec'
	nom += '.csv'
	os.chdir(chemin_fin)
	d.to_csv(nom, index = False)









