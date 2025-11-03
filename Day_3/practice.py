
# This program asks for user's details and prints a short intro

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Output using concatenation (joining strings)
print("Hello " + name + "! You are " + str(age) + " years old and live in " + city + ".")

# Output using f-string (no need to convert int to string)
print(f"Hi {name}! Next year, you will be {age + 1} years old and still rocking in {city} 😄")

# End message
print("Thanks for using my program!")

