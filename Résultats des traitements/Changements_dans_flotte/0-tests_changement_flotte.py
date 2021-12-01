"""
L'idee ici c'est de changer les vehicules de groupe pour arriver a atteindre les objectifs de reduction

variables a suivre:
	emissions totales
	nb de vehicules modifies

On va proceder comme ça :
	il faudra manip des tableaux de type AD x groupe avec des valeurs differentes
	a partir de ces tableaux on doit avoir une fonction qui nous calcule les émissions totales (km*GES/km)			FAIT
	
	on doit aussi avoir une fonction qui transforme la base des véhicules par AD (changer de groupe)				FAIT
	pour suivre la variation d'emissions en continu on peut utiliser [delta_emiss = nb_veh*(emiss_1 - emiss_2)*km_tot_pr_AD]
	
	une fonction d'objectif : les emissions de depart, la variation demandee, la base de depart, qui la modifie jusqu'à passer l'objectif
																	FAIT

	une fonction qui donne les changements au niveau des vehicules
"""


import pandas as pd
import geopandas as gpd
import numpy as np
import random as rd
import pickle as pk



##########
########## Variables utilisees
##########

fichier_AD = "../outs/emissions_final_par_AD"
fichier_SM = "../outs/emissions_final_par_SM"
fichier_vehicules = "../GO_PAU_par_groupe.csv"
fichier_AD_SM = "../outs/equivalence_AD_SM.pkl"
fichier_propre = "veh_par_SM_2030.csv"

# ->-> a regarder si on prend elec a 0 ou a 6.9 gCO2/km
fichier_emissions_par_groupe = "../emissions_groupe_elec_nn_nul.csv" 
fichier_emissions_par_groupe = "../emissions_USA.csv" 
#fichier_emissions_par_groupe = "../emissions_groupe.csv"


facteur_annu = 335

cible_emission = 2.3125 # en Mtonnes

##########
########## Import des bases
##########

print("import des bases...")
corres = pd.read_pickle(fichier_AD_SM)
AD = gpd.read_file(fichier_AD)
SM = gpd.read_file(fichier_SM)
veh = pd.read_csv(fichier_vehicules)
emiss_par_gr = pd.read_csv(fichier_emissions_par_groupe)
propre = pd.read_csv(fichier_propre)
print("importé\n")















#"""
##########
########## Fonctions utiles
##########

class TableATester :

	def __init__(self, base, decoupage="Sm100", emiss=emiss_par_gr, nom="Ma Table", grp = 10):
		self.t = pd.DataFrame(base[[decoupage, "gr0", "gr1", "gr2", "gr3", "gr4", "gr5", "gr6", "gr7", "gr8", "gr9", "nb_veh", "km_totaux"]])
		self.t = self.t.set_index(decoupage)
		for i in range(10): 		# les groupes
			lg = []		# les emissions des groupes par aire de diff
			for j in self.t.index: # les lignes
				if self.t["nb_veh"][j] == 0:
					lg.append(0)
				else:
					lg.append(self.t["km_totaux"][j] * emiss.emission[i] / self.t["nb_veh"][j]*facteur_annu/1000000000000)
			self.t["emiss{}".format(i)] = lg
		self.nb_gr = grp
		self.emissions = -1
		self.nom = nom
	
	
	def fois_facteur(self, facteur):
		# multiplie les valeurs du tableau par le facteur (utilisé pour prendre en compte la variation dans la flotte)
		for col in ["gr0", "gr1", "gr2", "gr3", "gr4", "gr5", "gr6", "gr7", "gr8", "gr9", "nb_veh", "km_totaux"]:
			self.t[col] = self.t[col] * facteur
	

	def indices(self):
		# retourne la liste des id de decoupage
		return list(self.t.index)

	def val_case(self, i, j):
		# retourne la val de la case dans le tableau, i = index, j = colonne
		return self.t[j][i]

	def emission_lgn(self, lgn):
		# retourne les emissions totales d'une ligne
		cpt = 0
		for i in range(self.nb_gr):
			cpt += self.t['gr{}'.format(i)][lgn] * self.t['emiss{}'.format(i)][lgn]
		return cpt

	def groupes(self):
		return [i for i in range(self.nb_gr)]



	def emission_tot(self, recalcule=False):
		# retourne les emissions totales de la base
		if recalcule:
			cpt = 0
			for i in self.t.index:
				cpt += self.emission_lgn(i)
			self.emissions = cpt
