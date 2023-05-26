#The driver class stores important information about drivers such as car capacity and location
#The __str__() function is hugely useful because it allows us to print out all of the driver's
#information for the spreadsheet in the proper csv format!!!! Python is sick
class Driver:
    #Constructor
    def __init__(self, name, number, capacity, location, car_info):
        self.name = name
        self.num = number
        self.cap = capacity
        self.loc = location
        #car_info = color and model
        self.info = car_info
        #These are only used if the driver is also riding at least
        #one day in the week
        #This seems unlikely but I wanted it to be an option
        self.dues = True
        self.in_car = False
    
    #This will change when I know what I'm doing more
    #The hope is that this will be able to let me output everything needed for the driver in nice pretty csv format
    def __str__(self):
        return f"{self.name}"
    

#The rider class is very similar to the driver class in that it's just storing useful information
#Such as whether or not they're dues paying and if they've already been in a car during the week
#The __str()__ function will hopefully work the same as with the driver class
class Rider:
    def __init__(self, name, number, location):
        self.name = name
        self.num = number
        self.loc = location
        #Whether or not they've been in a car is false by default
        self.in_car = False
        #Dues paying will be True by default and made False when the dues paying members
        #File is ready in
        self.dues = True
    
    #Just like Driver this will hopefully be changed to print out everything 
    #in pretty csv format to make this program nice and modular
    def __str__(self):
        return f"{self.name}"

    