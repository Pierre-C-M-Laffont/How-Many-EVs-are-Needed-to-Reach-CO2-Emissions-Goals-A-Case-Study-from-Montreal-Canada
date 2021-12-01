##########
##########
#	Copie-colle correspondance
##########
##########

CLAS_Promenade = ["PAU", "PMC", "PCY", "PHM"]
CLAS_Pro = ["CAU", "CMC", "CCY", "CHM", "TTA", "TAB", "TAS", "BCA", "CVO", "COT"]
CLAS_Circulation_Restreinte = ["RAU", "RMC", "RCY", "RHM", "RAB", "RCA", "RMN", "ROT"]
CLAS_Hors_Reseau = ["HAU", "HCY", "HAB", "HCA", "HMN", "HVT", "HVP", "HOT"]


# automobile ou camion leger, Motocyclette, Aucun type specifique, cyclomoteur
TYPES_AUTORISES = ["AU", "MC", "AT", "CY"]

CLASSES_AUTORISEES = CLAS_Promenade + CLAS_Circulation_Restreinte

def critere_type(lgn):
# informe si une ligne correspond aux criteres de type de vehicule
	trouve = False
	ind = 0
	l = len(TYPES_AUTORISES)
	while not trouve and ind < l:
		if lgn[3] == TYPES_AUTORISES[ind]:
			trouve = True
		ind += 1
	return trouve

def critere_classe(lgn):
# informe si une ligne correspond aux criteres de classe de vehicule (commercial ou autre)
	trouve = False
	ind = 0
	l = len(CLASSES_AUTORISEES)
	while not trouve and ind < l:
		if lgn[2] == CLASSES_AUTORISEES[ind]:
			trouve = True
		ind += 1
	return trouve

##########
##########
#	Fin copie-colle
##########
##########





# modele = 5

def compte_modeles_composes(n):
# donne le nb de modeles ayant un espace dans leur nom
	fic = open('circulation_part' + str(n) + '_tri', 'rb')
	l = pk.load(fic)
	fic.close()
	cpt = 0
	res = []
	for lgn in l:
		if lgn[5].count(' ') >= 1 and critere_classe(lgn) and critere_type(lgn) and (lgn[4] != "GUZZI" or lgn[5] != "V7 II"):
			if res == [] or res[-1][5] != lgn[5]:
				res.append(lgn)
				cpt += 1
	print('base ', n, ' :')
	for x in res:
		print(x[6], x[4], x[5])
	return cpt

def modeles_composes_totaux():
# pour toutes les bases
	compteur = 0
	for n in range(133):
		compteur += compte_modeles_composes(n)
	return compteur


#########################
#########################
#########################
#########################
# Les MAZDA

def compte_modeles_particuliers(n):
# compte des modeles bien particuliers de MAZDA (en fait c'est pour vois si ils existent dans les bases)
	etude = ['CX-30', '6 TUR', '6 SPO', '3 TUR', '323', '626']
	trav = enreg('PAU' + str(n))
	cpt = [0, 0, 0, 0, 0, 0]
	for lgn in trav:
		if lgn[4] == 'MAZDA':
			ok = False
			i = 0
			while i < 6 and not ok:
				if lgn[5].startswith(etude[i]):
					ok = True
					cpt[i] += 1
				i += 1
#	for x in range(6):
#		print(etude[x], ' : ', cpt[x], ' trouves')
	return cpt

def compte_modeles_particuliers_all():
	etude = ['CX-30', '6 TUR', '6 SPO', '3 TUR', '323', '626']
	c_tot = [0, 0, 0, 0, 0, 0]
	for n in range(133):
		print(n)
		cpt = compte_modeles_particuliers(n)
		for i in range(6):
			c_tot[i] = c_tot[i] + cpt[i]
	for x in range(6):
		print(etude[x], ' : ', c_tot[x], ' trouves')




##### compter les modeles MX ou CX sans "-"
def compte_MX_CX(n):
	l = enreg('circulation_part' + str(n) + '_tri')
	res = []
	for lgn in l:
		if lgn[4] == 'MAZDA' and ((lgn[5].startswith('MX') and not lgn[5].startswith("MX-")) or (lgn[5].startswith('CX') and not lgn[5].startswith('CX-'))):
			res.append(lgn)
	for lgn in res:
		print(lgn[1], lgn[6], lgn[4], lgn[5])
	#return res

