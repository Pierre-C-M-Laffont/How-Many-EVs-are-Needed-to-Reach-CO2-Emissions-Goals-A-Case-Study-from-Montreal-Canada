import pandas as pd

########## Variables

fic_2018 = "veh_par_SM.csv"
fic_2030 = "../flotte_2030/flotte2030.csv"
nom_enreg = "veh_par_SM_2030.csv"


########## Imports

f18 = pd.read_csv(fic_2018)[["Sm100", "nb_veh", "km_totaux"]]
f30 = pd.read_csv(fic_2030)

########## Code

print(f18)
print(f30)

res30 = f30.merge(f18)

res30["tot30"] = sum([res30["gr{}".format(i)] for i in range(10)])#res30.apply(lambda x : 

res30["km_totaux"] = res30.km_totaux * res30.tot30 / res30.nb_veh

res30["nb_veh"] = res30.tot30

res30 = res30.drop(columns=["tot30"])

print(res30)
print(res30.describe())

res30.to_csv(nom_enreg)
