from classes import Driver
from classes import Rider

#In order to make the form well-written for people filling it out 
#some of the dictionary keys (questions on the form) are long
#So here are some global variables to make thing shorter

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
def make_tuesday_lists(tuesday_drivers, tuesday_riders, tues_dues, responses):
    tues_choice = "Will you be driving or riding on Tuesday?"
    tues_loc = "Where are you leaving from on Tuesday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[tues_choice]
        #Skips person if they're not going on tuesday
        if choice == "I'm not going on Tuesday":
            continue
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[tues_loc], person[car_info])
            tuesday_drivers.append(new_driver)
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[tues_loc])
            tuesday_riders.append(new_rider)
            #checks if they pay dues
            if (person[uniqname].lower() in dues_list):
                tues_dues.add(person[uniqname])

#Populates Thursday lists
def make_thursday_lists(thursday_drivers, thursday_riders, thurs_dues, responses):
    thurs_choice = "Will you be driving or riding on Thursday?"
    thurs_loc = "Where are you leaving from on Thursday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[thurs_choice]
        #Skips person if they're not going on Thursday
        if choice == "I'm not going on Thursday":
            continue
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[thurs_loc], person[car_info])
            thursday_drivers.append(new_driver)
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[thurs_loc])
            thursday_riders.append(new_rider)
            #checks if they pay dues
            if (person[uniqname].lower() in dues_list):
                thurs_dues.add(person[uniqname])

#Populates Sunday Lists
def make_sunday_lists(sunday_drivers, sunday_riders, sun_dues, responses):
    sun_choice = "Will you be driving or riding on Sunday?"
    sun_loc = "Where are you leaving from on Sunday?"
    for person in responses:
        #Determines if person is a rider or driver and makes correct class
        choice = person[sun_choice]
        #Skips person if they're not going on Sunday
        if choice == "I'm not going on Sunday":
            continue
        #Makes person a driver if they say they're driving
        elif choice == "Driving":
            new_driver = Driver(person[name], person[number], person[car_capacity], person[sun_loc], person[car_info])
            sunday_drivers.append(new_driver)
                
        #otherwise they're a rider
        else:
            new_rider = Rider(person[name], person[number], person[sun_loc])
            sunday_riders.append(new_rider)
            #checks if they pay dues
            if (person[uniqname].lower() in dues_list):
                sun_dues.add(person[uniqname])


#This function will actually make the Tuesday spreadsheet
#It will write tuesday.csv to be ready for uploading to Google Sheets
def make_tuesday(tuesday_drivers, tuesday_riders):
    #If tuesday_drivers is empty then there's no one to drive anyone
    if not tuesday_drivers:
        return
    

    #If tuesday_riders is empty we still want to write each driver
    #in tuesday_drivers to the csv in case riders sign up at a later point

