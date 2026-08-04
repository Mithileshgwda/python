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