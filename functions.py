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
dues_list = set()
#This goes through the list of dues paying members and adds them to the dues_list set
#The format of the file has newlines at the end of every uniqname and some are entered
#with capitalization so this also makes everything lowercase and removes the newline character
with open("dues.csv") as dues:
    while True:
        line = dues.readline()
        if not line:
            break
        
        line = line.strip("\n")
        line = line.lower()
        if line == "jeshah":
            line = "jesha"
        dues_list.add(line)
        

#This is the function that will populate the lists
#It iterates through the responses and populates each list
#and set as parameters are met
def make_lists(responses):
    uniqname = "Uniqname"
    name = "Name"
    number = "Phone Number"
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

#This is so we don't need to type out the header over and over again
header = ",Name,Car Type,Phone Number,Departure Time,Location,Notes\n"

#This is a new set to keep track of riders that have
#Already been put in a car at some point during the week
rode = set()

#Strings to reduce chances of typo-based bugs
central = "Central Campus (The Cube)"
north = "North Campus (Pierpont)"

#This function will actually make the Tuesday spreadsheet
#It will create and write tuesday.csv to be ready for uploading to Google Sheets
def make_tuesday():
    #The tuesday.csv file will be open for the whole function
    with open("tuesday.csv", "x") as tuesday:
        #No matter what the sheet header has to be written
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
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                #start by writing the header
                tuesday.write(header)
                #write the info of the driver (the __str__ class method makes this easy!!!!)
                tuesday.write(str(driver))
                #want to make new lines in the csv for each spot that a rider could sign up for
                for _ in range(int(driver.cap)):
                    tuesday.write("\nRider,")
                tuesday.write("\n\n")
        #By the same logic commented above we know that tuedsay_riders and tuesday_drivers
        #are populated if this point is reached
        else:
            #Riders can be easily sorted using deques (double-ended queues)
            #Riders will be randomly pulled from the tuesday_riders list
            #If they pay dues then they're added to the right of the deque
            #If they don't pay dues then they're added to the left of it
            #Then riders are selected going right to left, thus selecting the dues paying members first
            #Two deques are needed -- one for north campus and one for central campus
            central_riders = deque()
            north_riders = deque()
            while tuesday_riders:
                #length is minus one because randint is inclusive but lists are zero-indexed
                index = random.randint(0, len(tuesday_riders) - 1)
                curr = tuesday_riders[index]
                #Locations need to be checked to populate the correct deque
                if curr.loc == central:
                    #first dues paying is checked
                    #If they're paying dues they go on the right of the deque, otherwise they go on the left
                    if curr.uniqname in dues_list:
                        central_riders.append(curr)
                    else:
                        central_riders.appendleft(curr)
                #Same for north campus
                elif curr.loc == north:
                    if curr.uniqname in dues_list:
                        north_riders.append(curr)
                    else:
                        north_riders.appendleft(curr)
                #Last the current rider needs to be removed from tuesday_riders because
                #They've already been dealt with in terms of organization
                tuesday_riders.pop(index)
            #Now we just need to iterate through the drivers and add riders using the 
            #deques that were just created
            for driver in tuesday_drivers:
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                #This writes the info for the top of each new car in the spreadsheet
                tuesday.write(header)
                tuesday.write(str(driver))
                #need to know the location of the driver we're on then we just iterate 
                #through the capacity of the current driver's car, adding riders as we go
                location = driver.loc
                #These next steps are identical but we need to write them twice because
                #The location changes
                if location == central:
                    for _ in range(int(driver.cap)):
                        #If there are no riders left then just print a newline and continue
                        #So the space is available for randos once the carpools are released
                        if not central_riders:
                            tuesday.write("\nRider,")
                            continue
                        else:
                            #pop() is nice because it removes the rider and returns it
                            #so two steps in one
                            curr = central_riders.pop()
                            #__str__() makes writing the riders incredibly easy too
                            tuesday.write(str(curr))
                            #Also need to keep track of the riders who have been put into a car
                            #This is what the rode set made above the make functions is for
                            rode.add(curr.uniqname)
                #same process for north campus
                elif location == north:
                    for _ in range(int(driver.cap)):
                        if not north_riders:
                            tuesday.write("\nRider,")
                            continue
                        else:
                            curr = north_riders.pop()
                            tuesday.write(str(curr))
                            rode.add(curr.uniqname)
                #Two newlines are written after the car is made to make things a little easier
                #When uploading and editing the spreadsheet once it's in Google Sheets
                tuesday.write("\n\n")

        
