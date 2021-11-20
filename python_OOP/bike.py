""" Create 3 instances of the Bike class.

Use the __init__() method to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following methods to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods? """



class Bike:

    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayinfo(self):
        return (print(f"Price of the Bike: ${self.price}, \n Bike's maximum speed: {self.max_speed}mph, \n Mileage: {self.miles}km"))
        

    def ride(self):
        print("Riding")
        self.miles += 10
        print(self.miles)
        return self
    
    def reverse(self):
        print("Reversing")
        if self.miles >= 5:
            self.miles -= 5
            print(self.miles)
        elif self.miles >= 0 and self.miles< 5:
            self.miles = 0

        return self

firstInstance = Bike(100, 20, 0)
firstInstance.ride().ride().ride().reverse().displayinfo()

secondInstance = Bike(3000, 40, 15)
secondInstance.ride().ride().reverse().reverse().displayinfo()

#thirdInstance = Bike(500, 15, 5)
#thirdInstance.reverse().reverse().reverse().displayinfo()