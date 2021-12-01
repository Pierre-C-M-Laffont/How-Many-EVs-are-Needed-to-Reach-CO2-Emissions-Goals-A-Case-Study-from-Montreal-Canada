import pandas as pd
import os


##########
########## Variables
##########
fic_emiss = "../vehicules_et_emissions_2018_10gr_dont_elec.csv"

##########
########## Imports
##########

groupes = pd.read_csv(fic_emiss)


##########
########## Fonctions
##########

def attribue_emiss(df):
	# pour la base donnee (deja un dataframe), essaie de retrouver les corresp des vehicules et leur groupe associe
	trav = df.merge(groupes, how = 'left')
	return trav

def check_annee(annee, nb_bases):
	# compte sur le nb de veh d'une annee la proportion qui est pas reconnue
	vus = 0
	non_rec = 0
	elec, hyb = 0, 0
	res = pd.DataFrame()#{'ANNEE':[], 'MARQUE':[], 'MODELE':[], 'NB_CYL':[], 'CYLINDREE':[], 'EMISSION':[], 'GROUPES':[], 'NA':[]})
	for i in range(nb_bases):
		print(i)
		trav = pd.read_csv("{}/{}_part{}.csv".format(annee, annee, i))
		#trav = attribue_emiss(trav)
		#trav['NA'] = trav.GROUPES.isna()
		vus += len(trav)
		non_rec += len(trav.query('NA ==True'))
		res = res.append(trav.query('NA ==True'))
		elec += len(trav.query('GROUPES == 0'))
		hyb += len(trav.query('GROUPES == 1'))
		#trav.to_csv("{}/{}_part{}.csv".format(annee, annee, i))
	print('{} elec et {} hyb='.format(elec, hyb))
	return elec, hyb


##########
########## Code
##########
"""
e = []
h = []

ref = os.getcwd()
for an in range(2011, 2019):
	os.chdir(str(an))
	n = len(os.listdir())
	os.chdir(ref)
	en, hn = check_annee(an, n)
	e.append(en)
	h.append(hn)

pd.DataFrame({"an":[i for i in range(2011, 2019)], "elec":e, "hyb":h}).to_csv("resu_test.csv")

#vue = test[['ANNEE', 'MARQUE', 'MODELE', 'NB_CYL', 'CYLINDREE', 'EMISSION', 'GROUPES', 'NA']]

#"""


##########
########## 
##########


def divise_base(fichier):
# divise un fichier trop long en plusieurs plus petits pour pouvoir y travailler dessus tranquille
	fic = open(fichier, 'r')
	compteur = 0
	for ligne in fic:
		if True:#ligne[:4] == '2018' or ligne[:4] == 2018:
			compteur += 1
	return compteur

cpt = 0
os.chdir("2018")
for i in range(14):
	cpt += divise_base("2018_part{}.csv".format(i)) -1

print(cpt)





