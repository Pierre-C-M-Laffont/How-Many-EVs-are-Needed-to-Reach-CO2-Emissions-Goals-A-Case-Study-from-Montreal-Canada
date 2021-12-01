# fonctions pour trier les docs (par année > marque > modele)

### Emission
# ANNEE = 0		MARQUE = 1		MODELE = 2


def inf_adapte(chaine1, chaine2):
# pour 2 chaines de carac. rpztant des float (possiblement vides) dit si la 1 est strictement plus petite que la 2. La chaine vide est la plus petite
	if chaine1 == '':
		c1 = -1.0
	else:
		c1 = float(chaine1)
	if chaine2 == '':
		c2 = -1.0
	else:
		c2 = float(chaine2)
	return c1 < c2


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
	elif lgn1[2] < lgn2[2]:
		return True
	elif lgn1[2] > lgn2[2]:
		return False
	elif inf_adapte(lgn1[3], lgn2[3]):
		return True
	elif inf_adapte(lgn2[3], lgn1[3]):
		return False
	else:
		return inf_adapte(lgn1[4], lgn2[4])


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

def rearrange(fichier):
# trie le fichier donne
	fic = open(fichier, 'rb')
	liste = pk.load(fic)
	fic.close()
	liste2 = tri_log(liste)
	fic = open(fichier, 'wb')
	pk.dump(liste2, fic)
	fic.close()

def rearrange_all():
# trie tous les fichiers
	for i in range(1995, 2021):
		rearrange(str(i) + '_(5)')
		print(i)

