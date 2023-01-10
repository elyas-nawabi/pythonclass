# variable, a- local,   b- global
# we can access global variable globaly across the program
# we can access lobal variable just inside the function

name = "ahmad"

def useLocal():
    # global name 
    name = "mohammad"
    print("this is a local variable named:  ", name)

useLocal()
# use global
print("outside the function: ",name)
    