class Student:
    __schoolName = "MySchoolName"
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def __Display(args):
        print("this method is private.")

obj = Student("mustafa", 14)
obj.__Display()
# print(obj._Student__schoolName)
# print(obj.__name)
        