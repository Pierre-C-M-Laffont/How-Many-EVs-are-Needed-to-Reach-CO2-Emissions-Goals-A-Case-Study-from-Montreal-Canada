

def trouve(lgn, liste):
# cherche une corresp (annee, marque, modele) dans la liste
	fin = len(liste)
	trouv = False
	ind = 0
	while ind < fin and not trouv:
		if lgn[0] == liste[ind][0] and lgn[1] == liste[ind][1] and lgn[2] == liste[ind][2]:
			trouv = True
		ind += 1
	return trouv

def trouve_therm(lgn):
# cherche corresp (marque, modele) dans l'annee demandee
	trav = enreg(lgn[0] + '_(5)')
	return trouve(lgn, trav)


# regarder si les modeles hybrides / elec / thermiques ont les mêmes marques & nom de modèle
def mm_veh():
# pour la base hybride (ou elec), regarder dans la base elec (ou hybride) si on trouve
	hybride = enreg('hybrides_(2)')
	f_h = len(hybride)
	elec = enreg('elec_(2)')
	f_e = len(elec)
#	corresp_hybrides = []
#	corresp_thermique = []
	res = []
	ind = 0
	while ind < f_e:
		remplir_h = False
		remplir_th = False
#		print(elec[ind][1] + ' ' + elec[ind][2] + " de l'annee " + elec[ind][0] + " ?")
		if trouve(elec[ind], hybride):
#			corresp_hybrides.append(elec[ind])
			remplir_h = True
		if trouve_therm(elec[ind]):
#			corresp_thermique.append(elec[ind])
			remplir_th = True
		if remplir_h or remplir_th and [elec[ind][:3], [True, remplir_h, remplir_th]] not in res :
			res.append([elec[ind][:3], [True, remplir_h, remplir_th]])
		ind += 1
	ind = 0
	while ind < f_h :
		if trouve_therm(hybride[ind]) and [hybride[ind][:3], [True, True, True]] not in res:
			res.append([hybride[ind][:3], [False, True, True]])
		ind += 1
#	print('corresp_hybrides : ')
#	for x in corresp_hybrides:
#		print(x[:3])
#	print('corresp_thermique :')
#	for x in corresp_thermique:
#		print(x[:3])
	return res


def liste_corresp(liste, nom):
	fic = open(nom, 'wb')
	res = []
	for x in liste:
		res.append(x[:3])
	pk.dump(res, fic)
	fic.close()

def resu_mm_veh(liste):
# enregistre dans un fichier txt et dans un fichier liste les correspondances trouvees par la fction mm_veh
	tout = open('mm_veh_tout', 'wb')
	el_hyb = open('mm_veh_elec-hybride', 'wb')
	el_th = open('mm_veh_elec-thermique', 'wb')
	hyb_th = open('mm_veh_hybride-thermique', 'wb')
	resu_txt = open('mm_veh_resu.txt', 'w')
	tt = []
	eh = []
	et =[]
	ht = []
	for lgn in liste :
		cond = lgn[1]
		if cond[0] and cond[1] and cond[2]:
			tt.append(lgn[0])
		elif cond[0] and cond[1] :
			eh.append(lgn[0])
		elif cond[0] and cond[2] :
			et.append(lgn[0])
		elif cond[1] and cond[2] :
			ht.append(lgn[0])
	pk.dump(tt, tout)
	pk.dump(eh, el_hyb)
	pk.dump(et, el_th)
	pk.dump(ht, hyb_th)
	tout.close()
	el_hyb.close()
	el_th.close()
	hyb_th.close()
	resu_txt.write('modeles communs aux trois bases :\n\n')
	for l in tt:
		resu_txt.write(str(l) + '\n')
	resu_txt.write('\n\nmodeles elec ou hybrides :\n\n')
	for l in eh:
		resu_txt.write(str(l) + '\n')
	resu_txt.write('\n\nmodeles elec ou thermiques :\n\n')
	for l in et:
		resu_txt.write(str(l) + '\n')
	resu_txt.write('\n\nmodeles hybrides ou thermiques :\n\n')
	for l in ht:
		resu_txt.write(str(l) + '\n')
	resu_txt.close()
	fic = open('mm_veh_brut', 'wb')
	pk.dump(liste, fic)
	fic.close()


