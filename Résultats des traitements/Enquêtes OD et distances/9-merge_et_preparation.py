"""
Merge toutes les bases qui seront utiles pour plus tard (les distances, les AD, les colonnes manqantes depuis l'OD18), renvoie des stats de taux d'occupation aussi

"""


import pandas as pd



##########
########## Variables utilisees
##########


dossier = "outs_V2/"
nom_od = "calculé_od18_completV3.pkl"

nom_od_brut = "Fichiers_bruts/OD18_brut.pkl"

nom_AD = 'outs_V2/SM_des_deplac.pkl'

enreg = True
nom_enreg = "outs_V2/calculé_od18_completV4_SM.pkl"



##########
########## Import bases de donnees
##########

print("import donnees...")
od18 = pd.read_pickle(dossier + nom_od)
AD = pd.read_pickle(nom_AD)
taux_occ = pd.read_pickle(nom_od_brut)[['IPERE', 'PERS_AUTO', 'FACLOG', 'PERSLOGI']]
print("importé\n")


##########
########## Calculs
##########

print(od18.columns)
print(taux_occ.columns)

print("debut_merge sur ipere")
od18 = od18.merge(taux_occ).merge(AD)
print("fin\n")

print(od18.columns)

conducs = od18.query("SEQ_MODES == '1' and PERS_AUTO != 0")
passagers = od18.query("SEQ_MODES == '2' and PERS_AUTO != 0")

print("valeurs pour conduc\n", conducs.PERS_AUTO.value_counts())
print("moyenne :", conducs.PERS_AUTO.mean())
print("valeurs pour passagers :\n", passagers.PERS_AUTO.value_counts())
print("moyenne :", passagers.PERS_AUTO.mean())

if enreg:
	print("enregistrement...")
	od18.to_pickle(nom_enreg)
	print("enregistré sous {}".format(nom_enreg))
