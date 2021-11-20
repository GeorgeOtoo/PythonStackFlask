# Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

""" def countDown(num):
    less = []
    for i in range(num, -1, -1):
        less.append(i)
    return less

print(countDown(6)) """

#  - Your function will receive a list with two numbers. Print the first value, and return the second.
""" def twoList(num):
    print(num[0])
    return num[1]

x = twoList([4,6])
print(x) """

# Given a list, return the sum of the first value in the list, plus the list's length
""" def sumList(num):
    return num[0] + len(num)

print(sumList([10,6,8,3])) """

# Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False

""" def greatList(num):
    if len(num) < 2:
        return false

    count = 0
    newNum = []
    for i in num:
        if i < i+1
            count = count + 1
            i = i + (i+1)
    return num """ # Question is not clear enough

# Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(size, value):
    newList = []
    for i in range(size, 0, -1):
        newList.append(value)
    return newList

print(lengthAndValue(2,100))

