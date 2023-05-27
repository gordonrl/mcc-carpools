from classes import Driver
from classes import Rider

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

#This makes the list of dues members a set so names can easily be checked
#also makes the uniqnames lowercase to reduce the chances of someone being 
#incorrectly marked as not in the list
dues_list = set(line.strip() and line.lower() for line in open("dues.csv"))

#These are functions that are used in main
#This function populates the tuesday_drivers and tuesday_riders list
def make_tuesday(tuesday_drivers, tuesday_riders, responses):
    tues_choice = "Will you be driving or riding on Tuesday?"
    tues_loc = "Where are you leaving from on Tuesday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[tues_choice]
        if choice == "I'm not going on Tuesday":
            continue
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[tues_loc], person[car_info])
            tuesday_drivers.append(new_driver)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_driver.dues = False
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[tues_loc])
            tuesday_riders.append(new_rider)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_rider.dues = False

#Populates Thursday lists
def make_thursday(thursday_drivers, thursday_riders, responses):
    thurs_choice = "Will you be driving or riding on Thursday?"
    thurs_loc = "Where are you leaving from on Thursday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[thurs_choice]
        if choice == "I'm not going on Thursday":
            continue
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[thurs_loc], person[car_info])
            thursday_drivers.append(new_driver)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_driver.dues = False
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[thurs_loc])
            thursday_riders.append(new_rider)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_rider.dues = False

#Populates Sunday Lists
def make_sunday(sunday_drivers, sunday_riders, responses):
    sun_choice = "Will you be driving or riding on Sunday?"
    sun_loc = "Where are you leaving from on Sunday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[sun_choice]
        if choice == "I'm not going on Tuesday":
            continue
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[sun_loc], person[car_info])
            sunday_drivers.append(new_driver)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_driver.dues = False
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[sun_loc])
            sunday_riders.append(new_rider)
            #checks if they pay dues
            if not (person[uniqname].lower() in dues_list):
                new_rider.dues = False

