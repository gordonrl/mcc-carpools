from classes import Driver
from classes import Rider
from collections import deque
import random

#These lists are what people will go into 
#The dues ones are only for riders on the given day
#Dues ones are sets so lookup is easy and people can easily be taken out of them
tuesday_drivers = []
tuesday_riders = []

thursday_drivers = []
thursday_riders = []

sunday_drivers = []
sunday_riders = []

#Allows easy lookup of dues paying members
dues_list = set(line.lower() and line.strip("\n") for line in open("dues.csv"))

#This is the function that will populate the lists
#It iterates through the responses and populates each list
#and set as parameters are met
def make_lists(responses):
    uniqname = "Uniqname"
    name = "Name"
    number = "Phone Number"
    driving_this_week = "Will you be driving on at least 1 day this week?"
    car_info = "Car model and color"
    car_capacity = "How many people can you fit (not including yourself)?"
    #Some local variables to make things cleaner
    tues_choice = "Will you be driving or riding on Tuesday?"
    tues_loc = "Where are you leaving from on Tuesday?"

    thurs_choice = "Will you be driving or riding on Thursday?"
    thurs_loc = "Where are you leaving from on Thursday?"

    sun_choice = "Will you be driving or riding on Sunday?"
    sun_loc = "Where are you leaving from on Sunday?"

    for person in responses:
        tues = person[tues_choice]
        thurs = person[thurs_choice]
        sun = person[sun_choice]

        #For each day this determines if the person is a rider or
        #driver and populates the corresponding list(s)
        if tues == "Driving":
            tues_driver = Driver(person[name], person[number], person[car_capacity], person[tues_loc], person[car_info], person[uniqname])
            tuesday_drivers.append(tues_driver)
        elif tues == "Riding":
            tues_rider = Rider(person[name], person[number], person[tues_loc], person[uniqname])
            tuesday_riders.append(tues_rider)
        #Tuesday Done

        #Thursday:
        if thurs == "Driving":
            thurs_driver = Driver(person[name], person[number], person[car_capacity], person[thurs_loc], person[car_info], person[uniqname])
            thursday_drivers.append(thurs_driver)
        elif thurs == "Riding":
            thurs_rider = Rider(person[name], person[number], person[thurs_loc], person[uniqname])
            thursday_riders.append(thurs_rider)
        #Done with thursday

        #Sunday:
        if sun == "Driving":
            sun_driver = Driver(person[name], person[number], person[car_capacity], person[sun_loc], person[car_info], person[uniqname])
            sunday_drivers.append(sun_driver)
        elif sun == "Riding":
            sun_rider = Rider(person[name], person[number], person[sun_loc], person[uniqname])
            sunday_riders.append(sun_rider)
        #Done with sunday


#Here's the idea for make_tuesday, make_thursday, and make_sunday:
#1. If the corresponding drivers list is empty then return and do nothing
#This still means a sheet is made but it'll just be completely empty for the day

#2. If the list of riders is empty then just write the names of the drivers and move on

#3. Finally, if there's actual assignment to do, with import random, randomly select riders
#for each driver
#If the rider doesn't pay dues and there are dues paying people yet to be selected then
#a new random person is picked, otherwise they're added to the sheet
#Once added, riders are removed from the lists so there aren't any repeats
#Location is taken into account as well don't worry!


header = ",Name,Car Type,Phone Number,Departure Time,Location,Notes\n"

#This is a new set to keep track of riders that have
#Already been put in a car at some point during the week
rode = set()

#Strings to reduce chances of typo-based bugs
central = "Central Campus (The Cube)"
north = "North Campus (Pierpont)"

