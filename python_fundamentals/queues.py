# If you're given a list with a bunch of numbers and you're supposed to sort the numbers (with the smallest number on the left and the largest number on the right), how would you do this? There are numerous sorting algorithms to sort numbers in the list. We'll introduce one of the simplest sorting algorithm called selection sort.

# Selection Sort
""" def selectionSort():
    arr = [64, 25, 12, 22, 11]

    for i in range(len(arr)):
        # loop through the array indices
        print(i, "This is i")

        minIndex = i # 1, 2, 
        for j in range(i+1, len(arr)):
        #min = arr[0]
            #print("/n")
            #print(arr[minIndex], "with the min index")
            #print(arr[j], "current j")
            if arr[minIndex] > arr[j]:
                minIndex = j
                print("this is the minIndex", minIndex)
            
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            print(arr)
            #print(("-")*20, "new J")
            #print(j)

selectionSort() """

""" def mySelectionSort():
    arr = [8,9,4,6,2,0,1]

    for i in range(len(arr)):
        #print(i) 
        minValue = i
        for j in range(i+1, len(arr)):
            if arr[minValue] > arr[j]:
                minValue = j
        arr[i], arr[minValue] = arr[minValue], arr[i]

    return arr

print(mySelectionSort()) """

# Execute Insertion Sort

""" def myInsertionSort():
    arr = [11,9,5,1,8,3]

    for i in range(1, len(arr)): #[9,11,5,1,8,3]
        nextVal = arr[i] # 9,5

        prev = i - 1 # 0,1
        while prev >= 0 and nextVal < arr[prev]: #5< 11 yes --> 5< 9
            arr[prev+1] = arr[prev] #[11,11,5,1,8,3], [9] -->[9,11,11,1,8,3] --> [9,9,11,1,8,3]
            prev = prev - 1   # -1 and while loop is false --> 0
        arr[prev+1] = nextVal # arr[0] --> [9,11,5,1,8,3] --> [5,9,11,1,8,3]

myInsertionSort() """

#Lambdas
""" def lambdaExamples(num, lamb):
    y = num + lamb(2)
    return y

print(lambdaExamples(2, lambda x: x + 2)) """

""" trywithArr = [5,7,8,'here', lambda y: y*4]
print(trywithArr[4](8)) """

""" my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument
# Functions where this implementation comes into play:

# map()
# reduce()
# sort() - lambda is optional
# filter() """
