import ourBase
import datetime

# ourBase.my_first_func()

# print(ourBase.my_var)

# print(datetime.date.today())

# Python if statement..
"""if statement is a way to test if a condition is true or false and we perform our desired actions."""
# test = None
# if test == True:
#     print("This is really true!")
# else:
#     print("This is not true!")

# age = 10
# age = 29
# # age = 22
# if age <= 10:
#     print("This is a kid!")
# elif age >= 22 and age < 30:
#     print("This is a teen!")
# elif age == 30:
#     print("This is an adult!")
# else:
#     pass
    # print("This is not a valid age!")



# Python function..
""" Python function """

# def my_first_func(**kwargs):
#     """This is the documentation of our function! `WITHUBB CLASS` To run this fuction you must add two args the `x, y` """
#     # has_passed = f'This our {name} and the {position} of our fuction!'
#     # for x in args:
#     #     print(f'{x}')
#     for x in kwargs.values():
#         print(f'{x}')

#     # has_passed = f''

#     return

# def my_first_func(name=int(), val=str()):
#     """This is the documentation of our function!"""
#     data = f'{name} === and ==== {val}'
#     print(data)

# my_first_func(name='I am a Withubb Ltd student. \n', val='I am very glad to be here!')

# my_first_func(name='This is Withubb', hobby='I and happy!', said='hello')

# var = f'I love Python, \n and that\'s why \n am here!'

# print(var)


# Python while loop..
"""A while loop can be used repeat a block of code multiple times."""
# x = 0
# while x <= 20:
#     x += 1
#     print("We are here!")
#     if x == 10:
#         break



# Python dictionary..
"""Dictionaries are used to store data values in key-value pairs. They are collections that are ordered*, mutable, and do not allow duplicate keys."""

names = {
     'Chimobi': 'Hello can I ask you a question',
     'Emmanuel': 'Hi, do we have class today sir!',
     'Femi': 'Hello, I will watch the videos.',
     'Okolie': 'Ok sir, thank you!',
     'hobby': {'today': 'reading!', 'yesterday': 'coding', 'myList':['Coding now!', 'Reading later!']}
 }

# loop through a dictionary..
# for x in names:
#   print(names[x])

# loop through a dictionary values..
# for x in names.values():
#   print(x)


# loop through a dictionary keys..
# for x in names.keys():
#   print(x)


# loop through a dictionary key and values..
# for x, y in names.items():
#   print(f'Key: {x} \n Value: {y} \n\n')

# adding default values to catch a None dict value..
# print(names.get('Chimobi'))
# print(names.get('Withubb'))

# new_names = names.copy() # to copy a dictionary
# new_names = dict([('Doing', 'Coding now'), ('To_do', 'Reading later!')])

# print(new_names.get("Doing"))

# print(new_names.get('hobby', "I don't know who you are!").get('myList')[0])


# python list..
""" A List is an Array look-alike data type in Python that allows you to store and manipulate collections of items.
You can create a list by placing all the items (elements) inside square brackets `[]`, separated by commas.
"""

# Creating a list
students = ["Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi"]
# print(students)


#### Accessing List Items

# List items are indexed, with the first item having index `[0]`, the second item having index `[1]`, and so on.

# Accessing items
# print(students[0])  # Output: Chimobi
# print(students[1])  # Output: Emmanuel


#### Changing List Items

# Lists are mutable, meaning you can change their elements after creation.

# Changing items
# students[1] = "Withubb"
# print(students)  # Output: ["Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi"]


#### Looping Through a List

# You can loop through the list items using a `for` loop.

# Loop through a list
# for xx in students:
#     print(xx)


#### List Length

# Use the `len()` function to determine the number of items in a list.


# Length of a list
# print(len(students))


#### Adding Items to a List
# You can add items to a list using the `append()` method to add to the end or `insert()` to add at a specific position.
# students.append("Withubb")
# print(students)  # Output: ["Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi", "Withubb"]

# Pop an item
# students.pop(6)
# print(students)  

# Insert an item
students.insert(1, "Withubb")
print(students)  


#### Removing Items from a List

# Use the remove() method to remove a specific item, or pop() to remove an item at a specific index (or the last item if the index is not specified).


# Remove an item
# students.remove("Withubb")
# print(students) 



#### List Comprehensions

# List comprehensions provide a concise way to create lists.
fruits = ["Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi"]

newlist = [x for x in fruits if "a" in x]


# Some common list methods:

# - append(): Adds an element at the end of the list.
# - insert(): Adds an element at the specified position.
# - remove(): Removes the first item with the specified value.
# - pop(): Removes the element at the specified position.
# - sort(): Sorts the list.
# - reverse(): Reverses the order of the list.
# - index(): Returns the index of the first element with the specified value.
# - count(): Returns the number of elements with the specified value.


# Example of using some methods
# numbers = [5, 3, 8, 1, 2]
# numbers.sort()
# print(numbers)  # Output: [1, 2, 3, 5, 8]

# numbers.reverse()
# print(numbers)  # Output: [8, 5, 3, 2, 1]

# print(numbers.index(3))  # Output: 2

# print(numbers.count(5))  # Output: 1




# python Set..
""" Python Tuple, 
Tuples are used to store multiple items in a single variable. They are one of the built-in data types in Python used to store collections of data, alongside Lists, Sets, and Dictionaries, each with unique qualities and uses.

A tuple is an ordered and unchangeable collection, written with round brackets.
"""

# my_tuple = ("Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi")
# print(my_tuple)
# tuple()

# python list..
""" Python set, Sets are used to store multiple items in a single variable.
A set is one of the four built-in data types in Python for storing collections of data, alongside Lists, Tuples, and Dictionaries, each with unique characteristics and uses.
A set is an unordered, unchangeable*, and unindexed collection. """

my_set = {"Chimobi", "Emmanuel", "Dave", "Austine", "Nelson", "Femi", True, 500}
# my_set.add()


# Python has four built-in collection data types:

# - List: An ordered and changeable collection that allows duplicate members.
# - Tuple: An ordered and unchangeable collection that allows duplicate members.
# - Set: An unordered, unchangeable*, and unindexed collection with no duplicate members.
# - Dictionary: An ordered** and changeable collection with no duplicate members.




# python ..
""" ... """