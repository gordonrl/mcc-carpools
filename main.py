import csv
from classes import *
from functions import *

#REMEMBER: People in one car are less likely to be in another
#CHECK DUES PAYING MEMBERS!!!!!!

#RN (maybe permanently) TO RUN PRESS CONTROL F5 WHILE IN MAIN.PY!!!!

#These lists are what people will go into 
#The dues ones are only for riders on the given day
#Dues ones are sets so lookup is easy and people can easily be taken out of them
tuesday_drivers = []
tuesday_riders = []
tues_dues = set()

thursday_drivers = []
thursday_riders = []
thurs_dues = set()

sunday_drivers = []
sunday_riders = []
sun_dues = set()

#This whole section reads in all of the responses
#and populates the above lists with all the necessary information
with open("responses.csv") as response_file:
    #reads in responses.csv as a dictionary
    responses = csv.DictReader(response_file)
    make_tuesday_lists(tuesday_drivers, tuesday_riders, tues_dues, responses)
    make_thursday_lists(thursday_drivers, thursday_riders, thurs_dues, responses)
    make_sunday_lists(sunday_drivers, sunday_riders, sun_dues, responses)

#The next step is parsing through lists to actually create carpools
#This is done through calling functions so if there's no one to 
#drive for a given day it's easily dealt with