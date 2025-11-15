# -----------------------------------------
# Practice: Python Functions 
# -----------------------------------------

print("------ Example 1: Basic Function ------")

def say_hello():
    print("Hello! This is my first Python function.")

say_hello()
print()


print("------ Example 2: Function with Parameter ------")

def welcome_user(username):
    print(f"Welcome, {username}! Let's start learning.")

welcome_user("Mithun")
welcome_user("Anand")
print()


print("------ Example 3: Returning a Value ------")

def multiply(x, y):
    return x * y

result = multiply(4, 6)
print("Multiplication Result:", result)
print()


print("------ Example 4: Default Parameters ------")

def greet(person="Friend"):
    print(f"Hi, {person}! Nice to meet you.")

greet()            # uses default value
greet("Neha")      # custom value
print()


print("------ Example 5: Local vs Global Variables ------")

score = 50  # Global variable

def update_score():
    score = 100  # Local variable
    print("Inside function:", score)

update_score()
print("Outside function:", score)
print()


print("------ Example 6: Nested Functions ------")

def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function inside the outer function.")

    inner_function()

outer_function()
print()
