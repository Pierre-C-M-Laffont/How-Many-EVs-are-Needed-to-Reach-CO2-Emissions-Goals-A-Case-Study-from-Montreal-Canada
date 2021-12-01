import random as rd
import numpy as np
from mpl_toolkits import mplot3d


"""
V = [rd.randint(0, 50) for i in range(200)]

V.sort()

print('debut de la liste triee... ')
print(V[:20])

m1 = np.array([i/10 for i in range(500)])
m2 = np.array([i/10 for i in range(500)])

m13d = np.outer(m1, np.ones(500))
m23d = np.outer(np.ones(500), m2)

grille = np.array([[0. for j in range(500)] for i in range(500)])


for i1 in range(500):
	print(i1)
	for i2 in range(500):
		somme = 0
		for i in range(len(V)):
			d1 = (V[i] - m1[i1])**2
			d2 = (V[i] - m2[i2])**2
			somme += min(d1, d2)
		grille[i1][i2] = somme



#plt.plot(kint, resuint, '.')
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(m13d, m23d, grille)
#plt.plot(k[1:], derresu)

plt.axis([10, 40, 10600, 12000])
plt.axhline(y=0, xmin=0, xmax=50)
for n in range(50):
	plt.axvline(x=n, ymin=-25, ymax=25)
plt.show()"""


"""
 pour un k-means type:
 assigner les mi au hasard
 associer les points correspondants pour creer les clusters
 calculer le milieu des clusters
 recommencer

donner le nb de pts / la liste des points + nb de representants
liste pour les placements des points
liste pour les points de chaque cluster (meme type que la liste de depart)
"""

def calcul_des_distances(val_un, trav):
# actualise les distances des valeurs (rattache au cluster dont le centre est le plus proche)
	cluster = 0
	nb_cl = len(trav)
	for v in val_un:
		if cluster + 1 != nb_cl and abs(v[0] - trav[cluster]) > abs(v[0] - trav[cluster + 1]):
			cluster += 1
		v[2] = cluster


def nouveau_placement(i, val_un):
# donne le nouveau centre de gravité du cluster i selon les valeurs donnees (on prend dans val_un seulement les pts rattaches au cluster donne
	somme = 0
	nb_elts = 0
	for v in val_un:
		if v[2] == i:
			somme += v[0] * v[1]
			nb_elts += v[1]
	if nb_elts == 0:
		print('cluster ', i, ' vide')
		return False, 0.0
	else:
		return True, somme/nb_elts


def condition_darret(liste_placements):
# tout est dans le nom de la fonction...
	dep_max = 0
	for i in range(len(liste_placements[0])):
		dep_max = max(dep_max, abs(liste_placements[-1][i] - liste_placements[-2][i]))
	return dep_max < 0.0001

def liste_vals_uniques(V):
# renvoie la liste des valeurs uniques, puis le nb d'occurences...
	val_un = []
	for v in V:
		if val_un != [] and v == val_un[-1][0]:
			val_un[-1][1] += 1
		else:
			val_un.append([v, 1, 0]) # valeur, nombre d'occurences dans la liste, cluster d'attache
	return val_un
	

def cluster(val_un, n, placement_init = []):
# creee les n clusters correspondants a la liste V, V la liste des vals uniques triee
	maxv = 0
	for v in val_un:
		maxv = max(maxv, v[1])
	mini = val_un[0][0]
	maxi = val_un[-1][0]
	nb_iterations_max = 2000
	pas = (maxi - mini) / n
	if placement_init != []:
		placement_pts_fin = [placement_init]
	else:
		placement_pts_fin = [[mini + (i+1) * pas for i in range(n)]] # les centres sont ranges dans l'ordre croissant
#	print('placement_initial :')
#	print(placement_pts_fin[0])
#	for v in val_un:
#		plt.plot([v[0]]*2, [0, v[1]])
#	plt.plot([val_un[i][0] for i in range(len(val_un))], [val_un[j][1] for j in range(len(val_un))])

	j = 0
	while j < nb_iterations_max and (j < 3 or not condition_darret(placement_pts_fin)): # la c'est le nb de fois ou on va repeter l'algo
		