def traitement_hyb_th():
# fonction faite le 29 juillet pour regarder ce qu'on fait des vehicules thermiques et hybrides semblables.
# resultat : on peut en general pas les separer avec le cylindree
	fic = enreg('mm_veh_hybride-thermique')
	for lgn in fic:
		th = enreg(lgn[0] + '_(6)')
		hyb = enreg('hybrides_(3)')
		lth = []
		lhyb = []
		for l in th :
			if l[:3] == lgn[:3]:
				lth.append(l)
		for l in hyb:
			if l[:3] == lgn[:3]:
				lhyb.append(l)
		print('thermiques :\n')
		for l in lth:
			print(l[3], l[4])
		print('\n\nhybrides :\n')
		for l in lhyb:
			print(l[3], l[4])
		input('verification')


#######################
#######################
#######################
# Tests pour faire des correspondances exactes avec les MAZDA

def affiche_prefixes_mazda(n):
# affiche toutes les lignes d'une annee de MAZDA dont le modele commence par certaines chaines de caracteres
# fonction a reecrire pour reutiliser si des changements ont ete faits a la base
	trav = enreg(str(n) +  '_(2)_tri')
	pref = ['3', '5', '6', 'CX-3', 'CX-5', 'CX-9']
	res = []
	for lgn in trav:
		if lgn[1] == 'MAZDA':
			ok = False
			i = 0
			while i < 6 and not ok:
				if lgn[2].startswith(pref[i]):
					ok = True
				i += 1
			if ok:
				res.append(lgn)
	for l in res:
		print(l[0:3])

def affiche_prefixes_mazda_all():
	for n in range(1995, 2021):
		affiche_prefixes_mazda(n)



#######################
#######################
#######################
#######################
#######################


# regarder si les modeles de meme annee, marque, modele ont necessairement le meme nombre de cylindres et le même cylindree
def verifie_cylindree(n, version = 2):
# pour l'annee n, renvoie la liste des modeles qui ont memes annee, marque, modele et pas le meme nb de cyl ou cylindree
	trav = enreg(str(n) + '_(' + str(version) + ')_tri')
	a_comparer = trav[0]
	res = []
	groupe = [a_comparer] # le groupe de tous ceux qui ont pas les memes cylindres
	cpt = 0
	a_ajouter = False # si le groupe presente le detail cherche
	for lgn in trav:
		if a_comparer[:3] == lgn[:3] :
			groupe.append(lgn)
			if (a_comparer[4] != lgn[4] or a_comparer[5] != lgn[5]):
				a_ajouter = True
		else:
			if a_ajouter :
				res.append(groupe)
				cpt += 1
			a_comparer = lgn
			groupe = [lgn]
			a_ajouter = False
	print(cpt, ' groupes reperes')
	return res

def verifie_cylindree_all(version = 2):
	res = []
	for n in range(1995, 2021):
		res = res + verifie_cylindree(n, version)
	return res


# au niveau des emissions
def impact_cylindree(n, version = 2):
# renvoie une liste avec les emissions possibles selon le cylindree pour un meme modele
	trav = enreg(str(n) + '_(' + str(version) + ')_tri')
	a_comparer = trav[0]
	res = []
	groupe = [a_comparer] # le groupe de tous ceux qui ont pas les memes cylindres
	cpt = 0
	a_ajouter = False # si le groupe presente le detail cherche
	for lgn in trav:
		if a_comparer[:3] == lgn[:3] :
			groupe.append(lgn)
			if (a_comparer[4] != lgn[4]):
				a_ajouter = True
		else:
			if a_ajouter :
				liste_des_emiss = []
				for x in groupe:
					liste_des_emiss.append(float(x[12]))
				res.append(liste_des_emiss)
				cpt += 1
			a_comparer = lgn
			groupe = [lgn]
			a_ajouter = False
	print(cpt, ' groupes reperes pour ', n)
	return res

