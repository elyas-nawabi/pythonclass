# a set is a mutable collecion of distint object
# list [] tuple () set{}
numbers = {100,200,300,'apple', True, 4.4,100}
print(numbers)
#  a set does'nt store duplicate objects.
#  is an unordered collction of objects, meaning it does not record elements position
#  or order of insertion
mySet = {(1,2),3,1,3,2}
print(mySet)
name = "ahmad"
newSet = set(name)
print(newSet)
setoflanguages = {'python', 'java', 'php'}
setoflanguages.add('csharp')
setoflanguages.remove('java')
newlang = {'ruby','js','html','css'}
setoflanguages.update(newlang)
# update set with another set
print(setoflanguages)
