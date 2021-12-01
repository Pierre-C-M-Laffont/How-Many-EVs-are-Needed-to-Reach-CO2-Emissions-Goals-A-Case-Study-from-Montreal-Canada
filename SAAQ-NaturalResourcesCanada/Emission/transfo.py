# a taper dans le terminal pour executer : exec(open("transfo.py").read())

### Circulation
# CLAS = 2		TYP_VEH = 3		MARQUE = 4
# MODELE = 5		ANNEE = 6

### Emission
# MARQUE = 1		MODELE = 2


def coupage_a_5(n, version = 1):
# rogne tout a 5 pour l'annee n, version de fichier a changer au besoin
	os.chdir(doss_emiss)
	fic = open(str(n), 'rb')
	l = pk.load(fic)
	fic.close()
	for x in l:
		marque, modele = x[1], x[2]
		if len(marque) > 5:
			x[1] = marque[:5]
		if len(modele) > 5:
			x[2] = modele[:5]
	fic = open(str(n) + '_(' + str(version) + ')', 'wb')
	pk.dump(l, fic)
	fic.close()

def coupage_a_5_all(version = 1):
	for n in range(1995, 2021):
		coupage_a_5(n, version)

def majuscules(n, version = 1):
# met les marque et modele en majuscule sur tous les fichiers
	os.chdir(doss_emiss)
	fic = open(str(n) + '_(' + str(version) + ')', 'rb')
	l = pk.load(fic)
	fic.close()
	for x in l:
		x[1] = x[1].upper()
		x[2] = x[2].upper()
	fic = open(str(n) + '_(' + str(version) + ')', 'wb')
	pk.dump(l, fic)
	fic.close()

def majuscules_all(version = 1):
	for n in range(1995, 2021):
		majuscules(n, version)


########### special mazda 3
def rapport_MAZDA3(n):
# donne les MAZDA pour les emissions de l'annee n
	os.chdir(doss_emiss)
	fic = open(str(n), 'rb')
	l = pk.load(fic)
	res = []
	fic.close()
	for x in l:
		if x[1] == 'MAZDA' and x[2].startswith('MAZDA'):
			print(x[2])
			res.append(x[2])
	return res

def rapport_MAZDA3_all(nom = 'rapport_test'):
# affiche toutes les MAZDA pour etre sur qu'on remplace pas trop ou pas assez quand on ecrira le prgm
	rapport = open(nom + '.txt', 'w')
	for n in range(1995, 2021):
		print("pour l'annee ", str(n), ' : ')
		rapport.write("pour l'annee "+ str(n)+ ' : '+ '\n')
		for x in rapport_MAZDA3(n):
			rapport.write(x + '\n')
		print()
		rapport.write('\n')
	rapport.close()
###########

def rectif_mazda3(n):
# recupere le doc de l'annee n, version 1 et 2, et transforme tous les modeles commencant par mazda par la meme chose sans le prefixe mazda
	os.chdir(doss_emiss)
	fic = open(str(n), 'rb')
	init = pk.load(fic)
	fic.close()
	fic = open(str(n) + '_(1)', 'rb')
	trav = pk.load(fic)
	fic.close()
	for k in range(len(init)):
		if trav[k][2].startswith("MAZDA"):
			trav[k][2] = init[k][2][5:].upper()
	fic = open(str(n) + '_(1)', 'wb')
	pk.dump(trav, fic)
	fic.close()

def rectif_mazda3_all():
	for n in range(1995, 2021):
		rectif_mazda3(n)

########## special mazda CX...
def rapport_MAZDA_CX(n):
# donne les MAZDA CX... pour les emissions de l'annee n
	os.chdir(doss_emiss)
	fic = open(str(n) + '_(1)', 'rb')
	l = pk.load(fic)
	res = []
	fic.close()
	for x in l:
		if x[1] == 'MAZDA' and ('X - ' in x[2]):
			print(x[2])
			res.append(x[2])
	return res

def rapport_MAZDA_CX_all(nom = 'rapport_test'):
# affiche toutes les MAZDA pour etre sur qu'on remplace pas trop ou pas assez quand on ecrira le prgm
	rapport = open(nom + '.txt', 'w')
	for n in range(1995, 2021):
		print("pour l'annee ", str(n), ' : ')
		rapport.write("pour l'annee "+ str(n)+ ' : '+ '\n')
		for x in rapport_MAZDA_CX(n):
			rapport.write(x + '\n')
		print()
		rapport.write('\n')
	rapport.close()

