#string manipulation

''' 0 1 2 3 4 5 6 7 8 INDEX VALUES   POSITION = INDEX + 1 
    M I T H I L E S H 
    1 2 3 4 5 6 7 8 9 POSITION VALUES
   -9 -8 -7 -6 -5 -4 -3 - 2 -1'''

name = "Mithilesh"
print(name[2])

print(name[-3])

print(name[1:9])

print(name[2:]) #from t to still end it will print


''' string methods
 1 upper
 2 lower 
 3 stripe
 4 replace'''

message = "Warning"
print(message.upper()) # capital letters

print(message.lower()) # all letters will be small

print(message.strip())

print(message.replace("Warning","Error"))


#CONCATINATION :- means joining 2 words 

first_name = "Mithilesh"
last_name = "gowda"
full_name = first_name + " " +  last_name
print(full_name)

#STRING LENGTH 

message = "Mithilesh gowda HA"
print(len(message))

#ESCAPE SEQUENCE

name = "Mithilesh \n is good boy"   #is good boy will be printed in next line
print(name)

name = "Mithilesh \t is a good boy"
print(name)                            # \t is used to leave the space