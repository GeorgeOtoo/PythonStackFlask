# Print all the numbers/integers from 0 to 150.
""" for i in range(0, 150):
    print(i) """

# Print all the multiples of 5 from 5 to 1,000,000.
""" for i in range(5, 1000000, 5):
    print(i) """

# Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo"
""" for i in range(0,100,1):
    if i%5 == 0:
        print("Coding", i)
        if i%10 == 0:
            print("Dojo", i) """

# Add odd integers from 0 to 500,000, and print the final sum
""" score = 0
for i in range(0,500000):
    if i%2 == 1:
        score = score + i
print(score) """

# Print positive numbers starting at 2018, counting down by fours (exclude 0)
""" for i in range(2018, 0, -4):
    print(i) """

# Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
""" for i in range(2,9):
    if i%3 == 0:
        print(i) """

""" list = [3,5,1,2]
for i in list:
    print(i) """

""" list = [3,5,1,2]
for i in range(list):
    print(i) """

""" list = [3,5,1,2]
for i in range(len(list)):
    print(i) """


# Functions Assignments

""" def a():
    return 5
print(a())   """   #always returns 5  when a is called

""" def a():
    return 5
print(a()+a()) """     #always returns 5+5=10

""" def a():
    return 5
    return 10
print(a())  """    #always returns 5  when a is called because it is the first return

""" def a():
    return 5
    print(10)
print(a())  """    #always returns 5. Doesn't get to the print method

""" def a():
    print(5)
x = a()
print(x) """     #Error. there is no return hence you cannot assign a to variable x

""" def a(b,c):
    print(b+c)

print(a(1,2) + a(2,3)) """ #return the sum in the a function to eliminate errors

""" def a(b,c):
    return str(b)+str(c)
print(a(2,5)) """  #prints 25 as strings

""" def a():
    b = 100
    print(b)    #prints 100
    if b < 10:
        return 5
    else:
        return 10 #returns 10
    return 7    #doesnt get tot this return
print(a())  """  #print 100 and return 10


""" def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3)) """ #prints 7, 14, 21

""" def a(b,c):
    return b+c
    return 10
print(a(3,5)) """ #prints 8

""" b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b) """ #500, 500, 300, 500

""" b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b) """ #500, 500, 300, 500

""" b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b) """ #500, 500, 300, 

""" def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() """

""" def a():
    print(1)
    x = b() #x=5
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a() #10
print(y) """