def impact_cylindree_all(version = 2):
	res = []
	for n in range(1995, 2021):
		res = res +impact_cylindree(n, version)
	return res


def ecarts_max(liste_cylindrees):
# a partir de la liste de listes de cylindrees possibles pour un meme modele, donne 2 listes avec la valeur min d'emission et les ecarts max d'emission pour un meme modele
	res = []
	base = []
	for l in liste_cylindrees:
		res.append(max(l) - min(l))
		base.append(min(l))
	return (base, res)


def ecarts_min(liste_groupes):
# a partir de la liste des groupes de meme modele, donne 1 liste avec la valeur d'ecart min d'emission pour un meme modele
	res = []
	base = []
	trav = []
	for grp in liste_groupes:
		g = []
		for lgn in grp:
			g.append(float(lgn[4]))
		trav.append(g)
	for l in trav:
		l.sort()
		m = 10000
		for i in range(1, len(l)):
			ecart = l[i] - l[i-1]
			if ecart > 0:
				m = min(m, ecart)
		if m ==10000:
			print(l)
		res.append(m)
		base.append(min(l))
	return (base, res)


def valeurs_cylindree(n):
# renvoie une liste triee de tous les cylindrees possibles pour l'annee n
	trav = enreg(str(n) + '_(2)_tri')
	res = []
	for lgn in trav:
		res.append(float(lgn[4]))
	res.sort()
	return res

#######################
#######################
#######################
#######################
#######################
# tests generaux sur les marques
def lister_emiss_all(marque, version = 3, titre = 'resultat_modeles_emission_actuels'):
# liste tous les modeles existant en emission
	res = []
	for n in range(1995, 2021):
		print(n)
		trav = enreg(str(n) + '_(' + str(version) + ')')
		for lgn in trav:
			ajout = lgn[1:3]
			if ajout[0] == marque and not ajout in res:
				res.append(ajout)
	os.chdir(doss_historique_transfos)
	fic = open(titre, 'w')
	for lgn in res:
		fic.write(str(lgn) + '\n')
	fic.close()
	os.chdir(doss_emiss)
	

def lister_marques_all():
# donne toutes les marques possibles pour les bases d'emission
	res = []
	for n in range(1995, 2021):
		fic = enreg(str(n) + '_(3)')
		for lgn in fic:
			if not lgn[1] in res:
				res.append(lgn[1])
	os.chdir(doss_historique_transfos)
	fic = open('liste_des_marques', 'w')
	for l in res:
		fic.write(l + '\n')
	fic.close()
	os.chdir(doss_emiss)

def lister_marques_hybridelec():
# donne toutes les marques possibles pour les bases d'emission
	res = []
	for nom in ['elec_(1)', 'hybrides_(1)']:
		fic = enreg(nom)
		for lgn in fic:
			if not lgn[1] in res:
				res.append(lgn[1])
	os.chdir(doss_historique_transfos)
	fic = open('liste_des_marques_hybridelec', 'w')
	for l in res:
		fic.write(l + '\n')
	fic.close()
	os.chdir(doss_emiss)




def lister_modeles(marque, annee = False, cpt = True, nom_fic_enreg = 'resultat_actuel_lister_modeles'):
# pour une marque donnee, lister les modeles associes dans la base de circulation
	os.chdir(doss_historique_transfos)
	fic = open(nom_fic_enreg, 'w')
	os.chdir(doss_veh)
	if annee and cpt:
		travail = enreg('liste_veh_brute_avec_compteurs')
		indice = 1
	elif not annee and not cpt :
		travail = enreg('veh_sans_annee_tri')
		indice = 0
	elif annee and not cpt:
		travail = enreg('liste_veh_tri')
		indice = 1
	else:
		travail = enreg('veh_sans_annee_compteurs')
		indice = 0
	res = []
	ecriture = []
	for lgn in travail:
		if cpt:
			if lgn[0][indice] == marque:
				res.append(lgn[0])
				fic.write(str(lgn) + '\n')
		else:
			if lgn[indice] == marque:
				res.append(lgn)
				fic.write(str(lgn) + '\n')
	os.chdir(doss_historique_transfos)
	fic.close()
	os.chdir(doss_emiss)
	return res

