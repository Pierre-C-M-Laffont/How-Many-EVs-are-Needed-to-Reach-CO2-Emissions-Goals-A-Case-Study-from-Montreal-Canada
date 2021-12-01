import pandas as pd
import matplotlib.pyplot as plt

fic_flotte = "prevision_SAAQ.csv"
fic_pop = "population_2030.csv"
fic_poss = "possession_auto.csv"


pop = pd.read_csv(fic_pop).set_index("annee")
poss = pd.read_csv(fic_poss).set_index("ANNEE")
flotte = pd.read_csv(fic_flotte)
flotte.index = flotte.an
flotte = flotte.drop(columns=["an"])
print(flotte)

#pop
pop = pop['pop'][2030]

# nb d'autos
autos = pop * poss['TOTAL'][2030]


#flotte.loc[2018].plot.bar()
plt.bar(flotte[["gr{}".format(i) for i in range(10)]].columns, flotte.loc[2018, ["gr{}".format(i) for i in range(10)]]*autos)
plt.xlabel("group of emission")
plt.ylabel("number of vehicles")
plt.ylim(0, 1000000)
plt.show()
