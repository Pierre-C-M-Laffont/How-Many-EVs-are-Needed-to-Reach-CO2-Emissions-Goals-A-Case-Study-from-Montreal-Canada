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
	res = pd.DataFrame()#{'ANNEE':[], 'MARQUE':[], 'MODELE':[], 'NB_CYL':[], 'CYLINDREE':[], 'EMISSION':[], 'GROUPES':[], 'NA':[]})
	for i in range(nb_bases):
		print(i)
		trav = pd.read_csv("{}/{}_part{}.csv".format(annee, annee, i)).rename(columns={'MARQ_VEH':'MARQUE', 'MODEL_VEH':'MODELE', 'ANNEE_MOD':"ANNEE", 'CYL_VEH':'CYLINDREE'}).query('CLAS == "PAU"')[['ANNEE', 'MARQUE', 'MODELE', 'NB_CYL', 'CYLINDREE', 'CG_FIXE']]
		trav = attribue_emiss(trav)
		trav['NA'] = trav.GROUPES.isna()
		vus += len(trav)
		non_rec += len(trav.query('NA ==True'))
		res = res.append(trav.query('NA ==True'))
		trav.to_csv("{}/{}_part{}.csv".format(annee, annee, i))
	print('{} % nn reconnus'.format(int(non_rec/vus*100000)/1000))
	return res


##########
########## Code
##########


ref = os.getcwd()
for an in range(2019, 2020):
	os.chdir(str(an))
	n = len(os.listdir())
	os.chdir(ref)
	check_annee(an, n)

#vue = test[['ANNEE', 'MARQUE', 'MODELE', 'NB_CYL', 'CYLINDREE', 'EMISSION', 'GROUPES', 'NA']]



