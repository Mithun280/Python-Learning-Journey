# DAY 5 – Python Operators 
## 1. Assignment Operators

- These operators are used to store a value inside a variable.
- The basic one is = which assigns the value from right side to left side.

| Operator | Meaning             | Example  | Result              |
| -------- | ------------------- | -------- | ------------------- |
| =        | Assign value        | `x = 10` | x becomes 10        |
| +=       | Add and assign      | `x += 5` | same as `x = x + 5` |
| -=       | Subtract and assign | `x -= 3` | same as `x = x - 3` |
| *=       | Multiply and assign | `x *= 2` | x = x × 2           |
| /=       | Divide and assign   | `x /= 4` | x becomes float     |
| %=       | Modulus and assign  | `x %= 3` | x = remainder       |

Example:
```python
x = 12
x += 8   # x = 20
x -= 5   # x = 15
x *= 2   # x = 30
x /= 6   # x = 5.0
```

## 2. Comparison Operators

- Used to compare two values.
- The output will be either True or False.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |

Example:
```python
a = 7
b = 9

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(b >= 9)   # True
```

## 3. Logical Operators

- Used to combine conditions.

| Operator | Meaning                                   |
| -------- | ----------------------------------------- |
| and      | True only if **both** conditions are true |
| or       | True if **any one** condition is true     |
| not      | Reverses True to False / False to True    |

Example:
```python
age = 25
city = "Mumbai"

print(age > 18 and city == "Mumbai")   # True
print(age < 18 or city == "Delhi")     # False
print(not(age < 18))                   # True
```

## 4. Membership Operators

- Used to check if an item exists in a sequence like list, string, tuple.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| in       | True if value is present     |
| not in   | True if value is not present |

Example:
```python
colors = ["red", "blue", "green"]
text = "learning python"

print("blue" in colors)         # True
print("yellow" not in colors)   # True
print("p" in text)              # True
```
## 5. Bitwise Operators

- These work on binary (0s and 1s).
- Used in low-level operations (not used daily, but good to know).

| Operator | Meaning     |
| -------- | ----------- |
| &        | AND         |
| |        | OR          |
| ^        | XOR         |
| ~        | NOT         |
| <<       | Left Shift  |
| >>       | Right Shift |

Example:
```python
a = 6   # binary: 110
b = 4   # binary: 100

print(a & b)   # 4  -> 100
print(a | b)   # 6  -> 110
print(a ^ b)   # 2  -> 010

print(a << 1)  # 12 -> (1100)
print(b >> 1)  # 2  -> (10)
```

## 6. Arithmetic Operators 

| Operator | Meaning        | Example     |
| -------- | -------------- | ----------- |
| +        | Add            | 4 + 2 = 6   |
| -        | Subtract       | 6 - 3 = 3   |
| *        | Multiply       | 4 * 2 = 8   |
| /        | Divide         | 7 / 2 = 3.5 |
| //       | Floor Division | 7 // 2 = 3  |
| %        | Remainder      | 7 % 2 = 1   |
| **       | Power          | 3 ** 2 = 9  |

## Summary 

- Learned about assignment operators used to assign and update values in variables.

- Understood comparison operators, which compare two values and return True or False.

- Practiced logical operators to combine multiple conditions in decisions.

- Learned membership operators to check if a value exists in a list or string.

- Studied bitwise operators, which work on binary (0s and 1s) form of numbers.

- Revised arithmetic operators for basic math operations like +, -, *, /, //, %, and **.





