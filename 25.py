# EXCEPTION HANDLING IT IS THE PROCESS OF PROTECTING THE PROGRAM FROM CRASHING DUE TO ERRORS 

# methods are try,except,else,finally

a = int(input("a:"))
b = int(input("b:"))

try:
    print(a/b)

except:
    print("Error came")

finally:
    print("I will execute no matter what")



a = int(input("a:"))
b = int(input("b:"))

try:
    print(a/b)

except Exception as e:
    print(f"Error came {e}")

else:
    print("no error came")

finally:
    print("Program ended!")
