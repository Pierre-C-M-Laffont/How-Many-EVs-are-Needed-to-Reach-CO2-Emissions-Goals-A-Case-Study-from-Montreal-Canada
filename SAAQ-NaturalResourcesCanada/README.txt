Here are some general scripts, documents and results of the part of the
research concerning the SAAQ and Naturan Resources Canada databases.

/!\ The code on this part of the research is not well written. Only some
functions have been coded and the modifications were done typing instructions
directly on the terminal. It would be better to restart from scratch to get a
proper history of the modifications done.




Circulation/ :
	All scripts & files related to the circulation database (SAAQ).

Emission/ :
	All scripts & files related to the emission database (Natural Resources
	Candada).

Estimation_evolution/ :
	Scripts used to predict the future composition of the fleet.

Separateurs/ :
	Scripts & files related to the k-mean clustering method.





%age d'écart en émission meme modele mais cylindree différent.png :
	might be a graph representing the difference in emissions between
	vehicles with the same year-make-model but without the same engine
	size. 1500 vehicles have a difference lower than 20%, and the rest
	have a difference in emission higher than 20%. The higher difference in
	emissions is +120%.


description_emiss_2018.csv :
	Table used in the master thesis (to be opened as text, and use with
	LaTex)


diagramme d'émission des véhicules corresp exacte.png :
	Distribution of emissions of vehicles in the region of Quebec. Only
	circulating vehicles with a match in the emission database are taken
	into account in this graph.


division_grosse_base.py :
	Script used to divide the big database with vehicles in circulation in
	smaller files.


emissions moyennes par année.ods :
	Linear regression for average emissions per year



emissions moyennes par annee pour les matchs parfaits seulement.png :
	Results of linear regression for average emissions per year for
	vehicles in circulation with a match in the emission database.


export.py :
	Might be a script used to return the boundaries of the groups formed by
	the k-mean clustering method.


outils.py :
	Tools used by other scripts in this folder.


reglin.pdf :
	Result of the linear regression.


Renommage des bases.mm :
	Some notes... Can be read using the software Freeplane.


repart1.pdf & repart2.pdf :
	Distribution of vehicles in circulation and emission category
	boundaries.


travail_base.py :
	Script containing the functions used to modify the database of vehicles
	in circulation.


travil réalisé.txt :
	Notes describing the modifications done to the database. May not be
	complete.


vehicules_et_emissions.csv & vehicules_et_emissions_2018.csv :
	Final files with all vehicles in circulation and their emission values.


vehicules_et_emissions_2018_10gr_dont_elec.csv :
	Same as above, with a column in which is given the corresponding
	emission category.


vehicules_et_emissions_2018_10groupes.ods :
	File sent to the SAAQ in order to obtain the table used in the rest of
	the research, with the number of vehicles in each category in each
	dissemination area.



