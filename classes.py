#The driver class stores important information about drivers such as car capacity and location
#The __str__() function is hugely useful because it allows us to print out all of the driver's
#information for the spreadsheet in the proper csv format!!!! Python is sick
class Driver:
    #Constructor
    def __init__(self, name, number, capacity, location, car_info, uniq):
        self.name = name
        self.num = number
        self.cap = capacity
        self.loc = location
        #car_info = color and model
        self.info = car_info
        self.uniqname = uniq.lower()

        #This starts as False but will be changed to true for Sunday
        self.sunday = False
    
    #This will change when I know what I'm doing more
    #The hope is that this will be able to let me output everything needed for the driver in nice pretty csv format
    def __str__(self):
        if not self.sunday:
            return f"Driver,{self.name},{self.info},{self.num},6:45,{self.loc},"
        else:
            return f"Driver{self.name},{self.info},{self.num},9:45,{self.loc},"
    

#The rider class is very similar to the driver class in that it's just storing useful information
#Such as whether or not they're dues paying and their location
#The __str()__ function will hopefully work the same as with the driver class
class Rider:
    #constructor
    def __init__(self, name, number, location, uniq):
        self.name = name
        self.num = number
        self.loc = location
        self.uniqname = uniq
    
    #Just like Driver this will hopefully be changed to print out everything 
    #in pretty csv format to make this program nice and modular
    def __str__(self):
        return f"\nRider,{self.name},,{self.num},,{self.loc}"

    