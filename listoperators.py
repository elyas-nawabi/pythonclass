listofweekdays = ["saturday", "sunday", "monday","tuesday",
                  "wed", "thursday","friday"]
listofmonths = ["october","november","december"]
# list[initial : End : indexJump]
# print(listofweekdays + listofmonths)

# print(listofweekdays * 3)
# in string, :
# print(listofweekdays[2:5])
# print(listofweekdays[2:])
# print(listofweekdays[:3])
# print(listofweekdays[-5:-1])
# print(listofweekdays[-5:])

# print(listofweekdays[0:7:2])
# monday, saturday, tuesday
# print(listofweekdays[::])
# print(listofweekdays[-7::])
# print(listofweekdays[::2])  
# print(listofweekdays[::-1])  # friday, thurs..... sat
# print(listofweekdays[::-3])
# print(listofweekdays[:1:-3])
# if some slicing expressions are made that don not make sense or are incomputable
# then empty lists are generated
# print(listofweekdays[1:1:1])
# print(listofweekdays[-1:-1:-1])
# print(listofweekdays[:0:3])

# listofweekdays[1] = "day1"
# listofweekdays[2] = "day2"
# listofweekdays[3] = "day3:
# listofweekdays[1:4] = ["day1","day2","day3"]

# print(listofweekdays)
# del listofweekdays[0:6]
# listofweekdays[:6] = []
# print(listofweekdays)

# somedays = listofweekdays[:3] + listofweekdays[7:]
# print(somedays)

somedays = listofweekdays[::2] + listofweekdays[1::2]
print(somedays)
