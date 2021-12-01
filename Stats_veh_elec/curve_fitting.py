import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
import pandas as pd
import random as rd

##########
########## Import et modif base
##########

qc = pd.read_csv("nvx_veh_elec_qc_propre.csv")
mtl = pd.read_csv("nvx_veh_elec_mtl.csv")

# A decocher si on veut les previsions de l'AVEQ
"""
new = pd.DataFrame({"annee":[2026, 2030], "nvx_veh_qc":[-1, -1], "cumul":[600000, 1500000]})
qc = qc.append(new)
#"""

qc['annee_ref'] = qc.annee - 2010
mtl['annee_ref'] = mtl.annee - 2010


##########
########## Fonctions à fitter
##########

def bass(t, M, p, q):
	return M*(1-np.exp(-(p+q)*t))/(1+(q/p)*np.exp(-(p+q)*t))

def bass2(t, M, p, q):
	return [M*(1-np.exp(-(p+q)*x))/(1+(q/p)*np.exp(-(p+q)*x)) for x in t]

def gomperz1(t, M, b, l):
	return M*np.exp(-b*t)*np.exp(-l*np.exp(-b*t))

"""def gomperz(t, M, b, l):
	res = []
	for x in t:
		c = 0
		for i in range(x):
			c += gomperz1(i, M, b, l)
		res.append(c)
	return np.array(c)#sum([gomperz1(i, M, b, l) for i in range(t)])"""

def gomperz(t, M, b, l):
	return np.array([sum([gomperz1(i, M, b, l) for i in range(int(x))]) for x in t])

def gomperz(t, M, b, l):
	return(M*np.exp(-np.exp(-b*(t-l))))


def logistic(t, M, A, I):
	return M/(1+np.exp(I*A)*np.exp(-A*t))

def bassM(t, p, q):
	return bass(t, 1, p, q)
def gomperzM(t, b, l):
	return gomperz(t, 1, b, l)
def logisticM(t, A, I):
	return logistic(t, 1, A, I)

##########
########## Code
##########

"""
l = []

for i in range(3):
	les_i = [rd.randrange(t) for t in range(10, 7, -1)]
	print(les_i)
	trav = qc.drop([les_i[0]])
	trav = trav.reset_index()
	trav = trav.drop([les_i[1]])
#	trav = trav.reset_index()
#	trav = trav.drop([les_i[2]]) 
	l.append(trav)
"""
l = [qc, mtl]
for i in [0, 1]:
	t = l[i]
	print(t)
	y = np.array(t.part_flotte)
	y = np.array(t.cumul)
	y2 = np.array(t.nvx_veh / t.flotte)
	x = np.array(t.annee_ref)


	params_bass, params_covariance_b = optimize.curve_fit(bass, x, y, p0=[1000000, 0.00007, 0.5], maxfev = 100000)
	params_gomperz, params_covariance_g = optimize.curve_fit(gomperz, x, y, p0=[10000000, 0.1, 20], maxfev = 1000000)
	params_logistic, params_covariance_l = optimize.curve_fit(logistic, x, y, p0=[10000000, 0.05, 0.05], maxfev = 10000)

	print(params_bass)
	#print(np.sqrt(np.diag(params_covariance_b)))
	#print(params_covariance_b)
	print()
	print(params_gomperz)
	#print(np.sqrt(np.diag(params_covariance_g)))
	print()
	print(params_logistic)
	#print(np.sqrt(np.diag(params_covariance_l)))
	print()

	# les courbes resultantes
	plt.figure()
	x2 = np.linspace(0, 90, 90)
	y2 = bass(x2, params_bass[0], params_bass[1], params_bass[2])
	y3 = gomperz(x2, params_gomperz[0], params_gomperz[1], params_gomperz[2])
	#y3 = gomperz(x2, 2000000, 20, 0.1)
	y4 = logistic(x2, params_logistic[0], params_logistic[1], params_logistic[2])
	plt.plot(x2, y2, label='Bass')
	#plt.plot(x2, y3, label = "Gompertz")
	plt.plot(x2, y4, label="Logistique")
	plt.plot(x, y, 'r+', label="données")
	plt.xticks([20*i for i in range(5)], [20*i + 2010 for i in range(5)])
	plt.yticks([500000000*i for i in range(7)], ["{}".format(i/2) for i in range(7)])
	plt.xlabel("année")
	plt.ylabel("nombre de VE (en milliards)")
	#plt.xlim(0, 20)
	#plt.ylim(0, 1600000)
	if i == 0:
		plt.plot(16, 0.1124, 'bo', label="objectif de l'AVEQ") #0.1124 ou 600000
		plt.plot(20, 0.2688, 'bv', label="objectif provincial") #0.2688 ou 1500000
		plt.plot(19, 0.11, 'bs', label="estimation d'Hydro-Québec")
	plt.legend()
	print("pour les données 2030 de {}, Bass = {}, Gompertz = {}, Logistic = {}".format(i, bass(20, params_bass[0], params_bass[1], params_bass[2]), gomperz(20, params_gomperz[0], params_gomperz[1], params_gomperz[2]), logistic(20, params_logistic[0], params_logistic[1], params_logistic[2])))
plt.show()




"""
print(bass(20, params_bass[0], params_bass[1], params_bass[2]))
print(gomperz([20], params_gomperz[0], params_gomperz[1], params_gomperz[2])[0])
print(logistic(20, params_logistic[0], params_logistic[1], params_logistic[2]))

#"""
