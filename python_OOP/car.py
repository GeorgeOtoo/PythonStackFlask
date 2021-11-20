""" Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined. """

class Car:

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print("Price: $" + str(self.price))
        print("Speed: " ,self.speed ,"mph")
        print("Fuel: "  ,self.fuel)
        print("Mileage: " ,self.mileage ,"km")
        x = 0.12
        y = 0.15
        #y if self.price > 10000 else x 
        print("Tax: " ,(y if self.price > 10000 else x ))
        return self

yourCar = Car(20000, 35, 'full' , 4520)
yourCar.display_all()

