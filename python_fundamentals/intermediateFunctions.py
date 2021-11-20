import random

# randInt() returns a random integer between 0 to 100

""" def randInt():
    return(int(random.random()*100)) #returns a random integer    
print(randInt()) """

# randInt(max=50) returns a random integer between 0 to 50
""" def randInt(max = 50, min = 0):
    return(int(min + (max-min)*random.random())) #returns a random integer    
print(randInt()) """

# randInt(min=50) returns a random integer between 50 to 100
""" def randInt(max = 100, min = 50):
    return(int(min + (max-min)*random.random())) #returns a random integer    
print(randInt()) """

# randInt(min=50, max=500) returns a random integer between 50 and 500
""" def randInt(max = 500, min = 50):
    return(int(min + (max-min)*random.random())) #returns a random integer    
print(randInt()) """

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ]. 
""" x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x) """

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
""" students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students[0]) """


# For the sports_directory, how would you change 'Messi' to 'Andres'?
""" sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer']) """


# For z, how would you change the value 20 to 30?
""" z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z) """

# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
""" students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for index in students:
    print("first_name -"  ,index['first_name'], ",","last_name -", index['last_name']) """


#Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

""" def iterateDictionary2():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    for index in students:
        print(index['first_name']) 

iterateDictionary2() """

#Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

def printDojoInfo():
    dojo = {
        'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }

    for key,value in dojo.items():
            print(len(value),key)
            
            for i in value:
                print(i)

printDojoInfo()
