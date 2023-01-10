# loop: basics, advance
# function, a function is a reuseable block of code to do a task.
# built in function, user functions
def display(brotherName, sisterName ):
    """ this function prints a statement """
    print("welcome dear: ", brotherName , " and ", sisterName)

# display("ahmad", "maryam")
# display("khan")
# display(123)
# display("mohammad")

# passing unlimited , unknown number of arguments to a function
# names = ['ahmad', 'omer', 'ayesha']
def meetings(*names):
    print("welcome dear: ", names[0], names[1], names[2])

# meetings('ahmad', 'omer', 'ayesha')

def meeting1(secondname, thirdname, firstname):
    print("welcome dear: ", firstname, secondname, thirdname)

# def meeting(**names):
#     print("welcome dear: ", names['firstname'], names['secondname'], names['thirdname'])

# meeting(firstname="ahmad", secondname="omer", thirdname="ayesh")
# meeting('ahmad', 'omer', 'ayesha')

# setting default values for functions
def test(name="john"):
    print("welcome dear ", name )
# test()

# most of the time, we neet the result of the function for further process

def divide(num1, num2):
    # print(num1 / num2)
    return num1 / num2
output = divide(10,2)
# print(output)
def add(output, num1):
    print(output + num1)
add(output, 10)