#			print("emissions recalculees de {} : {} Mtonnes".format(self.nom, self.emissions))
#		else:
#			print("emissions non mises a jour de {} : {} Mtonnes".format(self.nom, self.emissions))
		return self.emissions

	def max_veh(self, grp):
		# renvoie le nb max de veh pour un certain grp
		return self.t["gr{}".format(grp)].max()

	def max_veh_tot(self):
		# renvoie le nb max de veh pour tte la base
		return max([self.max_veh(i) for i in range(self.nb_gr)])


	def nb_veh_case(self, lgn, grp):
		#renvoie le nb de veh dans une case precise
		return self.t["gr{}".format(grp)][lgn]


	def diff_emiss(self, autre_table):
		# renvoie la difference d'emissions entre 2 bases a tester
		print("{} emet {} Mtonnes et {} emet {} Mtonnes, ce qui fait une difference de {}%".format(self.nom, self.emission_tot(), autre_table.nom, autre_table.emission_tot(), self.emission_tot()/autre_table.emission_tot()*100))


	def extrait_mat_veh(self):
		# renvoie la matrice des vehicules de la base
		return np.array(self.t[["gr{}".format(i) for i in range(self.nb_gr)]])


	def diff_veh(self, autre_table):
		# renvoie un tableau avec la diff des vehicules dans la base (de quoi change notre base par rapport a l'autre)
			m1 = self.extrait_mat_veh()
			m2 = autre_table.extrait_mat_veh()
			return m1 - m2

	def compte_veh_changes(self, ref):
		# entre 2 bases (celle avec laquelle on travaille et la ref), renvoie le nb de veh echanges
		veh_dep = ref.extrait_mat_veh().sum()
		trav = self.diff_veh(ref)
		i, j = len(self.t), self.nb_gr
		diff = np.maximum(trav, np.zeros((i, j))).sum()
		print("{} veh changes contre {} au depart, {} % de vehicules changes".format(diff, veh_dep, diff/veh_dep*100))
		return diff



	def remplacement(self, index, groupe_dep, groupe_arr, nb_deplac):
		#modifie la base en index donne pour qu'un certain nb de vehicules passent d'un groupe de depart a un groupe d'arrivee. Le nb de veh deplaces est limite par celui dans le grp de depart, modifie les emissions en consequence
		n = min(nb_deplac, self.nb_veh_case(index, groupe_dep))
		self.t.loc[index, 'gr{}'.format(groupe_dep)] -= n
		self.t.loc[index, 'gr{}'.format(groupe_arr)] += n
		self.emissions += n*(self.t["emiss{}".format(groupe_arr)][index] - self.t["emiss{}".format(groupe_dep)][index])

	def remplacement_tout(self, gr_d, gr_a, nb):
		# applique remplacement sur toutes les lignes
		for i in self.t.index:
			self.remplacement(i, gr_d, gr_a, nb)
		

	def prevision_diminution(self, grp, nb_veh):
		# renvoie la variation d'emission si on enleve vrmt les veh d'un grp donne
		cpt = 0
		for i in self.t.index:
			n = min(nb_veh, self.nb_veh_case(i, grp))
			cpt += self.t["emiss{}".format(grp)][i] * n
		return (cpt, self.emissions - cpt)


	def finition_objectif_naive(self, grp_d, grp_a, objectif):
		# enleve des vehicules 1 par 1 jusqu'a depasser l'objectif
		queue = [j for j in self.t.index]
		i = 0
		em = self.emission_tot(recalcule=True)
		while self.emission_tot() > objectif:
			self.remplacement(queue[i], grp_d, grp_a, 1)
			i += 1

	def charge_compo_flotte(self, nom):
		# remplace toutes les infos sur les vehicules de la base par une matrice donnee
		with open(nom, "rb") as fic:
			matrice = pk.load(fic)
		self.t.loc[[i for i in self.t.index], ["gr{}".format(i) for i in range(self.nb_gr)]] = np.array(matrice) # evite les changements par effet de bord
		self.emission_tot(recalcule=True)


	def liste_des_emissions(self):
		# renvoie la liste des emissions issue du tableau ( -> des tuple (valeur, no_de_groupe, ADIDU))
		l = []
		for i in self.t.index:
			for j in range(self.nb_gr):
				l.append((self.t["emiss{}".format(j)][i], j, i))
		return l












