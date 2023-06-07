import csv
from classes import *
from functions import *

#REMEMBER: People in one car are less likely to be in another
#CHECK DUES PAYING MEMBERS!!!!!!

#RN (maybe permanently) TO RUN PRESS CONTROL F5 WHILE IN MAIN.PY!!!!

#This whole section reads in all of the responses
#and populates the above lists with all the necessary information
with open("responses.csv") as response_file:
    #reads in responses.csv as a dictionary
    responses = csv.DictReader(response_file)
    make_lists(responses)




#The next step is parsing through lists to actually create carpools
#This is done through calling functions so if there's no one to 
#drive for a given day it's easily dealt with
#This also requires another set to keep track of riders who have already
#been assigned to a car in a previous day
make_tuesday()
make_thursday()
make_sunday()