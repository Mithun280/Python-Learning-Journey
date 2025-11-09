# Day 9
# Conditional Statements in Python (if, elif, else)

- Conditional statements allow your program to make decisions based on conditions.
- Depending on whether a condition is True or False, different parts of code will run.

## 1. if Statement

- Used to run a block of code only when the condition is True.

Syntax:
```python
if condition:
    # code to execute when condition is True
```

### Example:

Check whether a student passed an exam (pass mark: 35).
```python
marks = 45

if marks >= 35:
    print("You passed the exam!")
```
## 2. else Statement

- Runs when the if condition is False.

Syntax:
```python
if condition:
    # True block
else:
    # False block
```

### Example:
```python
marks = 30

if marks >= 35:
    print("You passed!")
else:
    print("You failed.")
```
## 3. elif Statement

- Used when we have multiple conditions to check.

Syntax:
```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

### Example: Checking temperature level
```python
temperature = 32

if temperature < 20:
    print("Weather is cold.")
elif temperature < 30:
    print("Weather is normal.")
else:
    print("Weather is hot.")
```
## 4. Comparison Operators

These are used to compare values inside conditions:
| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal             |
| `<`      | Less than             |
| `>`      | Greater than          |
| `<=`     | Less than or equal    |
| `>=`     | Greater than or equal |

Example:
```python
age = 18

if age >= 18:
    print("Eligible for voting.")
```
## 5. Logical Operators

- Used to combine multiple conditions.
| Operator | Meaning                          | Example Meaning           |
| -------- | -------------------------------- | ------------------------- |
| `and`    | True only if **both** are True   | Condition1 AND Condition2 |
| `or`     | True if **at least one** is True | Condition1 OR Condition2  |
| `not`    | Reverses the condition           | not True → False          |

### Example:
A person gets gym membership discount only if age < 25 and is a student:
```python
age = 22
is_student = True

if age < 25 and is_student:
    print("Discount applied.")
else:
    print("No discount.")
```
## 6. Real-Life Example: Movie Ticket Pricing
```python
age = 10

if age < 4:
    print("Ticket is free.")
elif age <= 12:
    print("Child ticket price: ₹100")
elif age >= 60:
    print("Senior citizen ticket price: ₹120")
else:
    print("Regular ticket price: ₹180")
```
## 7. Nested if Statements

- An if inside another if.

### Example:
Restaurant open only if it’s Sunday and time is between 6 PM and 10 PM.
```python
day = "Sunday"
time = 19  # 7 PM

if day == "Sunday":
    if 18 <= time <= 22:
        print("Restaurant is open!")
    else:
        print("Closed, wrong time.")
else:
    print("Closed today.")
```
## 8. Importance of Indentation

Python uses spaces to define code blocks.
Incorrect indentation → error.

Correct:
```python
if True:
    print("Hello")
    print("Inside block")
```
## 9. match-case (Python 3.10+ Only)

Used to compare one variable to many constant values (like switch-case).

Example:
```python
traffic_light = "yellow"

match traffic_light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
```
## ✅ Quick Summary
| Keyword        | Purpose                       |
| -------------- | ----------------------------- |
| `if`           | Checks first condition        |
| `elif`         | Additional conditions         |
| `else`         | Runs when none are True       |
| `and, or, not` | Combine conditions            |
| `match-case`   | Cleaner multiple value checks |

## 📌 Today I Learned (Summary)

- Conditional statements let the program make decisions.

- `if` runs when a condition is True.

- `else` runs when the `if` condition is False.

- `elif` is used to check multiple conditions one by one.

- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.

- Logical operators: `and`, `or`, `not` (used to combine conditions).

- Nested `if` means placing one `if` inside another for deeper checks.

- `Indentation` is important in Python to define code blocks.

- `match-case` (Python 3.10+) is used to handle multiple fixed values clearly (similar to switch-case).