########## Enlevement des lignes du bas
def lignes_bas(n, version_i, version_f):
# enleve toutes les lignes du bas pour l'annee n de version i, enregistre en version f
	nom_i, nom_f = str(n) + '_(' + str(version_i) +')', str(n) + '_(' + str(version_f) +')'
	l = enreg(nom_i)
	res = []
	for lgn in l:
		if lgn[0] == str(n):
			res.append(lgn)
	fic = open(nom_f, 'wb')
	pk.dump(res, fic)
	fic.close()

def lignes_bas_all(version_i, version_f):
	for n in range(1995, 2021):
		print('annee ' + str(n))
		lignes_bas(n, version_i, version_f)



####################
####################
####################
####################
####################
# Fonction de transformation principale

def duplique(fichier1, fichier2):
# copie le fichier1 dans le fichier2
	trav = enreg(fichier1)
	fic = open(fichier2, 'wb')
	pk.dump(trav, fic)
	fic.close()

def duplique_all(version):
	queue1 = '_(' + str(version) + ')'
	queue2 = '_(' + str(version+1) + ')'
	for n in range(1995, 2021):
		duplique(str(n) + queue1, str(n) + queue2)


def transfo_par_10(l_ind, l_listes, trav, historique):
# affiche toutes les lignes a changer sur la liste travail. Demande confirmation a l'usager, puis execute.
	print()
	print()
	for couple in l_listes:
		print('initial :')
		print(couple[0][:7], '...')
		print('a changer en :')
		print(couple[1][:7], '...')
		print()
	confirm = input('confirmer transformation de groupe ? (o = oui / n = non) : ')
	if confirm == 'o':
		for j in range(len(l_ind)):
			trav[l_ind[j]] = l_listes[j][1]
			historique.write(str(l_listes[j][0]) + '\n')
			historique.write('-> ' + str(l_listes[j][1]) + '\n\n')
	else:
		for j in range(len(l_listes)):
			print()
			print()
			print('initial :')
			print(l_listes[j][0][:7], '...')
			print('a changer en :')
			print(l_listes[j][1][:7], '...')
			print()
			confirm = input('confirmer transformation de ligne ? (o = oui / n = non) : ')
			if confirm == 'o':
				trav[l_ind[j]] = l_listes[j][1]
				historique.write(str(l_listes[j][0]) + '\n')
				historique.write('-> ' + str(l_listes[j][1]) + '\n\n')


def a_changer(lgn, recherche, colonnes):
# renvoie si on doit ou non modifier la ligne selon les deux listes recherche et colonnes. Envoie aussi la position du resultat dans les listes precedentes
	i = 0
	ok = False
	fin = len(recherche)
	while i < fin and not ok:
		if lgn[colonnes[i]] == (recherche[i]):
			ok = True
		else :
			i += 1
	if ok:
		return ok, i
	else:
		return ok, -1

def transfo_intermediaire(lgn, colonne, remplac):
# renvoie la meme liste que celle donnee, mais avec la chaine remplac dans la colonne donnee
	l2 = [elt for elt in lgn]
	l2[colonne] = remplac
	return l2


def transfo_en_masse(recherche, colonnes, remplacement, annee, version, historique):
# cherche dans la base annee toutes les lignes avec l'attribut colonne exactement egal a recherche, demande une confirmation de transformation, et enrgeistre dans une nouvelle version.
	trav = enreg(str(annee) + '_(' + str(version) + ')')
	indices = []
	a_afficher = []
	i = 0
	for lgn in trav:
		ajout, indice_listes = a_changer(lgn, recherche, colonnes)
		if ajout:
			indices.append(i)
			a_afficher.append((lgn, transfo_intermediaire(lgn, colonnes[indice_listes], remplacement[indice_listes])))
		i += 1
	j = 0
	fin = len(indices)
	while j < fin :
		if j + 10 >= fin :
			transfo_par_10(indices[j:], a_afficher[j:], trav, historique)
		else:
			transfo_par_10(indices[j:j+10], a_afficher[j:j+10], trav, historique)
		j += 10
	fic = open(str(annee) + '_(' + str(version) + ')', 'wb')
	pk.dump(trav, fic)
	fic.close()