def compte_MX_CX_all():
	for n in range(133):
		#print('pour la base ' + str(n) + ' : ', '\n')
		compte_MX_CX(n)



#########################
#########################
#########################
#########################



##### compter les vehicules appartenent a une classe particuliere
def compte_classe(n, classe = "PAU"):
# compte juste le nombre de veh de la classe indiquee
	l = enreg('circulation_part' + str(n) + '_tri')
	cpt = 0
	for lgn in l:
		if lgn[2] == classe and lgn[3] == "AU":
			cpt += 1
	return cpt

def compte_classe_all(classe = "PAU"):
	compteur = 0
	for n in range(133):
		print('etude de la partie ' + str(n))
		compteur += compte_classe(n, classe)
	return compteur

##### Compter les veh elec, hybrides, thermiques qu'on pourra pas differencier
def fait_partie_de(liste, ligne):
# regarde si une ligne de notre tableau correspond aux vehicules donnes dans la liste
	trouve = False
	fin = len(liste)
	ind = 0
	while ind < fin and not trouve:
		travail = liste[ind]
		if ligne[6] == travail[0] and ligne[4] == travail[1] and ligne[5] == travail[2] :
			trouve = True
		ind += 1
	return trouve

def compte_elec_therm_hybride(n, liste_a_etudier):
# les veh elec-therm de l'enregistrement n
	l = enreg('circulation_part' + str(n) + '_tri')
	cpt = 0
	for lgn in l:
		if lgn[2] == "PAU" and fait_partie_de(liste_a_etudier, lgn):
			cpt += 1
	return cpt

def compte_elec_therm_hybride_all(nom_a_etudier):
	cpt = 0
	os.chdir(doss_emiss)
	liste_a_etudier = enreg(nom_a_etudier)
	os.chdir(doss_circul)
	for n in range(133):
		print("etude de l'enregistrement " + str(n))
		cpt += compte_elec_therm_hybride(n, liste_a_etudier)
	return cpt


def compte_nbcyl_et_cylindree(n):
# compte le nombre de valeurs vides dans la liste
	trav = enreg('PAU' + str(n))
	cpt = 0
	nbcyl = []
	cylindree = []
	for lgn in trav:
		cpt += 1
		if lgn[8] == '':
			nbcyl.append(lgn)
		if lgn[9] == '':
			cylindree.append(lgn)
	print(str(len(nbcyl)) + ' sans nombre de cylindres')
	print(str(len(cylindree)) + ' sans cylindree')
	print('parmi ' + str(cpt) + ' vehicules')
	return nbcyl, cylindree


#########################
#########################
#########################
#########################
#########################
#########################
# Creation d'un fichier avec tous les modeles rencontres dans la base de circulation

def compte(ajout, liste):
# dans une liste comprenant des compteurs, soit ça incremente un compteur si il existe, soit ça en ajoute un
	fin = len(liste)
	i = 0
	ok = False
	while not ok and i < fin:
		if liste[i][0] == ajout:
			liste[i][1] += 1
			ok = True
		else:
			i +=1
	if i == fin:
		liste.append([ajout, 1])

def vehicules_base_simple(n, liste = []):
# renvoie la liste de tous les veh presents (un seul exemplaire)
	trav = enreg('PAU' + str(n))
	res = liste
#	i = 0
	for lgn in trav:
		ajout = [lgn[i] for i in [6, 4, 5]]
		compte(ajout, res)
#		i +=1
#		if i %1000 == 0:
#			print('modele numero ', i)
	print('nombre de veh comptes : ', len(res))
	return res

def vehicules_all(liste = []):
	res = []
	for n in range(133):
		print('base ', n)
		vehicules_base_simple(n, res)
		print()
	return res

#####################
#####################
#####################
#####################

def visu_emiss():
# affiche un histogramme des emissions des veh en fonction des émissions
	x = [10* i for i in range(80)]
	y = [0 for i in range(80)]
	for n in range(133):
		print(n)
		trav = enreg('PAU' + str(n))
		for mod in trav:
			em = mod[21]
			if em > 0:
				y[int(em/10)] += 1
	plt.plot(x, y)
	plt.show()

