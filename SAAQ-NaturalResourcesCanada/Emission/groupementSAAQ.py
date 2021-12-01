# information dans la case [12] des listes

import matplotlib
import matplotlib.pyplot as plt

def affiche_graphe(y):
# affiche le graphe des emissions a partir d'une liste non triee
	y.sort()
	y.reverse()
	plt.plot(y)
	plt.show()

def graphe(n, version = 2):
# Renvoie la liste non triee des emissions de GES pour l'annee n
	l = enreg(str(n) + '_(' + str(version) + ')_tri')
	y = []
	taille = len(l)
	for i in range(taille) :
		y.append(int(l[i][12]))
	return y

def graphe_hybrides(version = 1):
# pour les hybrides...
	l = enreg('hybrides_(' + str(version) + ')')
	y = []
	for lgn in l:
		y.append(int(lgn[17]))
	return y

def graphe_all(version = 2):
	res = []
	for n in range(1995, 2021):
		res = res + graphe(n, version)
	return res