def transfo_en_masse_all(recherche, colonnes, remplacement, version, nom_fichier_historique):
# enregistre le fichier d'historique dans le dossier correspondant
	os.chdir(doss_historique_transfos)
	if nom_fichier_historique in os.listdir():
		print('nom de fichier deja utilise')
	else:
		fic = open(nom_fichier_historique, 'w')
		fic.write('appel de la fonction : \ntransfo_en_masse_all\n\narguments :\nrecherche : ' + str(recherche) + '\ncolonnes : ' + str(colonnes) +'\nremplacement : ' + str(remplacement) + '\nversion : ' + str(version) + '\n\n\n')
		os.chdir(doss_emiss)
		for n in range(1995, 2021):
			print('annee ', n)
			fic.write('\nAnnee ' + str(n) + ' : \n\n')
			print()
			transfo_en_masse(recherche, colonnes, remplacement, n, version, fic)
			print()
			print()
		os.chdir(doss_historique_transfos)
		fic.close()
		os.chdir(doss_emiss)



def transfo_en_masse_hybridelec(recherche, colonnes, remplacement, version, nom_fichier_historique):
	os.chdir(doss_historique_transfos)
	if nom_fichier_historique in os.listdir():
		print('nom de fichier deja utilise')
	else:
		fic = open(nom_fichier_historique, 'w')
		fic.write('appel de la fonction : \ntransfo_en_masse_hybridelec\n\narguments :\nrecherche : ' + str(recherche) + '\ncolonnes : ' + str(colonnes) +'\nremplacement : ' + str(remplacement) + '\nversion : ' + str(version) + '\n\n\n')
		os.chdir(doss_emiss)
		for n in ['hybrides', 'elec']:
			print(n)
			fic.write( str(n) + ' : \n\n')
			print()
			transfo_en_masse(recherche, colonnes, remplacement, n, version, fic)
			print()
			print()
		os.chdir(doss_historique_transfos)
		fic.close()
		os.chdir(doss_emiss)


##########################
##########################
##########################
##########################
# Regroupement en un seul modele

def modeles_a_matcher(m1, m2):
# dit si deux modeles doivent etre matches ensemble
	return m1[0] == m2[0] and m1[1] == m2[1] and m1[2] == m2[2] and m1[5] == m2[5] and m1[4] == m2[4]

def enreg_moyenne(temp, res):
# enregistre dans la liste res la moyenne des modeles de temp
	for lgn in temp :
		print(str(lgn[:7]) + '  ' +str(lgn[12]))
	print()
	ok = 'o' #input('moyenner ? (o = oui, n = non)  ')
	if ok == 'o':
		l = []
		for i in [0, 1, 2, 5, 4]:
			l.append(temp[0][i])
		moy = 0
		for lgn in temp :
			moy += float(lgn[12])
		l.append(moy/len(temp))
		res.append(l)
#		print('enregistré\n\n')
	return ok == 'o'


def regroupement_modeles(nom, version_d, version_f):
# regroupe les modeles de la base nom (version d) et les enregistre dans la base nom (version f)
# on ne garde que les 
	nom_d = str(nom) + '_(' + str(version_d) + ')'
	nom_f = str(nom) + '_(' + str(version_f) + ')'
	fic = enreg(nom_d)
	observe = fic[0] # le modele auquel on compare
	ind = 1
	fin = len(fic)
	temp = [observe] # tous les modeles qui correspondent
	res = [] # le truc qu'on va enregistrer a la fin
	arret = False
	while ind < fin and not arret:
		if modeles_a_matcher(fic[ind], observe) :
			temp.append(fic[ind])
		else :
			if not enreg_moyenne(temp, res) :
				arret = True
			observe = fic[ind]
			temp = [observe]
		ind +=1
	if not arret :
		n_fic = open(nom_f, 'wb')
		pk.dump(res, n_fic)
		n_fic.close()
		print('enregistré dans ' + nom_f)
	else :
		print('non enregistré')


def regroupement_modeles_all(version_d, version_f):
	for n in range(1995, 2021):
		print('\n\nEtude de ' + str(n) + '\n')
		regroupement_modeles(n, version_d, version_f)
	print('termine')


#######################
#######################
def base_unique(nom):
# regroupe toutes les bases en une seule
	fic = open(nom, 'wb')
	res = []
	for n in range(1995, 2021):
		trav = enreg(str(n) + '_(6)')
		for lgn in trav:
			res.append(lgn)
	pk.dump(res, fic)
	fic.close()

