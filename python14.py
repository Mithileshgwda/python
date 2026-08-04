#LOOPING THROUGH LIST

l = [1,22,345,546,652]
print(sum(l))

l = [1,22,345,546,652]
total = 0
for num in l:
    total = total + num

print(total)

#DOUBLING EACH NUMBER IN A LIST

l = [1,22,345,546,652]
dl = []

for num in l:
    dl.append(num*2)
    print(dl)

#PRINTING FOOD ITEMS USIN FOR LOOP

food = ["dosa", "idli" , "bath", "curd rice"]
for foods in food:
    print(f" I like {food}")

#LOOPING THROUGH DICTORINARIES

student_marks = {"anand" : 30, "geetha":20, "shiva":39}

for student in student_marks.items():
    print(student)
