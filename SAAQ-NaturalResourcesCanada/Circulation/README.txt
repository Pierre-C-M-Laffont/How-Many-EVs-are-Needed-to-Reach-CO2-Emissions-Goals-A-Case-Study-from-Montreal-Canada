This folder contains the code used to modify the SAAQ database.





correspondances.py :
	Functions used to add emissions values to each vehicle. It may need some
	functions or variables from "../outils.py"


echantillon :
	Binary file, can be read using "pickle" module in Python. Contains only
	a small part of the data.


echantillon_tri :
	Same file as "echantillon". Vehicles in this file are sorted following
	their age, make, model, number of cylinders, engine size


historique des transfos :
	History of the modifications dont to the database. May not be complete.


Resu_moyennes :
	Average emissions of vehicles of the database for each year, make,
	taking into account the vehicles whose year, make and model were
	available in the SAAQ database.


tests_circul.py :
	Some test functions


transfo_base.py :
	Functions used to modify the database before assigning the vehicles
	their emissions values with "correspondances.py".


tri_circul.py :
	Functions used to sort vehicles in the database. Also used to sort
	"echantillon_tri"
