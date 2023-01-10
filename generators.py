# Generators: are basically functions that return traversable objects or items.
# these functions .
# these functionss do not produce all the items at once.
# rather they produce them one at a time and only required.

# advantage: easy to implemet
#  memory is saved 
# can be used to produce an infinite number of items.
# list of numbers
# Normal function V.S generators
# def sum() , def sum()
# generator functions make use of yeild keyword instead of return
# sum(),      next()
# [1,2,3,4]

# def numbers(a):
#     return a

# a = [1,2,3]
# output = numbers(a)
# print(output)

# def numbers(a):
#     yield a

# a = [1,2,3]
# output = numbers(a)
# print(next(output))

# def numbers(a):
#     return a
# a = [1,2,3]
# print(numbers(a))

# def genNum(a):
#     while a>=3:
#         yield a
#         a = a + 1
# output = genNum(5)
# print(next(output))
    
# def gen():
#     print("Grade A:")
#     yield 100

#     return
#     print("Grad B:")
#     yield 80

#     print("Grade C:")
#     yield 50

# output = gen()
# print(next(output))
# print(next(output))
# print(next(output))
# next(output)
# next(output)
# next(output)

# def listNumbers(num):
#     for item in range(num):
#         yield item * item
# output = listNumbers(10)
# while True:
#     try:
#         print("umbers :", next(output))
#     except StopIteration:
#         break

def listNumbers(a):
    for i in range(a):
        yield i  # 0 1 2 3 4 5 6 7 8 9 
output = listNumbers(10)
for item in range(4):
    print(next(output))

print("------")
print(next(output))

        
    