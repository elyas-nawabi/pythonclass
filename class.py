# oop:object oriented programming, is a technique of coding, or method a style of coding
# class, object
# python is a completely object oriented language
# every element in a python program is an object of class
# x = 5
# name = "ahmad"
# print(type(name))
# x = 5
# x = [1,2,3,4]
# set, tuple, dic,

class Car:
    def __init__(self, model="2000", speed=100):
        # print("constructor is called.")
        self.model = model
        self.speed = speed

    def displayInformation(self):
        print("Car information")
        print(self.model," ---> ", self.speed)

toyota =  Car("2022", 360)  # this is first object
toyota.displayInformation()
# print(toyota.model,"  ---  ", toyota.speed)
bmw = Car("1990", 180)
bmw.displayInformation()
# print(bmw.model," --- ", bmw.speed)
corolla = Car()
corolla.displayInformation()
# print(corolla.model," --- ", corolla.speed)

# write a class name student
# define a method to display names of 10 student