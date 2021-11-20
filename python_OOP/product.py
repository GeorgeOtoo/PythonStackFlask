class Product:

    def __init__(self, price, item_Name, weight, brand, status):
        self.price = price
        self.item_Name = item_Name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_Tax(self, tax=0.10):
        toBeAdded = self.price * tax
        self.price = self.price + toBeAdded
        return self 

    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            discount = 0.20 * self.price
            self.price = self.price - discount

        return self

    def displayInfo(self):
        print("The item you want is " + self.item_Name)
        print(f"The brand name is {self.brand}")
        print(f"The weight of the {self.item_Name} is : ", self.weight)
        print(f"This {self.item_Name} is currently {self.status}")
        print(f"The price of the {self.item_Name} is: ${self.price}")
        
        #print("Price after tax is: ", d)



c = Product(100, 'shirt', '5lbs', 'H&M', 'for sale')
#c.add_Tax().displayInfo()
c.return_item("opened").add_Tax().displayInfo()

