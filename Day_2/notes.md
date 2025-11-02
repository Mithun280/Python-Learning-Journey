  # Day 02 – Python Basics 🐍 
## (Variables, Data Types & Operators)
- Variables in Python

A variable is like a box that stores data.
You don’t need to mention the type — Python decides it automatically (because it’s dynamically typed).

Example:
```python
city = "Bangalore"
year = 2025
temperature = 26.5
is_raining = False


print(city, year, temperature, is_raining)
```


## Rules for naming variables:

- Must start with a letter or _

- Can have letters, numbers, and _

- Case sensitive (Name ≠ name)

# Data Types in Python

## Common built-in types:

- int → Whole numbers → 10, -5

- float → Decimal numbers → 3.14, -0.1

- str → Text → "Python", 'Hello'

- bool → True or False → True, False

Example:
```python
x = 12
y = 3.5
z = "Mithun"
is_coding = True

print(type(x))  # int
print(type(y))  # float
print(type(z))  # str
print(type(is_coding))  # bool
```

## Type Conversion

- You can change one type to another using:

int(), float(), str(), etc.

Example:
```python
x = "15"
y = int(x)       # convert string to int
z = float(y)     # convert int to float
print(z)         # 15.0
```

## Arithmetic Operators

Used to perform calculations.

## Operator	Meaning	Example	Output
+	Addition	5 + 3	8
-	Subtraction	10 - 4	6
*	Multiplication	6 * 2	12
/	Division	10 / 3	3.333
//	Floor Division	10 // 3	3
%	Modulus	10 % 3	1
**	Power	2 ** 3	8

Example:
```python
a, b = 9, 4
print(a + b)
print(a ** b)
```

## Assigning Multiple Values

You can assign values to many variables at once.

Example:
```python
name, age, country = "Mithun", 28, "India"
print(name, age, country)
```


Or give the same value:
```python
x = y = z = 100
print(x, y, z)
```

## Variable Reassignment

You can change a variable’s value anytime.

Example:
```python
score = 50
print(score)

score = 75
print(score)
```

# My Reflection

Today I learned how Python handles variables, data types, and arithmetic operators.
I also understood how Python automatically decides the type of a variable — that’s what dynamically typed means.
