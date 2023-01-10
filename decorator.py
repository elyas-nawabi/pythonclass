# decorator adds additional responsibility to an object dynamically.
# first function   pass first Funtion to  -> function two (customize our first function) -> 
# return customized function

def functionTwo(firstFunction):
    def customizing():
        firstFunction()
        print(" How are You! ")
    return customizing

@functionTwo
def firstFunction():
    print('Hello Mustafa')

@functionTwo
def anotherFunction():
    print("Hello all students: ")

anotherFunction()
    
