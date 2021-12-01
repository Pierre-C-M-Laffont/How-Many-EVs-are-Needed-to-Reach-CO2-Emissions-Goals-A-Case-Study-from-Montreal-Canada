"""
Récupère le fichier OD de base et enregistre au format pickle dans le dossier courant, pose des filtres entre temps
Normalement seulement les chemins vers les docs et les variables uilisees sont a changer
"""

import os
import pandas as pd
import geopandas as gpd


##########
########## Chemins vers les documents
##########


path_od18 = "Fichiers_bruts/OD18_brut.pkl"


current_path = os.getcwd()



##########
########## Variables utilisees
##########


# colonnes a garder
colonnes_od18 = ["IPERE", "FEUILLET", "RANG", "NODEPLAC", "NB_JONC", "DIST", "SEQ_MODES", "XORIG", "YORIG", "LATORIG", "LONORIG", "XDEST", "YDEST", "LATDEST", "LONDEST", "XJONC", "YJONC", "LATJONC", "LONJONC"]



# Filtrage sur les lignes à prendre en compte dans notre base
def fonction_de_filtre(df, i):
	modes = df.LISTE_SEQ.iloc[i]
	return ('17' in modes and ('1' in modes or '2' in modes or '11' in modes or '12' in modes))

on_enregistre_pkl = True
nom_pkl = "outs_V2/brut_od18_multimodal.pkl"



##########
########## import od18
##########

print("import OD18...")
od18 = pd.read_pickle(path_od18)
print("importé")
print("longueur", len(od18))
print()


print("filtrage sur les colonnes")
od18 = od18[colonnes_od18]
print()
#"""




##########
########## Fonctions
##########

def rearrange(seq, current, resu):
	# liste des modes utilises
	if seq == '':
		return [current] + resu
	elif current == '':
		return rearrange(seq[:-1], seq[-1], resu)
	elif len(current) == 2:
		return rearrange(seq[:-1], seq[-1], [current] + resu)
	elif seq[-1] == " ":
		return rearrange(seq[:-2], seq[-2], [current] + resu)
	else:
		return rearrange(seq[:-1], seq[-1] + current, resu)



##########
########## Traitement
##########

print("création de la colonne des modes utilisés...")
modes = []
liste_seq = []
for i in range(len(od18)):
	trav = od18.SEQ_MODES.iloc[i]
	if type(trav) == str:
		l_s = rearrange(trav, '', [])
		liste_seq.append(l_s)
		modes.append(len(l_s))
	else :
		modes.append(0)
		liste_seq.append([])
od18["NB_MODES"] = modes
od18["LISTE_SEQ"] = liste_seq
print("fin\n")


print("colonne de filtrage en calcul...")
od18['filtre'] = [fonction_de_filtre(od18, i) for i in range(len(od18))]
print("fin\n")


print("filtrage...")
od18 = od18.query('filtre == True')
print('filtré')
print("longueur", len(od18), '\n')

print(od18.LISTE_SEQ.value_counts(), '\n')
#"""



##########
########## enregistrement
##########


if on_enregistre_pkl :
	print("enregistrement en pkl")
	od18.drop(columns = ['filtre']).to_pickle(nom_pkl)
	print("enregistré sous {}".format(nom_pkl))
#"""




### Tests
"""
jon = pd.read_csv("jonctions.csv")
print("tests sur la base initiale :")
print(len(od18.query('NB_MODES >= 2')), 'trajets avec au moins 2 modes')

print("tests sur jonctions:")
od182m = od18.query('NB_MODES >= 2')
print(od182m[["LONORIG", "LATORIG", "LONJONC", "LATJONC", "LONDEST", "LATDEST"]])
distances = []
for i in range(len(od182m)):
	seq = od182m.LISTE_SEQ.iloc[i]
	if len(seq) >= 2:
		f = od182m.FEUILLET.iloc[i]
		r = od182m.RANG.iloc[i]
		n = od182m.NODEPLAC.iloc[i]
		if not jon.query("FEUILLET == @f and RANG == @r and NODEPLAC == @n").empty:	
			print(seq)
			print(od182m.LONJONC.iloc[i])
			print(jon.query("FEUILLET == @f and RANG == @r and NODEPLAC == @n"))




print(od18_filtre.LISTE_SEQ)
print(od18_filtre.SEQ_MODES.unique())


od18_t = od18.query("AUTO == 'X' and NB_MODES == 1")
res = []
for i in range(len(od18_t)):
	if type(od18_t.SEQ_MODES.iloc[i]) == str:
		mod = rearrange(od18_t.SEQ_MODES.iloc[i], '', [])
		if od18_t.SEQ_MODES.iloc[i] not in res:
			res.append(od18_t.SEQ_MODES.iloc[i])

print("avec 1 ou 2 dans la seq :")
for x in res :
	print(x)
print("ça rpz", len(od18_t), "enregistrements")

#"""