#"""
##########
########## Fonctions utiles
##########
"""
def calcul_ges_selon_base(base_v):
	# a partir des bases v (veh par AD deja mergé avec AD) et emiss, calcule les GES moyens émis pour chaque aire de diffusion, puis les émissions de chaque aire de diff, puis somme le tout pour donner le résultat (marche seulement avec la base AD)
	res = base_v
	e_moy = []
	for i in range(len(res)):
		som = 0
		tot = 0
		for j in range(10):
			som += res['gr{}'.format(j)].iloc[i] * emiss_par_gr.emission[j]
			tot += res['gr{}'.format(j)].iloc[i] * 1
		if tot == 0:
			print("tot = 0, som = ", som)
			e_moy.append(som/tot)
			print(e_moy[-1], '\n')
		else:
			e_moy.append(som/tot)
	res['nouv_CO2/km'] = e_moy
	res['nouv_tCO2/AD'] = res['nouv_CO2/km'] * res.km_totaux /1000000
	a = res['nouv_tCO2/AD'].sum()
	b = res['tCO2/AD'].sum()
	print("nouvelle valeur d'emission : {} (l'ancienne etait de {})\nCa nous fait une variation de {}%".format(a, b, (a/b-1)*100))





def remplacement(base_v, index, groupe_dep, groupe_arr, nb_deplac):
	#modifie la base v (vehicules) en index donne pour qu'un certain nb de vehicules passent d'un groupe de depart a un groupe d'arrivee. Le nb de veh deplaces est limite par celui dans le grp de depart, renvoie la variation dans les emissions correspondante
	n = min(nb_deplac, base_v['gr{}'.format(groupe_dep)][index])
	base_v['gr{}'.format(groupe_dep)][index] -= n
	base_v['gr{}'.format(groupe_arr)][index] += n
	return n, n*(emiss_par_gr.emission[groupe_arr] - emiss_par_gr.emission[groupe_dep])*base_v['km_totaux'][index]/base_v['nb_veh'][index]/1000000




def remplacement_selon_liste(base_v, groupe_dep, groupe_arr, liste_deplac):
	# retourne tous les veh selon la liste donnee (en fait ça va servir a faire des retours arriere), renvoie le changement de veh et d'emission correspondants
	chgmt_emiss = 0
	nb_total = 0
	for ind, nb in liste_deplac:
		n, delta = remplacement(base_v, ind, groupe_dep, groupe_arr, nb)
		if n == nb:
			chgmt_emiss += delta
			nb_total += n
		else:
			print("erreur : le nb de veh est different de celui donne au depart")
			a = input("ok ?")
	return nb_total, chgmt_emiss
	"""


def trifus1(l1, l2):
	# regroupe 2 listes triees en 1 seule
	mi = len(l1)
	mj = len(l2)
	res = []
	i, j = 0, 0
	while i < mi:
		if j < mj:
			if l1[i][0] < l2[j][0]:
				res.append(l2[j])
				j += 1
			else:
				res.append(l1[i])
				i += 1
		else:
			res = res + l1[i:]
			i = mi
	if j < mj:
		res = res + l2[j:]
	return res


def trifus(l):
	#trifusion ppale
	r = len(l)//2
	if r == 0:
		return l
	else:
		l1, l2 = l[:r], l[r:]
		return trifus1(trifus(l1), trifus(l2))
	


def trie_liste(l):
	#trie une liste de type [(elt_a_trier, ...)...]
	for i in range(len(l)):
		val = i
		for j in range(i+1, len(l)):
			if l[j][0] < l[val][0]:
				val = j
		pont = l[i]
		l[i] = l[val]
		l[val] = pont


def enreg_matrice(mat, nom):
	# enregistre la matrice au format pkl dans le dossier courant
	with open("matrices/" + nom + ".pkl", 'wb') as fic:
		pk.dump(mat, fic)
	print("matrice enregistrée comme {}.pkl\n".format(nom))



def remplit_objectif_naif(base_v, enreg):
	# calcule les emissions initiales de la base_v, puis la modifie pour avoir une reduc assez importante pour atteindre les objectifs. Les pas sont les nb de veh qu'on deplace en meme temps
	# Reduit en priorité les véhicules les plus émetteurs
	emiss_init = base_v.emission_tot(recalcule=True)
	obj = cible_emission
	print("on part de {} et on veut {} (diminution de {}%)\n".format(emiss_init, obj, (1-obj/emiss_init)*100))
	g = 9 #groupe de travail
	nb_veh = base_v.max_veh(g)
	while base_v.emission_tot() > obj:
		print("groupe {}, {} veh a changer, emissions actuelles = {} Mtonnes".format(g, nb_veh, base_v.emission_tot()))
		if nb_veh == 0:
			base_v.finition_objectif_naive(g, 0, obj)
		else:
			enleve, reste = base_v.prevision_diminution(g, nb_veh)
			if enleve == 0:
				g -= 1				# on redescend d'un grp
				nb_veh = base_v.max_veh(g)	# on recalc les veh de dep
			else:
				if reste > obj:
					base_v.remplacement_tout(g, 0, nb_veh)
				else:
					nb_veh = nb_veh // 2
	print("\n\nfin des calculs, nouvelle émission : {} Mtonnes, contre {} au départ, diminution de {} % ({}% voulu)\n\n".format(base_v.emission_tot(recalcule=True), emiss_init, (1-base_v.emission_tot()/emiss_init)*100, (1-obj/emiss_init)*100))
	enreg_matrice(base_v.extrait_mat_veh(), enreg) # enregistre les changements apportes pour pouvoir les recuperer plus tard
	