#The make_thursday and make_sunday functions will basically work the same as 
#make_tuesday. The only difference really is that they also need to 
#check if people have already been put in a car previously in the week
#But for this reason there will be much less commenting

def make_thursday():
    #header
    with open("thursday.csv", "x") as thursday:
        thursday.write("THURSDAY\n\n\n")
        #check for drivers
        if not thursday_drivers:
            return
        #check for riders
        if not thursday_riders:
            for driver in thursday_drivers:
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                thursday.write(header)
                thursday.write(str(driver))
                #Add lines so riders can still sign up if needed
                for _ in range(int(driver.cap)):
                    thursday.write("\nRider,")
                thursday.write("\n\n")
        #Actually populating the spreadsheet with full cars
        else:
            #These deques work the same way as for tuesday
            #The only difference (this will be present for Sunday too)
            #Is that we need to separate dues paying members and non-dues paying members into two different deques
            #This is because dues paying members still get priority over non-dues paying members even if
            #they've already been in a car previously
            #So the left side of the deques is now for people who have been in cars before in the weel
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
                elif curr.loc == north:
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
            #and add riders using the deques made above
            for driver in thursday_drivers:
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                thursday.write(header)
                thursday.write(str(driver))

                location = driver.loc
                #identical but location-dependent steps once again
                if location == central:
                    for _ in range(int(driver.cap)):
                        if not central_dues and not central_non_dues:
                            thursday.write("\nRider,")
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
                elif location == north:
                    for _ in range(int(driver.cap)):
                        if not north_dues and not north_non_dues:
                            thursday.write("\nRider,")
                            continue
                        if north_dues:
                            curr = north_dues.pop()
                            thursday.write(str(curr))
                            rode.add(curr.uniqname)
                        else:
                            curr = north_non_dues.pop()
                            thursday.write(str(curr))
                            rode.add(curr.uniqname)
                thursday.write("\n\n")

#make_sunday only has one difference from make_thursday
#and that's that the sunday attribute of each driver needs to 
#be changed to true so the correct time is written on the spreadsheet
def make_sunday():
    with open("sunday.csv", "x") as sunday:
        sunday.write("SUNDAY\n\n\n")
        #check for drivers
        if not sunday_drivers:
            return
        #check for riders
        if not sunday_riders:
            for driver in sunday_drivers:
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                sunday.write(header)
                #Need to make the driver's sunday attribute True so the correct time is printed
                #See classes.py for more info
                driver.sunday = True
                sunday.write(str(driver))
                #Lines for capacity
                for _ in range(int(driver.cap)):
                    sunday.write("\nRider,")
                sunday.write('\n\n')
        #Actually crete cars otherwise
        else:
            central_dues = deque()
            central_non_dues = deque()
            north_dues = deque()
            north_non_dues = deque()
            #randomization
            while sunday_riders:
                index = random.randint(0, len(sunday_riders) - 1)
                curr = sunday_riders[index]
                #check locations and dues paying
                if curr.loc == central:
                    if curr.uniqname in dues_list:
                        if curr.uniqname in rode:
                            central_dues.appendleft(curr)
                        else:
                            central_dues.append(curr)
                    else:
                        if curr.uniqname in rode:
                            central_non_dues.appendleft(curr)
                        else:
                            central_non_dues.append(curr)
                elif curr.loc == north:
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
                sunday_riders.pop(index)

            #iterate through drivers and populate cars
            for driver in sunday_drivers:
                #If driver was made by mistake
                if driver.cap == 0 or driver.loc == "Not Going":
                    continue
                sunday.write(header)
                driver.sunday = True
                sunday.write(str(driver))
                location = driver.loc
                
                if location == central:
                    #Don't need to add riders to rode because sunday is the last day
                    for _ in range(int(driver.cap)):
                        if not central_dues and not central_non_dues:
                            sunday.write("\nRider,")
                            continue
                        if central_dues:
                            curr = central_dues.pop()
                            sunday.write(str(curr))
                        else:
                            curr = central_non_dues.pop()
                            sunday.write(str(curr))
                #Same for north campus
                elif location == north:
                    for _ in range(int(driver.cap)):
                        if not north_dues and not north_non_dues:
                            sunday.write("\nRider,")
                            continue
                        if north_dues:
                            curr = north_dues.pop()
                            sunday.write(str(curr))
                        else:
                            curr = north_non_dues.pop()
                            sunday.write(str(curr))
                sunday.write("\n\n")

