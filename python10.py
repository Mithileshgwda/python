''' WHILE LOOP , BREAK , CONTINUE , NESTED WHILE LOOP'''

i = 1
while i <= 5:
    print(i)
    i += 1

name = "Mithilesh"
name = name[::-1]   # writing name in reverse
print(name)

sheep_count = 1                 # while loop example
while sheep_count <=10:
    print(f"sheep{sheep_count}")
    sheep_count += 1   


sheep_count = 1                          #while loop example using break statement
while sheep_count <= 10:
    print(f"sheep{sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break
    sheep_count += 1    


sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"sheep{sheep_count}")
    sheep_count += 1         
    
    
    '''while loop example using continue statement CONTINUE means used  to skip current iteration and 
       go to next statement '''


battery = 20
while battery < 100:
    print(f"charging...{battery}%")
    battery += 20

print("Battery fully charged")

correct_password = "1234"
entered_password = ""
while entered_password != correct_password:
    entered_password = input("enter password :")

print("access graunted")

# REAL WORLD EXAMPLE OF COMBINATION OF ALL IF ELSE ELIF NESTED IF LOOP WHILE BREAK CONINUE NESTED WHILE LOOP
correct_password = "1234"

# 🔐 Login system
while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break
    else:
        print("Wrong password, try again!")

# 📊 Marks system
while True:
    try:
        marks = int(input("Enter your marks: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    if marks < 0 or marks > 100:
        print("Invalid marks!")
        continue

    elif marks >= 90:
        print("Grade: A")

    elif marks >= 50:
        print("Grade: Pass")

    else:
        print("Grade: Fail")

    again = input("Check again? (yes/no): ").lower()

    if again == "no":
        print("Goodbye!")
        break


battery = 20

while battery < 100:
    print(f"charging{battery}%")

print("battery fully charged")


