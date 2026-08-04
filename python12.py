battery = 20

while battery < 100:
    print(f"charging{battery}%")
    battery += 20

print("battery fully charged")

correct_password = "1234"
entered_password = ""
while entered_password != correct_password:
    entered_password = input("Enter your password :")

print("access graunted :")