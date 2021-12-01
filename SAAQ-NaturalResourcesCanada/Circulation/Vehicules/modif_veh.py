########################
########################
########################
# tri de la base

def inferieur(lgn1, lgn2):
# indique si la lgn 1 doit etre placee avant la lgn 2 dans une liste triee
	if lgn1[0] < lgn2[0]:
		return True
	elif lgn1[0] > lgn2[0]:
		return False
	elif lgn1[1] < lgn2[1]:
		return True
	elif lgn1[1] > lgn2[1]:
		return False
	else:
		return lgn1[2] < lgn2[2]

def recolle(l1, l2):
# recolle deux listes triees en une seule triee
	res = []
	cpt1 = 0
	cpt2 = 0
	long1 = len(l1)
	long2 = len(l2)
	while cpt1 < long1 or cpt2 < long2:
		if cpt1 == long1:
			res.append(l2[cpt2])
			cpt2 += 1
		elif cpt2 == long2:
			res.append(l1[cpt1])
			cpt1 += 1
		elif inferieur(l1[cpt1],l2[cpt2]):
			res.append(l1[cpt1])
			cpt1 += 1
		else:
			res.append(l2[cpt2])
			cpt2 += 1
	return res

def tri_log(liste):
# tri par la methode divise pour mieux regner
	l = len(liste)
	if l <= 1:
		return liste
	else :
		l1, l2 = liste[:l//2], liste[l//2:]
		return recolle(tri_log(l1), tri_log(l2))

def rearrange():
# trie le fichier donne
	fic = open('liste_veh_brute', 'rb')
	liste = pk.load(fic)
	fic.close()
	liste2 = tri_log(liste)
	fic = open('liste_veh_tri', 'wb')
	pk.dump(liste2, fic)
	fic.close()



########################
########################
########################
# base sans annee

def base_sans_annee():
# cree un nouveau fichier (trie) des modeles sans prendre en compte l'annee
	fic = enreg('liste_veh_brute')
	res = []
	for lgn in fic:
		ajout = lgn[1:]
		if not ajout in res:
			res.append(ajout)
	res_tri = tri_log(res)
	return res_tri



########################
########################
########################

def insere(lgn, res):
# ajoute le compteur pour l'annee donnee, ou joute une nouvelle liste a res
	i = 0
	fin = len(res)
	ok = False
	while not ok and i < fin:
		if lgn[0][1:] == res[i][0]:
			ok = True
			res[i][1] += lgn[1]
		else:
			i += 1
	if not ok:
		res.append([lgn[0][1:], lgn[1]])


def compteurs_sans_annee():
# transforme la base compteurs en base sans annee, on la trie pas pour l'instant
	fic = enreg('liste_veh_brute_avec_compteurs')
	res = []
	for lgn in fic:
		insere(lgn, res)
	return res
