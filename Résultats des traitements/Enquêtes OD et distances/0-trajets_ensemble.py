import pandas as pd


od = pd.read_pickle('outs_V2/calculé_od18_complet_AD.pkl')

print(od.dist_tot.sum())
