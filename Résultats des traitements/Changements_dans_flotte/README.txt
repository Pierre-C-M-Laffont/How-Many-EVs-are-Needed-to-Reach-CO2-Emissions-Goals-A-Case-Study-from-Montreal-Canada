matrices/ :
	binary files containing the tables depicting the fleet after the
	simulations. Can be read with pickle in python.

resus/ :
	Results of simulations
	aleat -> random replacement
	optimise -> optimistic scenario
	optimise_inverse -> pessimistic scenario
	naif -> efficient scenario
	naif_inverse -> inefficient scenario


veh_par_SM.csv :
	Number of km travelled and number of vehicles in each municipal sector
	in 2018.


veh_par_SM_2030.csv :
	Same as above, but for 2030.





Important features of the result files (obtained with the script n°0) ("resus"
folder) :


l7, "emissions totales : " -> Hypothetical current emissions with the fleet and
emission values used.

l9, "on part de A et on veut B (diminution de C%)" -> we start with A MtonnesCO2,
we want to reach B Mtonnes. C is the rate of decrease.


last line, "D veh changes contre E au depart, F % de vehicules changes" -> D
vehicles were replaced with electric ones. E is the total number of vehicles. F
is the percentage of vehicles changed.
