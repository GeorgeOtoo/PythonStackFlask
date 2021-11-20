#  Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.
def reverseList(list):
    
    i=0
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]

    return list

#print(reverseList([1,3,5,9,6]))



# Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').
def isPalindrome(word):

    i=0
    for i in range(len(word)-1-i):
        if word[i] != word[len(word)-1-i]:
        
            return False
        
    else:
        return True

#print(isPalindrome("racecarr"))

    

# Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().
def coins(amount):

    # quarters, dime, nickel, pennies = 0
    arr = [] 

    quarters, amount = divmod(amount, 25)
    dime, amount = divmod(amount, 10)
    nickle, amount = divmod(amount, 5)
    pennies, amount = divmod(amount, 1)

    arr.append(quarters)
    arr.append(dime)
    arr.append(nickle)
    arr.append(pennies)

    return arr
    #print([quarters, dime, nickle, pennies])
    #print(arr)
#coins(87)


# (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).
def factorial(n):
    
    if n == 0:
        return 1

    return n * factorial(n-1)

#print(factorial(5))

# (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).
def fib(n):
        
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#print(fib(6))