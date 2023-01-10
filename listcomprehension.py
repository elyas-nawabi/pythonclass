# 
# evennumber = []

# for x in range(1,22):
#     if (x % 2) == 0 :
#         evennumber.append(x)

# print(evennumber)


evennumber = [ x for x in range(1,22) if x % 2 == 0 ]
print(evennumber)