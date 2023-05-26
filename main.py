import csv
from classes import Driver
from classes import Rider

#REMEMBER: People in one car are less likely to be in another
#CHECK DUES PAYING MEMBERS!!!!!!

#In order to make the form well-written for people filling it out 
#some of the dictionary keys (questions on the form) are long
#So here are some global variables to make thing shorter

#I know there's a bunch of them but it makes things easier

uniqname = "Uniqname"
name = "Name"
number = "Phone Number"
driving_this_week = "Will you be driving on at least 1 day this week?"
car_info = "Car model and color"
car_capacity = "How many people can you fit (not including yourself)?"
tues_choice = "Will you be driving or riding on Tuesday?"
tues_loc = "Where are you leaving from on Tuesday?"
thurs_choice = "Will you be driving or riding on Thursday?"
thurs_loc = "Where are you leaving from on Thursday?"
sun_choice = "Will you be driving or riding on Sunday?"
sun_loc = "Where are you leaving from on Sunday?"

#RN (maybe permanently) TO RUN PRESS CONTROL F5 WHILE IN MAIN.PY!!!!

#These lists are what people will go into 
tuesday_drivers = []
tuesday_riders = []
thursday_drivers = []
thursday_riders = []
sunday_drivers = []
sunday_riders = []

#This whole section reads in all of the responses
#and populates the above lists with all the necessary information
with open("responses.csv") as response_file:
    #reads in responses.csv as a dictionary
    responses = csv.DictReader(response_file)
    from functions import make_tuesday, make_sunday, make_thursday
    make_tuesday(tuesday_drivers, tuesday_riders, responses)
    make_thursday(thursday_drivers, thursday_riders, responses)
    make_sunday(sunday_drivers, sunday_riders, responses)

#The next step is parsing through lists to actually create carpools