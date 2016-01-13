# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 11:45:09 2014

@author: nagill
"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell','strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

#Shopping example
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total=0
    for item in food:
        if(stock[item]>0):
            total+=prices[item]
            stock[item]-=1
    return total

    print compute_bill(prices)
 
#Student dictionary   
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework*.10 + quizzes*.30 + tests*.60

def get_letter_grade(score):
    if(score>=90):
        return "A"
    elif(score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "D"
    else:
        return "F"
    
    get_letter_grade(get_average(lloyd))
    
def get_class_average(students):
    results = []
    for each in students:
        results.append(get_average(each)) 
    return average(results)

students = [lloyd,alice,tyler]   
print get_class_average(students)
print get_letter_grade(get_class_average(students))


#looping throgh list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for lst in lists:
        for item in lst:
            results.append(item)
    return results
        



print flatten(n)

