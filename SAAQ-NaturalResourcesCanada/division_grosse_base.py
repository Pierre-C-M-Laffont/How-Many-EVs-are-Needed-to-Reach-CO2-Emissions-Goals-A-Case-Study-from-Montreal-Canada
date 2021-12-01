# a taper dans le terminal pour executer : exec(open("division_grosse_base.py").read())


import os
dossier_initial = os.getcwd()


def divise_base(fichier, nom, destination, longueur):
# divise un fichier trop long en plusieurs plus petits pour pouvoir y travailler dessus tranquille
	fic = open(fichier, 'r')
	os.chdir(dossier_initial + destination)
	compteur = 0
	no_fic = 0
	ecriture = open(nom + '_part' + str(no_fic) + ".csv", 'w')
	for ligne in fic:
		if compteur%longueur == 0 and compteur != 0:
			ecriture.close()
			no_fic += 1
			ecriture = open(nom + '_part' + str(no_fic) + ".csv", 'w')
		ecriture.write(ligne)
		compteur += 1
