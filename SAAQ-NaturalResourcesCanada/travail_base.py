# a taper dans le terminal pour executer : exec(open("travail_base.py").read())


# 1° lgn circul : "AN","NOSEQ_VEH","CLAS","TYP_VEH_CATEG_USA","MARQ_VEH","MODEL_VEH",
# "ANNEE_MOD","MASSE_NETTE","NB_CYL","CYL_VEH","NB_ESIEU_MAX","COUL_ORIG",
# "TYP_DOSS_PERS","PHYS_SEX","PHYS_AGE","REG_ADM","MRC","CG_FIXE"

# 1° lgn emiss :
# ['ANN�E', 'MARQUE', 'MOD�LE', 'CAT�GORIE DE', 'CYLINDR�E', 'CYLINDRES', 'TRANSMISSION', 'TYPE DE', 'CONSOMMATION DE CARBURANT*', '', '', '', '�MISSIONS DE CO2', '', '', '', '\n']

# 2° lgn emiss :
# ['MOD�LE', '', '', 'V�HICULE', '(L)', '', '', 'CARBURANT', 'VILLE (L/100 km)', 'ROUTE (L/100 km)', 'COMB (L/100 km)', 'COMB (mi/gal)', '(g/km)', '', '', '', '\n']



####################    Variables de base
import pickle as pk
import os
dossier_initial = os.getcwd()
circul = open("vehicules-circulation-2018.csv", errors = "replace")

emiss = open("2010.csv", errors = 'replace')

# differentes classes possibles
# base circulation [2]
CLAS_Promenade = ["PAU", "PMC", "PCY", "PHM"]
CLAS_Pro = ["CAU", "CMC", "CCY", "CHM", "TTA", "TAB", "TAS", "BCA", "CVO", "COT"]
CLAS_Circulation_Restreinte = ["RAU", "RMC", "RCY", "RHM", "RAB", "RCA", "RMN", "ROT"]
CLAS_Hors_Reseau = ["HAU", "HCY", "HAB", "HCA", "HMN", "HVT", "HVP", "HOT"]

# Types de vehicules utilises :
# automobile ou camion leger, Motocyclette, Aucun type specifique, cyclomoteur
TYP_VEH = ["AU", "MC", "AT", "CY"]
####################    Fin varaibles de base





####################    Lecture et enregistrement des bases
def remplir(seq, separateur = ',', enlever = '"'):
# pour une ligne de doc txt en csv (seq), remplit une liste selon le separateur choisi (on enleve les guillemets) et on la renvoie
	res = []
	mot = ''
	for lettre in seq:
		if lettre == separateur:
			res.append(mot)
			mot = ''
		elif lettre != enlever:
			mot = mot + lettre
	res.append(mot)
	return res


def EnregistrerDansListe(doc, nb_max = -1):
# Tout prendre d'un doc texte csv et mettre dans une liste (pas oublier de lui attitrer une variable)
# le nb max sert a pas depasser la memoire
	limite = nb_max > 0
	compteur = 0
	res = []
	for x in doc :
		if not limite or compteur < nb_max :
			res.append(remplir(x))
			if limite :
				compteur += 1
		else:
			break
	return res


def Arrange1ereLigne(l):	
# arranger les 2 1eres lignes en une seule (titre sur 2)
# /!\ ça retourne une liste donc faut assigner une variable au resultat
	for i in range(len(l[1])):
		l[1][i] = l[0][i] + " " + l[1][i]
	return l[1:]
####################    Fin lecture et enregistrement des bases





####################    Modification des bases
def rogne(mot, nb_max):
# prend un mot et le remplace par le meme avec seulement les premieres lettres
	res = ""
	if mot != 'MAZDA' and mot[:5] == 'MAZDA':
		return mot[5:]
	elif len(mot) > nb_max:
		i = 0
		while i < nb_max :
			res += mot[i]
			i += 1
		return res
	else:
		return mot


def rogne_liste(liste, elts_a_rogner, nb_lettres_max):
# rogne les mots places a elts_a_rogner dans chaque liste d'une grde liste ppale
	for x in liste:
		for elt in elts_a_rogner:
			x[elt] = rogne(x[elt], nb_lettres_max)

####################    Fin modification des bases





####################    Verification et tests
def verifie(doc_csv, tableau):
# On va verifier que pour chaque elt du doc_csv il trouve une correspondance dans le doc d'emission
	# ici ce sont les deux compteurs, qui doivent etre tout le temps egaux
	veh_2018 = 0
	veh_reconnus = 0
	# parcours de tous les veh
	for x in doc_csv:
		travail = remplir(x)
		if travail[0] == '2018':
			veh_2018 += 1
			# on va mtnt parcourir le tableau des emissions pour trouver la correspondance
			parcours = 0
			trouve = False
			while parcours < len(tableau) and not trouve:
				if travail[4] == tableau[parcours][1] and travail[5] == tableau[parcours][2]:
					trouve = True
				else :
					parcours += 1
			if trouve:
				veh_reconnus += 1
	print("veh de 2018 : ", veh_2018)
	print("veh reconnus : ", veh_reconnus)


