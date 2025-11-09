# Conditional Statements Practice)


# 1) Check if a number is even or odd.
number = 7
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 2) Check if a person is a child, teenager, or adult.
age = 14
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")


# 3) Check if a username and password is correct.
username = "user123"
password = "pass"
if username == "user123" and password == "pass":
    print("Login Successful")
else:
    print("Login Failed")


# 4) Nested if: Check if today is holiday and weather is good.
holiday = True
weather_good = False
if holiday:
    if weather_good:
        print("We will go for a trip!")
    else:
        print("Holiday but weather is bad :(")
else:
    print("No holiday, Study day!")


# 5) match-case: Identify fruit color.
fruit = "banana"
match fruit:
    case "apple":
        print("Color: Red")
    case "banana":
        print("Color: Yellow")
    case "grapes":
        print("Color: Green or Purple")
    case _:
        print("Unknown fruit")
