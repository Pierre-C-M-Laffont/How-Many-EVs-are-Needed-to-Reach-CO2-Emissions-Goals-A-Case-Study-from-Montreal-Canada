import os
import pickle as pk
from matplotlib import pyplot as plt

doss_circul = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/circulation_divisee'

doss_veh = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/circulation_divisee/Vehicules'

doss_emiss = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/emission'

doss_historique_transfos = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/emission/Historique_transfo'

sep = '/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/Separateurs'


def affiche(nom, colonnes, nb_lignes = -1):
# ouvre le fichier binaire 'nom' et affiche les colonnes renseignees
	trav = enreg(nom)
	taille = len(trav)
	j = 0
	while j < taille and j != nb_lignes - 1:
		aff = []
		for i in colonnes:
			aff.append(trav[j][i])
		print(aff)
		j += 1


def enreg(nom):
# retourne la liste venant du fichier nomme
	fic = open(nom, 'rb')
	l = pk.load(fic)
	fic.close()
	return l

def run(nom):
# execute le script de nom donne
	fic = open(nom, 'r')
	exec(fic.read())
	fic.close()