def elec_therm_selon_cyl():
# renvoie le nb de veh elec ou thermiques, puis compte ceux qui ont des cylindrees, nb de cyl, et ceux qui en ont pas
	tot = 0
	cel = 0
	cth = 0
	c1des2 = 0
	for n in range(133):
		print(n)
		fic = enreg('PAU' + str(n))
		for mod in fic:
			if mod[18] and mod[20] and not mod[19]:
				tot += 1
				if mod[8] != '' and mod[9] != '':
					cth += 1
				elif mod[8] != '' or mod[9] != '':
					c1des2 += 1
				else :
					cel += 1
	print(tot, ' au tot')
	print(cel, ' elec')
	print(cth, ' thermique')
	print(c1des2, ' pas complets')
"""
def cpte_elec():
# tous les elec (on verif que pas d'infos en cyl et nb de cyl
	cpt = 0
	tot = 0
	for n in range(133):
		print(n)
		fic = enreg('PAU' + str(n))
		for mod in fic:
			tot += 1
			if mod[20]:# and mod[8] == '' and mod[9] == '':
				cpt += 1
	pourc = cpt / tot * 100
	print()
	print(tot, ' veh au total')
	print(cpt, ' veh elec')
	print('rpz ', pourc, ' %')
"""

def emission_par_annee():
# dresse le graphique des emissions par annee pour les veh dont c'est connu
	x = [n for n in range(1995, 2020)]
	y = [0 for n in range(1995, 2020)]
	cpt = [0 for n in range(1995, 2020)]
	y2 = [-3.036*n + 6330 for n in range(1995, 2020)]
	for n in range(133):
		print('base ', n)
		fic = enreg('PAU' + str(n))
		for mod in fic:
			if mod[21] >= 0:
				y[int(mod[6]) - 1995] += mod[21]
				cpt[int(mod[6]) - 1995] += 1
	for i in range(len(y)):
		if cpt[i] != 0:
			y[i] = y[i] / cpt[i]
	dimin_emiss = [y[i+1] - y[i] for i in range(24)]
	for n in dimin_emiss:
		print(n)
#	plt.plot(x[1:], dimin_emiss)
	plt.plot(x, y)
	plt.plot(x, y2)
	plt.show()



def fichier_moyennes():
# parcourt tous les fichiers et fait les moyennes des vehicules
# en fait c'est un tres gros dico
# chaque partie du dico ya 	'tot' (somme de tous les veh correspondant a la section)
#				'nb' (le nb de veh dans la section)
#				les sous-sections
	dico = {'tot' : 0, 'nb' : 0}
	for n in range(133):
		print('etude de la base ', n)
		trav = enreg('PAU' + str(n))
		for lgn in trav:
			if lgn[21] > 0 and lgn[18:21] != [False] * 3: # on ne prend que les veh qui sont deja comptes
				dico['tot'] += lgn[21]
				dico['nb'] += 1
				if lgn[6] not in dico.keys(): # moyennes annee
					dico[lgn[6]] = {'tot' : lgn[21], 'nb' : 1}
				else:
					dico[lgn[6]]['tot'] += lgn[21]
					dico[lgn[6]]['nb'] += 1
				
				if lgn[4] not in dico[lgn[6]].keys(): # moyennes annee-marque
					dico[lgn[6]][lgn[4]] = {'tot' : lgn[21], 'nb' : 1}
				else:
					dico[lgn[6]][lgn[4]]['tot'] += lgn[21]
					dico[lgn[6]][lgn[4]]['nb'] += 1
	drop = open('resu_moyennes', 'wb')
	pk.dump(dico, drop)
	drop.close()	



def ecriture_rec(dico, tab, entete, fic):
# Remplit le fichier par recurrence En arguments le dico sur lequel travailler, la tabulation, et le fichier sur lequel on travaille
	fic.write(tab* '\t' + 'emissions moyennes : ' + str(dico['tot']/dico['nb']) + '\tpour\n')
	for key in dico.keys():
		if key == 'tot':
			fic.write(tab* '\t' + 'somme des emissions : ' + str(dico['tot']) + '\n')

		elif key == 'nb':
			fic.write(tab* '\t' + 'nombre de vehicules etudies : ' + str(dico['nb']) + '\n')
		else:
			fic.write('\n' + (tab)* '\t' + entete)
			fic.write('\n' + (1+tab)* '\t' + str(key) + '\n')
			ecriture_rec(dico[key], tab + 1,str(key) , fic)
			fic.write((2-tab)*'\n')


def ecriture_moyennes():
# ecrit tout ca au propre dans un doc texte.
	dico = enreg('resu_moyennes')
	fic = open('resu_moyennes.txt', 'w')
	ecriture_rec(dico, 0, '', fic)
	fic.close()
	
