class Animal:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(f"The health is: {self.health}")

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
        def __init__(self, name, health):
            super().__init__(name, health)
            self.health = 170

        def fly(self):
            self.health -= 10
            return self

        def display_health(self):
            Animal.display_health(self)
            print("I am a Dragon")
            return self



# animal1 = Animal("cat", 100)
# animal1.walk().walk().walk().run().run().display_health()

# myPet = Dog("Shake", 70)
# myPet.walk().walk().walk().run().run().display_health()

# diagonali = Dragon("harry", 5)
# diagonali.fly().display_health()

# test = Animal("test", 40)
# test.display_health()

test = Dog("test", 40)
test.fly()

