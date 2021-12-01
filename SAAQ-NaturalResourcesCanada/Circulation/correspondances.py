# a taper dans le terminal pour executer : exec(open("correspondances.py").read())


#[AN	NOSEQ_VEH	CLAS	TYP_VEH_CATEG_USA	MARQ_VEH	MODEL_VEH	ANNEE_MOD	MASSE_NETTE	NB_CYL	CYL_VEH	NB_ESIEU_MAX	COUL_ORIG	TYP_DOSS_PERS	PHYS_SEX	PHYS_AGE	REG_ADM	MRC	CG_FIXE]


CLAS_Promenade = ["PAU", "PMC", "PCY", "PHM"]
CLAS_Pro = ["CAU", "CMC", "CCY", "CHM", "TTA", "TAB", "TAS", "BCA", "CVO", "COT"]
CLAS_Circulation_Restreinte = ["RAU", "RMC", "RCY", "RHM", "RAB", "RCA", "RMN", "ROT"]
CLAS_Hors_Reseau = ["HAU", "HCY", "HAB", "HCA", "HMN", "HVT", "HVP", "HOT"]


# automobile ou camion leger, Motocyclette, Aucun type specifique, cyclomoteur
TYPES_AUTORISES = ["AU"] #, "MC", "AT", "CY"]

CLASSES_AUTORISEES = ["PAU"]

pourcentage_elec = 0.004
pourcentage_hyb = 0.004 # (0.4%)


### Circulation
# CLAS = 2		TYP_VEH = 3		MARQUE = 4
# MODELE = 5		ANNEE = 6

### Emission
# MARQUE = 1		MODELE = 2

def se_trouve(ligne, liste):
# regarde si dans la "liste" de circulation on trouve le bon veh associe a "ligne"
	trouve = False
	cpt = 0
	fin = len(liste)
	while not trouve and cpt < fin:
		if ligne[6] == liste[cpt][0] and ligne[4] == liste[cpt][1] and ligne[5] == liste[cpt][2]:
			trouve = True
		cpt += 1
	return trouve


def cherche_corresp(n):
# tient une liste avec tous les cas sans corresp trouves, pour la partie circulation donnee (= n)
	os.chdir(doss_circul)
	trav = open('circulation_part' + str(n), 'rb')
	l = pk.load(trav)
	trav.close()
	os.chdir(doss_emiss)
	cpt = 0
	res = []
	for lgn in l:
		if lgn[6] != 'ANNEE_MOD':
			voir = open(lgn[6] + '_(1)', 'rb')
			if not se_trouve(lgn, pk.load(voir)):
				res.append(lgn)
				cpt += 1
			voir.close()
	print(cpt, ' erreurs')
	os.chdir(doss_circul)
	return res



##########################
##########################
##########################
##########################



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

##########################
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

##########################
def cylindree_en_L(cm3):
# convertit le cylindree de cm3 a L.
	return  int(int(cm3) / 100) / 10

##########################
def egalite_cylindree(emiss, circul):
# donne le critere d'egalite de cylindree pour deux listes
	return True

##########################
def critere_de_corresp_exacte(circul, emiss, indice):
# utilise dans la fonction suivante; donne le resultat de la condition de corespondance exacte
	egalite_modele = (circul[4] == emiss[indice][1] and circul[5] == emiss[indice][2]) # egalite marque et modele
	cyl_circul = circul[9]
	if cyl_circul != '':
		cyl_circul = cylindree_en_L(cyl_circul)
	nb_cyl_circul = circul[8]
	ok = egalite_modele  and (nb_cyl_circul == emiss[indice][5]) and (cyl_circul == float(emiss[indice][4]))
	# nb_cyl_circul == '' or 
	# cyl_circul == '' or 
	if ok :
		circul[18] = True
	return ok

