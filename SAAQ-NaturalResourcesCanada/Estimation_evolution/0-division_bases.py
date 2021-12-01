import pandas as pd
import pickle as pk
import os

##########
########## Variables
##########

fic_2017 = "../Vehicule-en-circulation-2017.csv"
fic_2018 = "../vehicules-circulation-2018.csv"


##########
########## Imports
##########





##########
########## Fonctions
##########

def divise_base(fichier, nom, destination, longueur):
# divise un fichier trop long en plusieurs plus petits pour pouvoir y travailler dessus tranquille
	ref = os.getcwd()
	fic = open(fichier, 'r')
	os.chdir(destination)
	compteur = 0
	no_fic = 0
	ecriture = open(nom + '_part' + str(no_fic) + ".csv", 'w')
	for ligne in fic:
		if compteur == 0:
			tete = ligne
		if compteur%longueur == 0 and compteur != 0:
			ecriture.close()
			print("base {} enregistree".format(compteur/longueur))
			no_fic += 1
			ecriture = open(nom + '_part' + str(no_fic) + ".csv", 'w')
			ecriture.write(tete)
		ecriture.write(ligne)
		compteur += 1
	os.chdir(ref)


##########
########## Code
##########

for i in range(2019, 2020):
	divise_base("../Vehicule-en-circulation-{}.csv".format(i), str(i), str(i), 500000)

