## 🐍 Day 03
## Input, Output, and Comments in Python
# 1. Input from the User

In Python, we use the input() function to take input from the user.
By default, anything entered is treated as text (string) — so if you need a number, you must convert it.

Example:
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert input to integer
```

# 🧠 Key point:

- `input() → always returns string`

- `Use int() or float() to convert when needed`

# Example:
```python
marks = float(input("Enter your marks: "))
print("You scored", marks, "marks.")
```

# 2. Output to the Console

- To show output, we use the print() function.

Example:
```python
print("Hello, " + name + "! You are " + str(age) + " years old.")
```


## The + joins text together, but you must convert numbers to strings using str().
## Here, + is used to join text together — this is called concatenation

## You can also use f-strings, which are cleaner and easier to read:
## They automatically handle conversions — so you don’t need to convert numbers to strings manually.
```python
print(f"Hello, {name}! You are {age} years old.")
```

# 3. Comments in Python.

Comments help you explain your code.
Python ignores them when running your program.

## Single-line comment:
```python
# This is a single-line comment
print("Hello, Python!")
```


## Multi-line comment:
```python
"""
This is a multi-line comment.
You can write explanations here.
"""
print("Learning Python step by step!")
```

## 💬 My Reflection

Today I learned how to take input from users using input(),
display output using print(),
and write comments to make code easier to understand.
I also learned about f-strings and how helpful they are for formatting text.
