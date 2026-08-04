''' list in python 
    they are mutuable(means changable)
    they are ordered
    in list square bracked [] are used'''

items = ["bru" , "coffee" , "sugar" ]
print(items)

items.pop()
print(items) # to remove last word in the list pop is used

items.append("milk") # to add any new in the last  of the list append is used
print(items)

items.insert(1,"chocolate")  #insert is used to add new word in the list
print(items)

items.remove("chocolate")  #remove is used to remove the last word in the list
print(items)

print(len(items)) #it is used to print the length in the list

items = ["bru" , "coffee" , "bru" , "milk" , "sugar"]
print(items . count("bru"))


fruits = ["apple" , "bananna" , "mango"] #Accessing list
print(fruits[1])

numbers = [2 , 9 , 5 , 4]  #sorting in list
numbers.sort()
print(numbers)

numbers = [1 , 2 , 3, 4]  #reversing in list
numbers.reverse()
print(numbers)

m  = [[1,2] , [3,4]]  #matrices
print(m)