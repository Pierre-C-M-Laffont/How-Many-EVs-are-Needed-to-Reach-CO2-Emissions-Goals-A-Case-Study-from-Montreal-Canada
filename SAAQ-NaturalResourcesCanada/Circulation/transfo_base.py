def transfo_CX5(n):
# prend toutes les lignes avec une MAZDA CX5 et remplace par CX-5
	nom = 'circulation_part' + str(n) + '_tri'
	l = enreg(nom)
	for lgn in l:
		if lgn[4] == 'MAZDA' and lgn[5] == 'CX5':
			lgn[5] = 'CX-5'
	fic = open(nom, 'wb')
	pk.dump(l, fic)
	fic.close()

def transfo_CX5_all():
	for n in range(133):
		print('base n° ', n)
		transfo_CX5(n)



def indicateurs_de_correspondance(n):
# ajoute 3 colonnes de booleens a notre base a la fin pour savoir si le veh a une correspondance exacte dans une base d'emission thermique, dans la base hybride, et dans la base elec
	nom = 'circulation_part' + str(n) + '_tri'
	l = enreg(nom)
	os.chdir(doss_emiss)
	hyb = enreg('hybrides_(1)')
	elec = enreg('elec_(1)')
	for lgn in l:
		if len(lgn) == 18:
			for i in range(3):
				lgn.append(False)
		if se_trouve(lgn, hyb):
			lgn[19] = True
		if se_trouve(lgn, elec):
			lgn[20] = True
	os.chdir(doss_circul)
	fic = open(nom, 'wb')
	pk.dump(l, fic)
	fic.close()

def indicateurs_de_correspondance_all():
# pour tous les enregistrements
	for n in range(133):
		print("base " + str(n))
		indicateurs_de_correspondance(n)

def copie_en_PAU(n):
# prend une base triee et la copie en prenant juste les PAU. On renomme aussi.
	l = enreg('circulation_part' + str(n) + '_tri')
	res = []
	for lgn in l:
		if lgn[2] == 'PAU':
			res.append(lgn)
	fic = open('PAU' + str(n), 'wb')
	pk.dump(res, fic)
	fic.close()

def copie_en_PAU_all():
	for n in range(133):
		print('base ' + str(n))
		copie_en_PAU(n)


##################
# Transfo FERRA 430 en F430
def FERRA430(n):
# recherche dans la base PAUn les modeles FERRA 430 et les remplace par FERRA F430
	trav = enreg('PAU' + str(n))
	for lgn in trav:
		if lgn[4] == 'FERRA' and lgn[5] == '430':
			print(lgn)
			ok = input('pour changer taper o')
			if ok == 'o':
				lgn[5] = 'F430'
#	fic = open('PAU' + str(n), 'wb')
#	pk.dump(trav, fic)
#	fic.close()

def FERRA430_all():
	for n in range(133):
		print('base ' + str(n))
		FERRA430(n)


def BMW_I3(base):
# remet les True et False au bon endroit pour les BMW I3
	trav = enreg('PAU' + str(base))
	for lgn in trav:
		if lgn[4] == 'BMW' and lgn[5] == 'I3' and int(lgn[6]) >= 2015 :
			print()
			print()
			print(lgn)
			ok = True # input('remplacer [True, True, False] par [False, True, True] ?  (o = oui)  ')
			if ok:
				lgn[18] = False
				lgn[19] = True
				lgn[20] = True
	fic = open('PAU'+ str(base), 'wb')
	pk.dump(trav, fic)
	fic.close()

def BMW_I3_all():
	for n in range(133):
		print()
		print('base ', n)
		BMW_I3(n)


def TESLA_all():
# met l'emission de toutes les TESLA a 0
	cpt = 0
	for n in range(133):
		print('\nbase ', n)
		fic = enreg('PAU' + str(n))
		for lgn in fic:
			if lgn[4] == 'TESLA' and lgn[21] < 0 and lgn[18:21] == [False] * 3:
				lgn[21] = 0
				cpt += 1
		drop = open('PAU' + str(n), 'wb')
		pk.dump(fic, drop)
		drop.close()
		print(cpt, ' modeles changes')

