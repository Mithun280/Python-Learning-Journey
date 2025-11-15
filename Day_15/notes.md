# Day 15
# Python Functions – Notes

- A function is a `reusable block of code` that performs a specific task when called. Functions are useful to `organize code`, make it `reusable`, and `reduce redundancy`.

## 1. Basics of Functions

- A function is a reusable block of code that performs a specific task only when it is called.

### Example
```python
def say_hello():
    print("Hello! This is my first Python function.")

say_hello()
```
## 2. Defining a Function

- You create a function using the def keyword, a name, parentheses (), and a colon :.

### Syntax
```python
def function_name(parameters):
    # code block
```
### Example
```python
def show_message():
    print("Learning Python step by step!")

show_message()
```
## 3. Function Parameters

- Parameters allow you to send information into a function.

### Example
```python
def welcome_user(username):
    print(f"Welcome, {username}! Let's start learning.")

welcome_user("Mithun")
```
## 4. Returning Values

- Functions can return results using the return keyword.

### Example
```python
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print("Product =", product)
```
## 5. Default Parameters

- If you don’t pass a value, Python uses the default.

### Example
```python
def greet(person="Friend"):
    print(f"Hi, {person}! Nice to meet you.")

greet()
greet("Neha")
```
## 6. Local and Global Variables

- Local variable → Created inside a function

- Global variable → Created outside a function and accessible everywhere

### Example
```python
score = 50  # Global variable

def update_score():
    score = 100  # Local variable
    print("Inside function:", score)

update_score()
print("Outside function:", score)
```
## 7. Nested Functions

- A function defined inside another function.

### Example
```python
def main_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()

main_function()
```

Nested functions are often used in advanced concepts like decorators.

# What I Learned Today 

- What a function is and why it is used

- How to define and call a function

- How parameters work

- How to return values

- How default parameters work

Local vs global variables

What nested functions are
