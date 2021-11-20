class MathDojo:
    def __init__(self):
        
        self.total = 0

    def add(self, *numbersA):
        #self.addNum = 0

        for num in numbersA:
            #self.addNum += num
            self.total += num
        #self.total = self.addNum

        return self

    def subtract(self, *numbersB):
        #self.subNum = 0

        for num in numbersB:
            #self.subNum += num
            self.total -= num
        #self.total = self.subNum
        
        return self

x = MathDojo().add(2).add(2,5,1).subtract(3,2).total
print(x)