#This function will actually make the Tuesday spreadsheet
#It will write tuesday.csv to be ready for uploading to Google Sheets
def make_tuesday():
    #The sheet header is always written
    with open("tuesday.csv", "w") as tuesday:
        tuesday.write("TUESDAY\n\n\n")
        #If tuesday_drivers is empty then there's no one to drive anyone
        #And nothing is added to the sheet
        if not tuesday_drivers:
            return
        #If there's no one in riders then the drivers will still be added
        #So people can add themselves after the sheet comes out
        #Because the above conditional would return it's implied that tuesday_drivers
        #isn't empty if we get to this point
        if not tuesday_riders:
            for driver in tuesday_drivers:
                #start by writing the header
                tuesday.write(header)
                #write the info of the driver (the __str__ class method makes this easy!!!!)
                tuesday.write(str(driver))
                #want to make new lines in the csv for each spot that a rider could sign up for
                for _ in range(int(driver.cap)):
                    tuesday.write("\n")
        #By the same logic commented above we know that tuedsay_riders and tuesday_drivers
        #are populated if this point is reached
        else:
            #First want to separate tues_riders list and tues_dues set into separate
            #Ones based on location
            north_riders = []
            central_riders = []
            north_dues = set()
            central_dues = set()
            for rider in tuesday_riders:
                if rider.loc == central:
                    central_riders.append(rider)
                    if rider.uniqname in dues_list:
                        central_dues.add(rider.uniqname)
                else:
                    north_riders.append(rider)
                    if rider.uniqname in dues_list:
                        north_dues.add(rider.uniqname)
            
            #Second step is the same as above conditional: Write the header then driver's info
            for driver in tuesday_drivers:
                tuesday.write(header)
                tuesday.write(str(driver))

                location = driver.loc
                #Adding riders is different because a lot of checks need to be made
                for _ in range(int(driver.cap)):
                    #The next steps are basically the same but location dependent
                    if location == central:
                        #If central_riders is empty then just write newlines and move on
                        if not central_riders:
                            tuesday.write("\n")
                            continue

                        #randint is inclusive but lists are 0-indexed so we
                        #want to go random to the size of central_riders - 1
                        index = random.randint(0, len(central_riders) - 1)
                        curr_rider = central_riders[index]

                        #need to make sure that dues paying members get priority
                        while not(curr_rider.uniqname in central_dues) and len(central_dues) != 0:
                            index = random.randint(0, len(central_riders) - 1)
                            curr_rider = central_riders[index]

                        #Curr_rider can then be added to the spreadsheet and removed from
                        #central_dues and central_riders
                        tuesday.write(str(curr_rider))
                        rode.add(curr_rider.uniqname)
                        central_riders.pop(index)
                        if curr_rider.uniqname in central_dues:
                            central_dues.remove(curr_rider.uniqname)
                    
                    #Same steps for north campus
                    else:
                        if not north_riders:
                            tuesday.write("\n")
                            continue
                        #randint is inclusive but lists are 0-indexed so we
                        #want to go random to the size of central_riders - 1
                        index = random.randint(0, len(north_riders) - 1)
                        curr_rider = north_riders[index]

                        #need to make sure that dues paying members get priority
                        while not(curr_rider.uniqname in north_dues) and len(north_dues) != 0:
                            index = random.randint(0, len(north_riders) - 1)
                            curr_rider = north_riders[index]

                        #Curr_rider can then be added to the spreadsheet and removed from
                        #central_dues and central_riders
                        tuesday.write(str(curr_rider))
                        rode.add(curr_rider.uniqname)
                        north_riders.pop(index)
                        if curr_rider.uniqname in north_dues:
                            north_dues.remove(curr_rider.uniqname)
                #Lastly a newline for spreadsheet formatting
                tuesday.write("\n\n")

#The make_thursday and make_sunday functions will basically work the same as 
#make_tuesday. The only difference really is that they also need to 
#check if people have already been put in a car previously in the week
#But for this reason there will be much less commenting

def make_thursday():
    #header
    with open("thursday.csv", "w") as thursday:
        thursday.write("THURSDAY\n\n\n")
        #check for drivers
        if not thursday_drivers:
            return
        #check for riders
        if not thursday_riders:
            for driver in thursday_drivers:
                thursday.write(header)
                thursday.write(str(driver))
                #Add lines so riders can still sign up if needed
                for _ in range(int(driver.cap)):
                    thursday.write("\n")
        #Actually populating the spreadsheet with full cars
        else:
            #Sort out thursday_riders
            #The deque only holds dues paying members
            #Those on the left have already been put in a car previously in the week
            #Those on the right (appended) have not been put in a car already
            central_dues = deque()
            central_non_dues = deque()
            north_dues = deque()
            north_non_dues = deque()
            #Randomization occurs here
            while thursday_riders:
                index = random.randint(0, len(thursday_riders) - 1)
                curr = thursday_riders[index]
                #check locations
                if curr.loc == central:
                    #check dues status
                    if curr.uniqname in dues_list:
                        #check if been in car
                        if curr.uniqname in rode:
                            central_dues.appendleft(curr)
                        else:
                            central_dues.append(curr)
                    else:
                        if curr.uniqname in rode:
                            central_non_dues.appendleft(curr)
                        else:
                            central_non_dues.append(curr)
                #same process for north campus
                else:
                    if curr.uniqname in dues_list:
                        if curr.uniqname in rode:
                            north_dues.appendleft(curr)
                        else:
                            north_dues.append(curr)
                    else:
                        if curr.uniqname in rode:
                            north_non_dues.appendleft(curr)
                        else:
                            north_non_dues.append(curr)
                #need to remove index from thursday_riders so loop isn't infinite
                thursday_riders.pop(index)

                #now just need to go iterate through thursday drivers
                #and add riders using the deques and lists made above
                for driver in thursday_drivers:
                    thursday.write(header)
                    thursday.write(str(driver))

                    location = driver.loc
                    for _ in range(int(driver.cap)):
                        #identical but location-dependent steps once again
                        if location == central:
                            if not central_dues and not central_non_dues:
                                thursday.write("\n")
                                continue
                            if central_dues:
                                curr = central_dues.pop()
                                thursday.write(str(curr))
                                rode.add(curr.uniqname)
                            else:
                                curr = central_non_dues.pop()
                                thursday.write(str(curr))
                                rode.add(curr.uniqname)
                        #same process for north campus
                        else:
                            if not north_dues and not north_non_dues:
                                thursday.writable("\n")
                                continue
                            if north_dues:
                                curr = north_dues.pop()
                                thursday.write(str(curr))
                                rode.add(curr.uniqname)
                            else:
                                curr = north_non_dues.pop()
                                thursday.write(str(curr))
                                rode.add(curr.uniqname)



            
                

