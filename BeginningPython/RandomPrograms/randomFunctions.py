# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 11:10:50 2014

@author: nagill
"""
#Is it an int?
def is_int(x):
    if (int(x) - x) != 0 and (int(x) - x) != 1:
        return False
    else:
        return True

#Sum digits of number        
def digit_sum(n):
  string_n = str(n)
  total = 0
  for char in string_n:
    total += int(char)
  return total

#Factorial 
def factorial(x):
    if(x==1 or x==0):
        return 1
    else:
        y = 1
        z = 1
        while y <= x:
            z *= y
            y += 1
        else:
            return z

#Prime?
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x!=n and x % n == 0:
                return False
        return True

#Reverse string
def reverse(text):
    text_new = []
    for c in range(len(text)-1,-1,-1):
       text_new.append(text[c])
    return ''.join(text_new)
    
#anti vowel
vowels="aeiou"
def anti_vowel(x):
    for a in x:         
        for j in vowels:
           if a.lower()==j:
               x=x.replace(a,"")
    return x

#Scrabble   
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    word = word.lower()
    word = list(word)
    total = 0
    for item in word:
        total += score[item]
    return total

#censor
def censor(text, word):
    split_text = text.split()
    for item in range(len(split_text)):
        if split_text[item] == word:
            split_text[item] = ("*" * len(word))
    return " ".join(split_text)
    
#Count
def count(sequence,item):
    found = 0
    for x in sequence:
        if x == item:
            found += 1
        else:
            found = found
    return found

#Return list of even
def purify(numlist):
    even = []
    for num in numlist:
        if num%2==0:
            even.append(num)
    return even
    
#Multiplication
def product(listint):
    total = 1
    for num in listint:
        total*=num
    return total

#Remove duplicates
def remove_duplicates(duplist):
    duplist2 = []
    for num in duplist:
        if(num not in duplist2):
            duplist2.append(num)
    return duplist2

#Median
def median(l):
    v = sorted(l)
    if len(v) % 2 == 0:
        top = len(v) / 2
        bottom = top - 1
        return (v[top] + v[bottom]) / 2.0
    else:
        return v[(len(v) / 2)]
#Computing stats
 grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
    average = grades_average(grades)
    variance = 0
    for score in grades:
        variance += (average - score) ** 2
    return variance / len(grades)
print grades_variance(grades)

def grades_std_deviation(variance):
    return variance**0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades_variance(grades))