for i in range(1,11):
    print(i)           #RANGE CONCEPET IN NEW LINE EVERY TIME


for i in range(1,11):
     print(i, end="") # RANGE CONCEPET IN SAME LINE


bag = ["red", "yellow", "blue", "Green"]

for ball in bag:
     print(ball)  #lists in for loop concepet 


for i in range(1,11,2):  #START STOP END CONCEPET
     print(i)


# LOOPS OVER STRINGS

name = "mithilesh"

for letter in name:
     print(letter)

name = "mithilesh"

for letter in name:
     print(letter*2)



name = "mithilesh"

for  index, letter in enumerate(name):
     print(letter*(index + 1))

#BREAK CONCEPET IN FOR LOOP

cities = ["bangalore", "mysuru", "hubbali","mangalore"]

for city in cities:
     if city == "hubbali":
          print(f"Found{city}!")
          break
     print(city)

# CONTINUE IN FOR LOOP

for city in cities:
     if city == "hubbali":
          continue
     print(city)

l = [1,12,1111,222]

for num in l:
     print(num)
else:
     print("all printed")


#IF WE USE d.items() IT WILL BE CONVERETED FROM DICT TO LIST INSIDE TUPLE WILL BE THERE
d = {"name" : "mithilesh" , "age" : "18" ,"income" : "1"}
print(d.items())   

#DICTIONARY IN FOR LOOP
d = {"name" : "mithilesh" , "age" : "18" ,"income" : "1"}

for key, value in d.items():
     print(key," ",value)

# NESTED FOR LOOP

for i in range(1,11):
     print(f"2 X {i} = {2*i}")  #PROGRAM TO WRITE EACH TABLE

for i in range(2,11):
     for j in range(1,11):
          print(f"{i} X {j} = {i*j}")  #PROGRAM TO PRINT TABLES 1 TO 10 