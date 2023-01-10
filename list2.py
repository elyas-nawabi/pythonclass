# 
name = "ahmad"
print(name[0])
listNames = ["ahmad","maryam","khan",[2,3,4, [900,800,83]]] #nested list, inner list
print(listNames[3][3][1])

name = "mohammad" # string
# we can convert any datatype to list
# list()
print(list(name))

listBooks = [
    "pythonProgramming", 
    "Python for dummies", 
    "LearnPythonWithAhmad"
    ]
# print(listBooks[0])
# print(listBooks[1])
# print(listBooks[2])
# how to update a list
listBooks[0] = "JS programming"
# how to add a new list
listBooks.append("ReactForDummies")
# 
listBooks.remove("LearnPythonWithAhmad")
del listBooks[1]
listBooks.pop()

del listBooks

# print(listBooks)
# Iterate on List
for _books in listBooks:
    print(_books)





    
