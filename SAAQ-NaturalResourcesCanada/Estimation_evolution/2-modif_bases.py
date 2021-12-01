import pandas as pd


##########
########## Variables
##########



##########
########## Imports
##########



##########
########## Fonctions
##########

def change(annee, filtre, colonne, remplac, nb_bases):
	# dans les bases donnees, flitre selon un truc précis
	changes = 0
	for i in range(nb_bases):
		print(i)
		trav = pd.read_csv("{}/{}_part{}.csv".format(annee, annee, i)).rename(columns={'MARQ_VEH':'MARQUE', 'MODEL_VEH':'MODELE', 'ANNEE_MOD':"ANNEE", 'CYL_VEH':'CYLINDREE'}).query('CLAS == "PAU"')
		changes += len(trav[eval(filtre)])
		trav.loc[eval(filtre), colonne] = remplac
		#trav.to_csv("{}/{}_part{}.csv".format(annee, annee, i))
	print(changes, 'vehicules changes')


##########
########## Code
##########

change(2018, "(trav['MARQUE'] == 'MAZDA') & (trav['MODELE'] == 'CX5')", 'MODELE', 'CX-5', 14)