#	os.chdir(doss_circul)
#	travail = enreg('PAU' + str(n))
#	res = liste
#	for lgn in travail:
#		if lgn[4] == marque:
#			ajout = [lgn[i] for i in [6, 4, 5]]
#			if not ajout in res:
#				res.append(ajout)
#	os.chdir(doss_emiss)
#	for lgn in res:
#		print(lgn)
#
#def lister_modeles_all(marque):
#	res = []
#	for n in range(133):
#		print('base ', n, ' en cours...')
#		lister_modeles(marque, n, res)
#		print()
#	return res



def modeles_matchant_pas(marque, m_circul, annee, version, liste_des_resu, matchs, regarder_annee = False):
# regarde dans la base d'emission annee si un ou plusieurs modeles de la marque donnee ne matche pas avec ceux de la liste m_circul
# /!\ c'est ecrit pour l'instant avec un truc non trie
	res = []
	trav = enreg(str(annee) + '_(' + str(version) + ')')
	for lgn in trav:
		if regarder_annee:
			ajout = [lgn[i] for i in [0, 1, 2]]
		else:
			ajout = [lgn[i] for i in [1, 2]]
		if lgn[1] == marque:
			if not ajout in m_circul:
				res.append(ajout)
				if not [ajout[-1]] in liste_des_resu:
					liste_des_resu.append([ajout[-1]])
			elif not ajout[-1] in matchs:
				matchs.append(ajout[-1])
	for lgn in res:
		print(lgn)

def modeles_matchant_pas_all(marque, m_circul, version, nom = 'resultat_actuel_modeles_matchant_pas_all', regarder_annee = False):
	res = []
	matchs = []
	os.chdir(doss_historique_transfos)
	fic = open(nom, 'w')
	os.chdir(doss_emiss)
	for n in range(1995, 2021):
		print('annee ', n, ' :')
		modeles_matchant_pas(marque, m_circul, n, version, res, matchs, regarder_annee)
		print()
	print('\n\n\n\nFinalement les erreurs sont : ')
	for l in res:
		print(l)
		fic.write(str(l) + '\n')
	print(len(res))
	fic.write('\net les matchs sont :\n\n')
	for l in matchs:
		fic.write(str(l) + '\n')
	os.chdir(doss_historique_transfos)
	fic.close()
	os.chdir(doss_emiss)



def modeles_matchant_pas_hybridelec(marque, m_circul, version, nom = 'resultat_actuel_modeles_matchant_pas_all', regarder_annee = False):
	resh = []
	matchsh = []
	rese = []
	matchse = []
	os.chdir(doss_historique_transfos)
	fic = open(nom, 'w')
	os.chdir(doss_emiss)
	print('les hybrides :')
	print()
	modeles_matchant_pas(marque, m_circul, 'hybrides', version, resh, matchsh, regarder_annee)
	print()
	print()
	print('les elec :')
	print()
	modeles_matchant_pas(marque, m_circul, 'elec', version, rese, matchse, regarder_annee)
	print('\n\n\n\nFinalement les erreurs sont : ')
	print('- hybrides')
	fic.write('\nhybrides :\n')
	for l in resh:
		print(l)
		fic.write(str(l) + '\n')
	fic.write('\net les matchs sont :\n\n')
	for l in matchsh:
		fic.write(str(l) + '\n')
	print('\n- elec:')
	fic.write('\nelec :\n')
	for l in rese:
		print(l)
		fic.write(str(l) + '\n')
	fic.write('\net les matchs sont :\n\n')
	for l in matchse:
		fic.write(str(l) + '\n')
	os.chdir(doss_historique_transfos)
	fic.close()
	os.chdir(doss_emiss)
