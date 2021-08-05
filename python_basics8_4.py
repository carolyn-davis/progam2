#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:48:50 2021

@author: carolyndavis
"""
# =============================================================================
#                     PYTHON REVIEW PRACTICE
# =============================================================================
d = {'key1': 'value', 'key2': 123}
d['key1']      #can only pull keys out of list not indexes  likd d[0]


d= {'k1':{'innerkey': [1,2,3]}}  #This is a dictionary within a dictionary 
#How do we call this?

d['k1']['innerkey'][1] #Returns the list of values for the 'innerkey

# my_list =[a sequence of characters within brackets, separated by commas]

#Tuples are very similar, except instead of using square brackets [], you use ()

t = (1,2,3)   #like lists you pull values by indexing t[]
t[0]

#Key difference between tuples and lists 
my_list = (1,2,3)    #Unlike lists, you can not reassign values in a tuple.
t[0] = 'NEW'


#YOU really want to use tuples to Prevent the user from changing objects with in the sequence


#SET : collection of unique elements
#Unlike dicts and lists, use the curlie brackets{}, no need for colons

{1,2,3}

{1,1,1,2,2} # The output returns just {1,2}
#This is because a set is only a unique elements. 1 of each

set([1,1,1,1,2,2,2,5,5,6,6,6])   #you can pass a list through the set functions to retrieve the unique elements


#You can add new elements to a set 

s = {1,2,3}

s.add(5)   #This is the method for adding elements to a set

print(s)   #{1,2,3,5}

1 > 2
#comparison operators return boolean values 
(1 < 2) or (5 > 10)   #or operator looks for either value for truth


if 1<2:
    print('yes')

if True:
    print('Perform code')
    
    
#Lets say we want multiple conditions. If we want something to occur if the condition is not true

if 1 == 2:              #If this code is true
    print('First')      #print this
else:                   #If it is not true...
    print('last')       #print this code
    
#Say you want to check for multiple conditions 

#then use elif
if 1 == 2:              #if this condition is true 
    print('First')      #print this 
elif 3 == 3:            #else if it is not and this condition is True
    print("Middle")    #print this
else:                   #If none of the conditions above are true 
    print('last')       #print this
    
    
#You can have as many elif statements as you want....
if 1 == 2: 
    print('First')
elif 4 == 4:            #Notice that the conly condition printed was the first that ran True "Second"
    print("Second")     #The first condition that is met is the only output printed
elif 3 == 3:  
    print("Middle")
else:  
    print('last') 


# =============================================================================
#                     FOR LOOPS AND WHILE LOOPS
# =============================================================================

#For loops allow you to iterate through a sequence

seq = [1,2,3,4,5]   #list of num

for jelly in seq:        #The temporary variable name 'item' can be anything you want it to be 
    print(jelly)     #Note the item in the print function can be anything you want it to be 
    
for jelly in seq:
    print('hello')    #iterates through sequence and return hello for each value in sequence (5)
    
    
    
#WHILE LOOPS 
#These are used to continually iterate through a sequence until conditions are met

i = 1
while i < 5:
    print(f'i is: {i}')  #Remember f' string must have a placeholder in curly brackets within notation {i}
    i = i+1 #While loop will execute a code while a condition is truye
      # if the first condition is True, print i is 0, add one to it and so on


#Other Methods/Functions in Python 
#Range

for x in seq:
    print(x)
    
# To specify the number of times you want to want to iterate

range(0,5) #this is a range object

for x in range(0,5):     #shorthand for generating values
    print(x)

#If you wanted to generate a list as the output:

list(range(0,5))   #outputs a list of elements


#List Comprehension: Saves you a bunch of time and writing when you are trying to create a for loop to make a list

x = [1,2,3,4]

out = []                #empty brackets act as a collector
                         #without this we would constantly have to update and input into the list 
for num in x:
    out.append(num**2)  #appends the powers of each item in x. Takes this info and adds it to the collector 'out'
print(out)

[num**2 for num in x]
#This is basically saying.....
out = [num**2 for num in x] #Give me the num squared for each num in x (list)



#FUNCTIONS MAKING THEM

def my_func(param1):       #Takes in the input
    print(param1)           #prints the inout

my_func('hello')            #Call the function with its name and () + input



def my_func(name):
    print('Hello '+name)    #This concats the variable name to the print 'Helo


my_func('Carolyn')   #processes names as whatever user calls in function 

def my_func(name='Default Name'):
    print('Hello '+name)
my_func()   #will still run with out anything

# Let's return a value that want to assign to another variable:

    
def square(num):
    return num**2     #You want to return a value so that your function is actually return the value as well as store it 

output = square(2)
output()

#Doc Strings

def square(num):
    """
    THIS IS A DOCSTRING
    CAN GO MULPTIPLE LINES
    """
    return num**2


# The map() function

seq = [1,2,3,4,5]   #Let's say i wanted to apply an element to every element in the list and output a list
#Could use a for loop and apply a function that appends the element to an empty new list OR

list(map(square, seq))   #If you wrap the map in a a list function 
                        #It will map to every element in the sequence, apply the function square
                        #and output it as a list
#^^this method calling the function will not always be useful
#Sometimes you do not want to call a whole function within the map() tool

##This is where LAMBDA comes in 

#def square(num):
    #return num**2
#Can actually be written like

def square(num):return num**2     #it works the same as indented stacked format
#Lambda removes words that you dont need like def square() and return into one line simplicity

t = lambda var:var*2
t(2)

list(map(lambda num: num*3,seq)) #It's basically re-writing a function into one line of code

#FILTERING 
#Similar to map except instead of mapping a function to elements in a sequence
#We will filter out elements from a sequence

filter(lambda num: num%2 == 0, seq) #Pass in either a function or lambda exp and returns boolean values 
                                    #seq is the iterable object that must be passed through
#num%2 "mod2"
#This just passes back a filter espression so we have to attach it to a list

list(filter(lambda num: num%2 == 0, seq))   #returns a list of only the even numbers in a list




# =============================================================================
#                 METHODS
# =============================================================================


s = 'hello my name is Sam'
s.upper()


s = 'hello my name is Sam'
s.split()    #splits a string on all the white space on a string
            #super useful for text analysis
            
tweet = 'Go Sports! #Sports'

tweet.split()   #splits the text into a list each element in string

tweet.split('#')   #splits on specific characters like the hashtage

tweet.split('#')[1]   #If you want to just grab the hashtage element set the index to the first element in that hashtag 
#useful for text analysis

d = {'k1': 1, 'k2': 2}

d.keys()    #returns the keys of a dictionary 


d.items()    #This returns the all the items in the dictionary 


d.values()   #this returns just the values of the dictionary 1,2

#Useful Methods For lists

lst = [1,2,3]

lst.pop()  #pops an items off the list.... the last element of a list on default

lst   #Then when you call the list that change is permanent

lst = [1,2,3,4,5]

item = lst.pop()
lst
item


#you can index an item to actually remove from a list with pop()

sample = [1,2,3,4,4]


first = sample.pop(0)       #pop removes the first element at the index 0
first                       #first now contains the lement popped from the list
sample                          #Sample now starts at value 2

pop()

#In Operator
#If you want to check if something is in a list 
#the thing you want to check, the in operator and the values 

'x' in [1,2,3]   #returns bool False

'x' in ['x', 'x', 'z']




#Review Tuple Unpacking
#Say you have a variable x that contains a list of tuples


x = [(1,2), (3,4), (5,6)]
x

#If you look the first item is a tuple of x
x[0]   #(1,2)

#you can grab items from the typle
x[1][2]

#Tuple unpacking

for (a,b) in x:     #This prints off the individual items in the first item in the list of tuple (1,2)
    print(b)
