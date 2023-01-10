# dictionary is an unordered collection 
# key:value pair
# {key:value}
# list1 = [[1,2,3],[3,4,3],[5,6,7]]

# for x in range(len(list1)):
#     for y in range(len(list1[x])):
#         if list1[x][2] == 3:
#             print(list1[x][2]+list1[x][0])
#         break
         
capitals = {"afghanistan":"kabul",
            "usa":"washington",
            "argentina":'bounceaires'}
# print(capitals["afghanistan"])
# print(capitals.get("usa"))
# update our dictionary
# capitals["usa"] = "france"
# add new key,value
capitals['germany'] = 'berlin'
# del a key,value
# del capitals["afghanistan"]
# del capitals
# for key in capitals:
#     print(key,"   ---  ", capitals[key])
    # print("key = ", key, "value = ", capitals[key])

# print(capitals.keys())
# print(capitals.values())

# print('swizerland' in capitals)

student = {
    "studentInfo" : {"name":"ahmad", "age":14, "grade": "A"},
    "marks" : [80,90,100,55]
}
# print(student["studentInfo"])
print(student.items())
# student["newitem"] = 30
# print(student)

# dic = {
#     "name" : "ahmad",
#     "age" : 12
# }


