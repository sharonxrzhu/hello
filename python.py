# SETS
# s = set() #not element appears to times in a set
# s.add(1)
# s.remove(1)
# print(f"The set has {len(s)} elements")


# FOR LOOPS
# for i in [0,1,2,3,4,5]:
#     print(i)
# for i in range (6):
#     print(i)

# names = ["Harry", "Ron", "Hermione"]
# for name in names:
#     print(name)

# name = "Harry"
# for character in name:
#     print(character)


# DICTIONARY
# houses = {"Harry": "Gryffindor", "Dreco": "Slytherin"}
# houses["Hermione"] = "Gryffindor"
# print(houses["Harry"]) # get Gryffindor
# print(houses["Hermione"]) # get Gryffindor


# FUNCTION 
# def square(x):
#     return x**2
# for i in range(10):
#     print(f"The square of {i} is {square(i)}")


# IMPORTS
# Option 1
# from squares import square
# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

# Option 2
# import squares
# for i in range(10):
#     print(f"The square of {i} is {squares.square(i)}")


# CLASS
# class Point():
#     def __init__(self, input1, input2): #new method aka function
#         self.x = input1 # self is representing the point itself
#         self.y = input2

# p = Point(2,8)
# print(p.x)
# print(p.y)

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)

# flight = Flight(3)

# names = ["Harry", "Ron", "Hermione", "Ginny"]
# for person in names:
#     if flight.add_passenger(person):
#         print(f"Added {person} to flight successfully.")
#     else:
#         print(f"No avaliable seats for {person}")


# # DECORATORS
# def announce(f): # gets our wrapped function named f
#     def wrapper(): # runs another function
#         print("About to run the function")
#         f() # runs the wrapped funtion
#         print("Done with the function")
#     return wrapper

# @announce
# def hello():
#     print("Hello, World")

# hello()
# # decorators can be used to check if a user is loged in...


# LAMBDA
# people = [
#     {"name":"Harry", "house": "Gryffindor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

#python cannot sort dictionaries

# Option1
# def f(person):
#     return person["name"]
# people.sort(key=f) # sort people by name
# print(people)

# Option2
# people.sort(key=lambda person: person["name"]) # sort people by name
# print(people)


#exceptions
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")