#		print('iteration ', j)
		travail = [x for x in placement_pts_fin[-1]]
		placement_pts_fin.append(travail)
		calcul_des_distances(val_un, travail)
		for i in range(n):
			ok, val = nouveau_placement(i, val_un)
			if ok:
				placement_pts_fin[-1][i] = val
		j += 1
#	for i in range(len(placement_pts_fin)):
#		plt.plot(placement_pts_fin[i], [i* maxv / len(placement_pts_fin)] * n, 'b.')
#	print('placement_final')
#	print(placement_pts_fin[-1])
#	plt.show()
	return placement_pts_fin


def erreur_tot(liste, placements):
# renvoie la somme des erreurs au carre
	somme = 0
	for v in liste:
		somme += (v[0] - placements[v[2]])**2 * v[1]
	return somme


def clusters_en_boucle(repet, val_un, n, zeros):
# fait tourner la fonction cluster avec val_un, n et une repartition aleatoire un nombre de fois donne (repet)
# si zeros, on prend en compte les elec dans le calcul
	mini = val_un[0][0]
	maxi = val_un[-1][0]
	placement_dep = [mini + rd.random() * (maxi - mini) for i in range(n)]
	placement_dep.sort()
	meilleur_resu = cluster(val_un, n, placement_init = placement_dep)
	meilleure_err = erreur_tot(val_un, meilleur_resu[-1])
	for i in range(repet):
		placement_dep = [mini + rd.random() * (maxi - mini) for i in range(n)]
		placement_dep.sort()
		resu_cl = cluster(val_un, n, placement_init = placement_dep)
		err = erreur_tot(val_un, resu_cl[-1])
		print(err)
		if err < meilleure_err:
			meilleur_resu, meilleure_err = resu_cl, err
	print('meilleure erreur :')
	print(meilleure_err)
	os.chdir(sep)
	nom = str(n)
	if not zeros:
		nom = nom + "(-0)"
	print(nom)
	if nom in os.listdir():
		memo = enreg(str(n))
		if memo[0] > meilleure_err:
			fic = open(nom, 'wb')
			pk.dump([meilleure_err, meilleur_resu], fic)
			fic.close()
			txt = open(nom + '.txt', 'w')
			txt.write('meilleurs separateurs actuels :\n')
			for x in meilleur_resu[-1]:
				txt.write(str(x) + '\n')
			txt.close()
	else:
		fic = open(nom, 'wb')
		pk.dump([meilleure_err, meilleur_resu], fic)
		fic.close()
		txt = open(nom + '.txt', 'w')
		txt.write('meilleurs separateurs actuels :\n')
		for x in meilleur_resu[-1]:
			txt.write(str(x) + '\n')
		txt.close()


def liste_des_emissions_un(zeros):
# renvoie la liste des emissions de notre dossier PAU, si zeros, on prend en compte les elec dans le calcul
	chemin = os.getcwd()
	os.chdir(doss_circul)
	res = []
	for n in range(133):
		print(n)
		fic = enreg('PAU' + str(n))
		for x in fic:
			if zeros or x[21] != 0:
				res.append(x[21])
	res.sort()
	os.chdir(chemin)
	return liste_vals_uniques(res)

def frontieres(n, zeros):
# recupere dans le dossier le fichier avec le resultat optimal et donne les frontieres correspondantes
		nom = str(n)
		if not zeros:
			nom = nom + '(-0)'
		trav = enreg(nom)
		pts = trav[1][-1]
		sep = [0 for i in range(len(pts)-1)]
		for i in range(len(sep)):
			sep[i] = (pts[i] + pts[i+1])/2
#		plt.plot(sep, [0 for i in range(len(sep))], 'b.')
#		plt.plot(pts, [0 for i in range(len(pts))], 'r.')
#		plt.show()
		fic = open('frontieres-' + nom, 'wb')
		pk.dump(sep, fic)
		fic.close()
		fic2 = open('frontieres-' + nom + '.txt', 'w')
		for frontiere in sep:
			fic2.write(str(frontiere) + '\n')
		fic2.close()