def remplit_objectif_aleat(base_v, enreg):
	# change des veh aleatoirement pour arriver a l'objectif
	# pour l'instant on vide toutes les cases
	emiss_init = base_v.emission_tot(recalcule=True)
	obj = cible_emission
	print("on part de {} et on veut {} (diminution de {}%)\n".format(emiss_init, obj, (1-obj/emiss_init)*100))
	li = base_v.indices()
	lgr = base_v.groupes()
	l = [(i, j) for i in li for j in lgr for k in range(int(base_v.nb_veh_case(i, j))+1)]
	rd.shuffle(l)
	m = base_v.max_veh_tot()
	i = 0
	while base_v.emission_tot() > obj:
		index, grp_dep = l[i]
		base_v.remplacement(index, grp_dep, 0, 1)
#		print("changé le grp {} de {}, {} % de l'objectif atteints".format(grp_dep, index, (1-base_v.emission_tot()/emiss_init)/(1-obj/emiss_init)*100))
		i += 1
	print("\n\nfin des calculs, nouvelle émission : {} Mtonnes, contre {} au départ, diminution de {} % ({}% voulu)\n\n".format(base_v.emission_tot(recalcule=True), emiss_init, (1-base_v.emission_tot()/emiss_init)*100, (1-obj/emiss_init)*100))
	enreg_matrice(base_v.extrait_mat_veh(), enreg) # enregistre les changements apportes pour pouvoir les recuperer plus tard


def remplit_objectif_optimise(base_v, enreg):
	# on vide en priorite les cases dont les emissions sont maximales (donc celles ou on a des forts km et des fortes emissions au km)
	emiss_init = base_v.emission_tot(recalcule=True)
	obj = cible_emission
	print("on part de {} et on veut {} (diminution de {}%)\n".format(emiss_init, obj, (1-obj/emiss_init)*100))
	queue = trifus(base_v.liste_des_emissions())
	i = 0 				# la progression dans la liste
	while base_v.emission_tot() > obj and i < len(queue):
		grp, ind = queue[i][1], queue[i][2]
		r = base_v.emission_tot() - obj
		print(r, "Mtonnes encore à gagner")
		g = base_v.val_case(ind, "emiss{}".format(grp))
		if g * base_v.val_case(ind, "gr{}".format(grp)) < r :
			base_v.remplacement(ind, grp, 0, base_v.val_case(ind, "gr{}".format(grp)))
		else:
			base_v.remplacement(ind, grp, 0, r//g + 1)
		i += 1
	print("\n\nfin des calculs, nouvelle émission : {} Mtonnes, contre {} au départ, diminution de {} % ({}% voulu)\n\n".format(base_v.emission_tot(recalcule=True), emiss_init, (1-base_v.emission_tot()/emiss_init)*100, (1-obj/emiss_init)*100))
	enreg_matrice(base_v.extrait_mat_veh(), enreg) # enregistre les changements apportes pour pouvoir les recuperer plus tard














#"""
##########
########## Code
##########


print("filtrage ADs dans base vehicules...")
veh = veh.merge(AD[["ADIDU"]])

#df = veh.merge(AD)


df = veh.merge(AD).merge(corres)[["Sm100", "gr0", "gr1", "gr2", "gr3", "gr4", "gr5", "gr6", "gr7", "gr8", "gr9", "nb_veh", "km_totaux"]].groupby("Sm100").sum()
df['Sm100'] = df.index

df = propre

travail = TableATester(df)#, decoupage = "ADIDU")
ref = TableATester(df)#, decoupage = "ADIDU")

#travail.fois_facteur(1.1025)
#ref.fois_facteur(1.1025)

print('fin\n')#, taille = {}\n'.format(len(vehAD)))

print("emissions totales : {} Mtonnes de CO2\n".format(travail.emission_tot(recalcule=True)))
#travail.fois_facteur(4)
#print("emissions totales : {} Mtonnes de CO2\n".format(travail.emission_tot(recalcule=True)))

remplit_objectif_optimise(travail, "USA")

travail.compte_veh_changes(ref)




#"""
##########
########## Tests
##########


#"""
