from selectors import SelectorKey


class Location:
    def __init__(self, name, country):
        self.name = name
        self.country =  country
    
    def myLocation(self):
        print("Hi, my name is "+ self.name + " and i live in "+ self.country + ".") 

loc1 = Location("Kenny", "Indonesia")
loc1.myLocation()

loc2 = Location("Kenny Rizky", "Singapore")
loc3 = Location("M.Kenny Rizky", "Malaysia")

loc2.myLocation()
loc3. myLocation()

your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()
