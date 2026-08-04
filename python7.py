'''TUPLES AND SETS

tuples and sets are same but the difference is bracket in list [] and in tuples() 
and list are mutuable and tuples are immutable'''

genders = ("male" , "female" , "other")
print(genders)

print(len(genders))

print(genders[2])

#CONCATINATION IN TUPLE

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

# MEMBERSHIP OPERATOR IN TUPLE

fruits = ("apple" , "bananna" , "mango")
print("apple" in fruits)

''' sets repesented in {} it is unordered here indexing is not possible 
types are UNION INTERSECTION DIFFERENCE'''

s = {1,2,3}
print(type(s))

s1 = {1,2,3}
s2 = {4,5,6}
print(s1|s2) #UNION Example in SETS

s1 = {1,2,3}
s2 = {3,5,6}
print(s1&s2) #INTERSECTION Example in SETS
