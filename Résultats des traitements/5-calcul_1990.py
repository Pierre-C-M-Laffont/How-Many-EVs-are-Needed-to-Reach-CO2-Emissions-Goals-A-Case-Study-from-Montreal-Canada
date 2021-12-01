"""
Juste un truc où rentrer toutes les valeurs initiales et qui sort les émissions de 1990 correspondantes et tout le reste
"""

# variables de base
taux_diminution = 37.5



# les valeurs de 2018
emiss_mtl18 = 5.5244#5.524 #initial
emiss_qc18 = 9.23 + 8.98
pop_mtl18 = 4208809.4
pop_qc18 = 8401738


#les valeurs de 1990
emiss_qc90 = 10.86 + 3.64
pop_mtl90 = 3086065
pop_qc90 = 6996986


# resultats
alpha = (emiss_mtl18 / pop_mtl18) / ((emiss_qc18 - emiss_mtl18) / (pop_qc18 - pop_mtl18))
em90 = (alpha * emiss_qc90 * pop_mtl90) / ((pop_qc90 - pop_mtl90) + (alpha * pop_mtl90))
em30 = em90 * (1 - (taux_diminution/100))


print("facteur alpha : {}\nemissions 1990 : {} Mtonnes\nemissions 2030 : {} Mtonnes".format(alpha, em90, em30))