def verifie_test(liste, tableau):
# On va verifier que pour chaque elt du doc_csv (liste) il trouve une correspondance dans le doc d'emission (tableau)
	# ici ce sont les deux compteurs, qui doivent etre tout le temps egaux
	# on enreg une liste avec toutes les erreurs
	veh_2018 = 0
	veh_reconnus = 0
	erreurs = []
	# parcours de tous les veh
	for travail in liste:
		if travail[6] == '2018':
			veh_2018 += 1
			# on va mtnt parcourir le tableau des emissions pour trouver la correspondance
			parcours = 0
			trouve = False
			while parcours < len(tableau) and not trouve:
				if travail[4] == tableau[parcours][1] and travail[5] == tableau[parcours][2]:
					trouve = True
				else :
					parcours += 1
			if trouve:
				veh_reconnus += 1
			else:
				erreurs.append(travail)
	print("veh de 2018 : ", veh_2018)
	print("veh reconnus : ", veh_reconnus)
	return erreurs


def correspond(lgn, a_compter):
# regarde si tous les attributs de la ligne correspondent aux criteres listes dans a_compter (cf plus bas pour compo de a_compter)
	bon = True
	for test in a_compter:
		if bon :
			bon_bis = False
			l = len(test[1])
			parcours = 0	
			while not bon_bis and parcours < l:
				if lgn[test[0]] == test[1][parcours]:
					bon_bis = True
				else :
					parcours += 1
			if not bon_bis:
				bon = False
	return bon

def stats(fichier, a_compter):
# compte dans un fichier le nb de lignes qui verifient les criteres a_compter
# a compter : liste [indice a regarder, liste des possibilites]
	compt = 0
	fic = open(fichier, 'r')
	for lgn in fic:
		if lgn[:4] == "2018":
			trav = remplir(lgn)
			if correspond(trav, a_compter):
				compt += 1
	print(compt)
####################    Fin verifiaction et tests





####################	Enregistrement
# dump(object, file)
# load(file)
def enregistre(obj, chemin, fichier):
# enregistre un objet donne dans un fichier etant donne le chemin d'acces (a partir de l'emplacement initial)
	path = dossier_initial + chemin
	os.chdir(path)
	fic = open(fichier, 'wb')
	pk.dump(obj, fic)
	fic.close()
	os.chdir(dossier_initial)

def Enreg_tout(chemin):
# enregistre tous les fichiers sous forme de liste dans le dossier chemin (a partir du dossier initial)
	#fic = open("1995-1999.csv", 'r')
	#emission = EnregistrerDansListe(fic)
	#emission = emission[2:]
	#init = emission[0][0]
	#prec = 0
	#cpt = 0
	#l = len(emission)
	#while cpt < l:
	#	if emission[cpt][0] != init:
	#		enregistre(emission[prec:cpt], chemin, init)
	#		prec = cpt
	#		init = emission[cpt][0]
	#	cpt += 1
	#enregistre(emission[prec:], chemin, init)
	#fic.close()
	for x in range(21):
		nom = str(2000+x)
		print(nom, type(nom))
		fic = open(nom + '.csv', 'r', errors = "replace")
		emission = EnregistrerDansListe(fic)[2:]
		enregistre(emission, chemin, nom)
		fic.close()

def convertit_circul():
# prend les docs csv de circulation et les met au format liste dans le meme dossier
	os.chdir('/home/pierre/Documents/Recherche/Données/Travail et modif des bases/Python/circulation_divisee')
	docs = os.listdir()
	for fic in docs:
		if fic.endswith('.csv'):
			ecriture = open(fic[:-4], 'wb')
			init = open(fic, 'r')
			liste = EnregistrerDansListe(init)
			pk.dump(liste, ecriture)
			ecriture.close()
			init.close()
	os.chdir(dossier_initial)
####################	Fin enregistrement





####################    Fonctions d'aide
def affiche(liste, deb, fin):
#affichage plus pratique d'une liste
	for x in liste:
		print(x[deb:fin])
####################    Fin fonctions d'aide





####################    Commandes
#emission = EnregistrerDansListe(emiss)
#emission = Arrange1ereLigne(emission)
# on met la marque et le modele a 5 lettres
#rogne_liste(emission[1:], [1, 2], 5)

#print("emission est la liste contenant les emissions")

#circulation = EnregistrerDansListe(circul, nb_max = 500)
#print("circulation est la liste contenant les modeles en circulation")
####################    Fin commandes

