import pandas as pd



### Nom des varaibles

nom_a_importer = "outs/od18_multi.pkl"

#1 conduc, 2 passager, 11 taxi, 12 moto, 13 velo, 14 pied, 18 indetermine
#ens_ok = {'1', '2', '11', '12'}

ens_ok = {"['2']","['1']","['11', '1']", "['1', '2']", "['11', '2']", "['11']", "['2', '2']", "['1', '11']", "['2', '1']", "['2', '11']", "['2', '1', '2']"}



### import des bases
print("import des bases")
od18 = pd.read_pickle(nom_a_importer)
print("importé\n")



### Fonctions utiles

def sousseq(seq):
	# coupe la liste de base selon les '17'
	res = []
	travail = seq
	while '17' in travail:
		i = travail.index('17')
		res.append(travail[:i])
		travail = travail[i+1:]
	res.append(travail)
	return res

def filtre_sousseq(sousseq):
	# selectionne les sous-listes qui correspondent a ce qu'on veut prendre en compte
	i = 0
	res = []
	inds = []
	for l in sousseq:
		if str(l) in ens_ok:
			res.append(l)
			inds.append(i)
		i += 1
	return res, inds
	




### debut des tests
print("debut des tests\n")


print(od18)


res = dict()
res2 = dict()
c = 0
for i in range(len(od18)):
	l = od18.LISTE_SEQ.iloc[i]
	l2 = sousseq(l)
	_, inds = filtre_sousseq(l2)
	for i in range(len(l2)):
		c += 1
		x = str(l2[i])
		if i in inds:
			if x not in res.keys():
				res[x] = 1
			else:
				res[x] += 1
		else:
			if x not in res2.keys():
				res2[x]  = 1
			else:
				res2[x]  += 1

print("total sections : ", c)
print("reconnu comme bon")
for x in res.keys():
	if True:#res[x] > 30:
		print(x, res[x])
print("\nReconnu comme mauvais")
for x in res2.keys():
	if True:#res2[x] > 30:
		print(x, res2[x])
	



