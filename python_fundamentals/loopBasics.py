# Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5]

""" def makeItBig(num):
    for i,val in enumerate(num): #i is the index and val is the value at the index
        print("i is: "  ,i , " val is: "  ,val)
        if val < 0:
            num[i] = "big"    
    return num

print(makeItBig([-1, 3, 5, -5])) """

# Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

""" def countPositives(num):
    count = 0
    for i in num:
        if i > 0:
            count = count + 1
    
    x = len(num)
    num[x-1] = count
    return num

print(countPositives([-1,1,1,1,6,-2,7])) """

#  Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

""" def sumTotal(num):
    sum = 0
    for i in num:
        sum = sum + i

    return sum 

print(sumTotal([1,2,3,4])) """

# Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

""" def multiples(num):
    sum = 0
    for i in num:
        sum = sum + i

    return sum / len(num)

print(multiples([1,2,3,4,6,8])) """

# Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

""" def length(num):

    return len(num)

print(length([1,2,3,4])) """

# Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

""" def minimum(num):
    if len(num) < 1:
        return false
    
    x = num[0]
    i = 1
    for i in num:
        #print(i)
        if i < x:
            x = i

    return x

print(minimum([7,2,3,4])) """

# Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

""" def minimum(num):
    if len(num) < 1:
        return false
    
    x = num[0]
    i = 1
    for i in num:
        #print(i)
        if i > x:
            x = i

    return x

print(minimum([7,2,18,4])) """

# Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
""" 
def findDict(num):

    sumTotal = 0
    average = 0
    minimum = num[0]
    maximum = num[0]
    lengthNum = len(num)
    numInfo = {}

    i = 1
    for i in num:
        #print(i)
        sumTotal = sumTotal + i

        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i
    
    average = sumTotal / lengthNum
    numInfo.update({"Sum": sumTotal,
                    "Average": average,
                    "Minimum": minimum,
                    "Maximum": maximum, 
                    "Length_of_Array": lengthNum
                    })

    return numInfo


print(findDict([7,2,18,4])) """

# Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

""" def reverse(num):
    startLeft = 0
    startRight = len(num) - 1

    while startLeft < startRight:
        temp = num[startLeft]
        num[startLeft] = num[startRight]
        num[startRight] = temp

        startLeft = startLeft + 1
        startRight = startRight - 1
    
    return num

print(reverse([1,2,3,4])) """

""" x = "Caleb"
y = "asare"
#print("my name is " + x + y + " last name")

# String Interpolation
print(f"My name is {x} and my Father's Last Name is {y}") """

# Aacessing list and Tuples

list = [99,4,2,5,-3]
tuple = [99,4,2,5,-3]

print(list[:4])
print(list[1:4])
