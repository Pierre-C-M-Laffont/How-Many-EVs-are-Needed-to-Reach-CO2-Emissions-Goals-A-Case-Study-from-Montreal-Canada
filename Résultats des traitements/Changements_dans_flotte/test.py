import pickle as pkl
import numpy as np

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

with open("nene.pkl", 'wb') as fic:
	pkl.dump(m, fic)

print("done")