##########################
def affichage_resultats(sans_partenaires, pref, trop_tot, etudies, exact0, cpt, cpt_pref, cpt_trop_tot, details):
# affiche les resultats des calculs
	exact = etudies - cpt - cpt_pref
	print()
	if details:
		print('les correspondances bancales sont :')
		for x in pref:
			print(x[1], x[6], x[4], x[5], x[8], x[9])
	print(exact, ' correspondances exactes')
	print(exact0)
	print(cpt_pref, ' correspondances bancales')
	print(cpt_trop_tot, ' trop tot')
	print(cpt, ' erreurs au total')
	print(etudies, ' etudies')
	print(exact*100//etudies, "% de correspondances exactes")
	print(cpt_pref*100//etudies, "% de correspondances bancales")
	print((cpt)*100//etudies, "% d'erreurs")
	return cpt

##########################
##########################
def cherche_corresp_triee(n, details = False):
# pareil que plus haut mais en tenant compte du fait que la liste est triee
# le code peut etre modifie pour travailler sur les fichiers globaux ou seulement PAU
	os.chdir(doss_circul)

	#trav = open('echantillon_tri', 'rb')
	#trav = open('circulation_part' + str(n) + '_tri', 'rb')
	nom = 'PAU' + str(n)
	trav = open(nom, 'rb')
	l = pk.load(trav)
	trav.close()

	os.chdir(doss_emiss)

	etudies = 0
	exact0 = 0
	cpt = 0
	cpt_prefixes = 0
	cpt_trop_tot = 0
	trop_tot = []
	res = []
	pref = []	# ce sera la liste pour laquelle le modele est un prefixe d'un modele dans la base d'emission
	annee_en_cours = '0' #l[0][6]

	#trav = open(annee_en_cours, 'rb')
	#emiss = pk.load(trav)	# la liste d'emssion actuelle
	#trav.close()
	#long_emiss = len(emiss)
	#parcours = 0		# curseur dans la liste d'emission
	for lgn in l:
		if lgn[6] >= '1995':

			# nouvelle base
			if lgn[6] != annee_en_cours:
				annee_en_cours = lgn[6]
				print('etude de ' + annee_en_cours)
				emiss = enreg(annee_en_cours + '_(5)')
				parcours = 0
				long_emiss = len(emiss)	

			# correspondance ?
			if critere_type(lgn) and critere_classe(lgn) and (not lgn[18] and not lgn[19] and not lgn[20]) : # pas deja exactement trouve
				etudies += 1
				p2 = parcours		# compteur pour la ligne
				p2_prefixe = parcours	# cmpteur pour la liste prefixes
				trouve = False		# cherche le suivant
				depasse = False 	# verif ordre alphabetique
				while not trouve and not depasse and p2 < long_emiss:
					if critere_de_corresp_exacte(lgn, emiss, p2):
						trouve = True
						exact0 += 1
					elif lgn[4] < emiss[p2][1]:
						depasse = True
					else:
						p2 += 1
				if trouve:
					parcours = p2
				# repartir en cherchant juste pour le prefixe
				else: 
					depasse = False
					while not trouve and not depasse and p2_prefixe < long_emiss:
						if lgn[4] == emiss[p2_prefixe][1] and emiss[p2_prefixe][2].startswith(lgn[5]) :
							trouve = True
						elif lgn[4] < emiss[p2_prefixe][1]:
							depasse = True
						else:
							p2_prefixe += 1
					if trouve:
						parcours = p2_prefixe
						pref.append(lgn)
						cpt_prefixes += 1
					# si on n'a rien trouve
					else:
						cpt += 1
						res.append(lgn)
		# si la date est trop ancienne
		else:
			trop_tot.append(lgn)
			cpt_trop_tot += 1
	os.chdir(doss_circul)
	# enregistrer les modifs apportees a la base
	trav = open(nom, 'wb')
	l = pk.dump(l, trav)
	trav.close()
	err = affichage_resultats(res, pref, trop_tot, etudies, exact0, cpt, cpt_prefixes, cpt_trop_tot, details)
	return err

##########################
##########################
##########################
##########################
def rallonge_a_21_all(nom):
	for n in range(133):
		fic = enreg(str(nom) + str(n))
		for l in fic:
			if len(l) < 22:
				l.append(-1)
		enr = open(str(nom) + str(n), 'wb')
		pk.dump(fic, enr)
		enr.close()
		print(n, ' fait')

def reinit_indicateurs_all():
# remet tous les indicateurs a False (colonnes 18, 19, 20)
	for n in range(133):
		print(n)
		trav = enreg('PAU' + str(n))
		for lgn in trav:
			lgn[18] = False
			lgn[19] = False
			lgn[20] = False
		fic = open('PAU' + str(n), 'wb')
		pk.dump(trav, fic)
		fic.close()		

###################
def elec_hyb_th(ligne, mm_veh):
# dit si la ligne rpz un veh qui peut etre associe a plusieurs bases. mm_veh est la liste brute
	trouve = False
	fin = len(mm_veh)
	ind = 0
	vect = []
	while not trouve and ind < fin:
		if mm_veh[ind][0] == [ligne[i] for i in [6, 4, 5]]:
			trouve = True
			vect = mm_veh[ind][1]
		ind += 1
	return trouve, vect

############
def depassement(lgn1, lgn2):
# regarde l'annee, marque, modele pour savoir
	if lgn1[6] < lgn2[0]:
		return True
	elif lgn1[6] == lgn2[0]:
		if lgn1[4] < lgn2[1]:
			return True
		elif lgn1[4] == lgn2[1] and lgn1[5] < lgn2[2]:
			return True
		else:
			return False
	else:
		return False

############
def correspondance_a_3(lgn1, lgn2):
# la lgn 1 est la circulation et la 2 est l'emission. Si on a une corresp en annee marque modele on met vrai dans l'indice (comme ca on sait qu'il faudra arrondir)
	return lgn1[6] == lgn2[0] and lgn1[4] == lgn2[1] and lgn1[5] == lgn2[2]



############
def cherche_pour_3(lgn, liste, ind_d):
# recherche dans la liste triee la ligne demandee a partir de l'indice donne. Si trouve, renvoie l'indice actuel, sinon l'initial
	ind = ind_d
	fin = len(liste)
	trouve = False
	arret = False
	while not trouve and not arret and ind < fin :
		if correspondance_a_3(lgn, liste[ind]):
			trouve = True
		elif depassement(lgn, liste[ind]) :
			arret = True
		else :
			ind += 1
	if trouve:
		return trouve, ind
	else:
		return trouve, ind_d


############
def new_corresp(base, mm_veh, elec, hyb, therm):
# pour attribuer les valeurs d'emission, la base mm_veh est la base brute (tous les modeles, avec les vecteurs de booleens associes)
# elec et hyb sont les bases d'emission derniere version
	os.chdir(doss_circul)
	fic = enreg('PAU' + str(base))
	annee_en_cours = 0
	res = []
	ind_th = 0
	ind_hyb = 0
	ind_elec = 0
	cpt_mm = 0
	cpt_th = 0
	cpt_hyb = 0
	cpt_elec = 0
	for lgn in fic:
		if lgn[18:21] == [False] * 3:
			mm, vecteur = elec_hyb_th(lgn, mm_veh)
			if mm:
				lgn[18] = vecteur[0]
				lgn[19] = vecteur[1]
				lgn[20] = vecteur[2]
				cpt_mm += 1
			else:
				ok_th, ind_th = cherche_pour_3(lgn, therm, ind_th)
				if ok_th:
					lgn[18] = True
					cpt_th += 1
				else:
					ok_hyb, ind_hyb = cherche_pour_3(lgn, hyb, ind_hyb)
					if ok_hyb :
						lgn[19] = True
						cpt_hyb +=1
					else:
						ok_elec, ind_elec = cherche_pour_3(lgn, elec, ind_elec)
						if ok_elec:
							lgn[20] = True
							cpt_elec += 1
						else:
							res.append(lgn)
	print(cpt_mm, ' vehicules de plusieurs bases')
	print(cpt_th, ' vehicules thermiques')
	print(cpt_hyb, ' vehicules hybrides')
	print(cpt_elec, ' vehicules elec')
	print(len(res), ' vehicules non comptes')
	return fic


def new_corresp_all():
	# enregistrer la base des veh avec corresp multiples
	os.chdir(doss_emiss)
	mm = enreg('mm_veh_brut')
	el = enreg('elec_(2)')
	hyb = enreg('hybrides_(3)')
	th = enreg('base_unique_(1)')
	for n in range(133):
		print('base ', n, ' :')
		resu = new_corresp(n, mm, el, hyb, th)
		print()
		fic = open('PAU' + str(n), 'wb')
		pk.dump(resu, fic)
		fic.close()
		print('enregistre')
		print()

####################
####################
def filtrage_cyl(liste, c_nb, c_cyl):
# pour une liste de modeles, ne garde que ceux de nb cyl le plus proche de cylindree le plus proche
	travail = liste
	inds = []
	mins = []
	ref = []
	res = []
	res2 = []
	if c_nb != '':
		inds.append(3)
		ref.append(c_nb)
		mins.append(abs(int(float(c_nb)*100) - int(float(travail[0][3])*100)))
		for mod in travail:
			mins[0] = min(mins[0], abs(int(float(mod[inds[0]])*100) - int(float(ref[0])*100)))
		for mod in travail:
			if abs(int(float(mod[inds[0]])*100) - int(float(ref[0])*100)) == mins[0]:
				res.append(mod)
		travail = res

	if c_cyl != '':
		inds.append(4)
		ref.append(c_cyl)
		mins.append(abs(int(float(c_cyl)*100) - int(float(travail[0][4])*100)))
		for mod in travail:
			mins[-1] = min(mins[-1], abs(int(float(mod[inds[-1]])*100) - int(float(ref[-1])*100)))
		for mod in travail:
			if abs(int(float(mod[inds[-1]])*100) - int(float(ref[-1])*100)) == mins[-1]:
				res2.append(mod)
		travail = res2


	emiss = 0
	for mod in travail:
		emiss += mod[5]
	emiss = emiss / len(travail)
	return emiss


#####################
def attribue_emiss(lgn, liste):
# pour un modele donne, on suppose qu'il est dans une seule base, donne une valeur d'emission correspondante. Dans la liste ya que les matchs annee-marque-modele
	nb_cyl = lgn[8]
	cyl = lgn[9]
	if cyl != '':
		cyl = cylindree_en_L(cyl)
#		if nb_cyl != '':
	lgn[21] = filtrage_cyl(liste, nb_cyl, cyl)
#		else :
#			# on a que le cylindree
#	elif nb_cyl != '':
#		# on a que le nb de cyl
#	else:
#		# on a R


#################
def attribue_emiss_approchee(lgn, th, hyb, el, dico, res):
# applique l'algo donne precedemment pour attribuer les emissions des modeles avec False x3
	etude = dico
	annee = int(lgn[6])
	if annee < 1995:
		lgn[21] = 6330 - annee * 3.036 # regression lineaire
	elif lgn[6] not in etude.keys():
		ok = input('annee nulle !!')
	else:
		etude = etude[lgn[6]]
		if lgn[4] not in etude.keys():
#			print()
#			print(lgn[4:7])
#			print(lgn[4], " n'est pas une marque")
			res.append(lgn)
		else:
			etude = etude[lgn[4]]
		lgn[21] = etude['tot'] / etude['nb']
		

###############
def attribue_emiss_multi(lgn_th, lgn_hyb, bools):
# etant donne les emissions de l'hyb, du thermique et de la compo du melange, return la valeur du melange
# ya forcement au moins 2 True dans les bools
	# utiliser pourcentage_elec & pourcentage_hyb
	if bools[0]:
		pth = 1
		if bools[1]:
			ph = pourcentage_hyb
			pth = pth - ph
		else:
			ph = 0
		if bools[2]:
			pe = pourcentage_elec
			pth = pth - pe # pas de else car les emiss des elec est nulle
	else:
		ph = pourcentage_hyb / (pourcentage_hyb + pourcentage_elec)
		pth = 0
	emiss = lgn_th[21] * pth + lgn_hyb[21] * ph # + emission du modele elec (0) * pe
	return emiss


###############
def actualise_inds(i_deb, i_fin, lgn, liste, init = False):
# renvoie les deux indices delimitant les modeles de la liste qui matchent annee-mq-mod avec la ligne
	fin = len(liste)
	if init:
		lgn = [0 for i in range(7)]
		lgn[6] = liste[0][0]
		lgn[4] = liste[0][1]
		lgn[5] = liste[0][2]
	if not init and correspondance_a_3(lgn, liste[i_deb]) :
		return i_deb, i_fin
	else:
		ok, i_deb = cherche_pour_3(lgn, liste, i_fin)
		if not ok:
			print('attention ya ptetre un bug')
			print(lgn)
			print()
			print(liste[i_deb])
			ok = input("entree si c'est bon ")
			print()
			print()
		i_fin = i_deb + 1
		while i_fin < fin and correspondance_a_3(lgn, liste[i_fin]):
			i_fin += 1
		return i_deb, i_fin


####################
def attribue_emiss_base(base, th, hyb, el, res, dico):
# attribue les emissions correspondantes pour tous les veh de la base pour lesquels c'est possible
# les indicateurs th_deb, th_fin... indiquent le deb et fin des matchs annee-mq-modele de chaque liste
	lgn_th = [0] * 22
	lgn_hyb = [0] * 22
	cpt = 0
	fic = enreg('PAU' + str(base))
	th_deb, th_fin = actualise_inds(0, 0, [], th, init = True)
	hyb_deb, hyb_fin = actualise_inds(0, 0, [], hyb, init = True)
	ind_elec = 0
	for lgn in fic :
		if lgn[18:21] == [True, False, False] and lgn[21] < 0:
			print('check')
			th_deb, th_fin = actualise_inds(th_deb, th_fin, lgn, th)
			attribue_emiss(lgn, th[th_deb:th_fin])
		elif lgn[18:21] == [False, True, False] and lgn[21] < 0:
			print('check')
			hyb_deb, hyb_fin = actualise_inds(hyb_deb, hyb_fin, lgn, hyb)
			attribue_emiss(lgn, hyb[hyb_deb:hyb_fin])
		elif lgn[18:21] == [False, False, True] and lgn[21] < 0:
			print('check')
			lgn[21] = 0 # les elec n'emettent pas
		elif (lgn[18] == True or lgn[19] == True or lgn[20] == True) and lgn[21] < 0:
			if lgn[18]:
				th_deb, th_fin = actualise_inds(th_deb, th_fin, lgn, th)
				lgn_th = [x for x in lgn]
				attribue_emiss(lgn_th, th[th_deb:th_fin])
			if lgn[19]:
				hyb_deb, hyb_fin = actualise_inds(hyb_deb, hyb_fin, lgn, hyb)
				lgn_hyb = [x for x in lgn]
				attribue_emiss(lgn_hyb, hyb[hyb_deb:hyb_fin])
			lgn[21] = attribue_emiss_multi(lgn_th, lgn_hyb, lgn[18:21]) # ce sera un return
		elif lgn[18:21] == [False] *3 and lgn[21] < 0 :
			cpt +=1
			attribue_emiss_approchee(lgn, th, hyb, el, dico, res)
	print(cpt, ' changes')
#	drop = open('PAU' + str(base), 'wb')
#	pk.dump(fic, drop)
#	drop.close()

def attribue_emiss_all():
# pour toutes les bases
	dico = enreg('resu_moyennes')
	os.chdir(doss_emiss)
	solos = []
	th = enreg('base_unique_(1)')
	hyb = enreg('hybrides_(3)')
	el = enreg('elec_(2)')
	os.chdir(doss_circul)
	for n in range(133):
		print('base ', n, ' etudiee')
		attribue_emiss_base(n, th, hyb, el, solos, dico)
	solo_tri = []
	for mod in solos:
		mod2 = [mod[i] for i in [6, 4]]
		if mod2 not in solo_tri:
			solo_tri.append(mod2)
	return solo_tri
		

