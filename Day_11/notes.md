# Day 11
# FOR LOOPS IN PYTHON 
## 1. Basic Structure

- A for loop is used to repeat a block of code for each item in a sequence (list, string, range, etc.).

### Syntax:
```python
for item in sequence:
    # Code to run
```

### Example:
```python
fruits = ["Apple", "Banana", "Orange", "Grapes"]
for fruit in fruits:
    print(fruit)
```

### Output:
```python
Apple
Banana
Orange
Grapes
```
## 2. Using range() in For Loops

- range() is used when you want to loop a specific number of times.

### Syntax:
```python
range(start, stop, step)
```

### Example (Print 1 to 5):
```python
for i in range(1, 6):
    print(i)
```

### Example (Print even numbers 2 to 10):
```python
for i in range(2, 11, 2):
    print(i)
```
## 3. Looping Over Strings

- You can iterate through each character of a string.
```python
word = "Python"
for char in word:
    print(char)
```

### Output:
```python
P
y
t
h
o
n
```
## 4. Nested For Loops

- A loop inside another loop.

### Example: Print pairs of coordinates
```python
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})")
    print()
```
## 5. Using break in a Loop

- break stops the loop when a condition is met.
```python
students = ["Ram", "Ravi", "Latha", "Suma"]
for student in students:
    if student == "Latha":
        print("Found Latha!")
        break
    print(student)
```
## 6. Using continue in a Loop

- continue skips one iteration and moves to the next.
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 != 0:   # Skip odd numbers
        continue
    print(num)
```

### Output:
```python
2
4
6
```
## 7. Looping with enumerate()

- Use enumerate() when you want index + value together.
```python
movies = ["KGF", "Kantara", "Ugramm"]
for index, movie in enumerate(movies):
    print(f"{index + 1}. {movie}")
```
## 8. else Block with For Loops

- The else part runs only if the loop completes without break.
```python
names = ["Arun", "Vijay", "Kiran"]
for n in names:
    print(n)
else:
    print("Loop completed!")
```
## 9. Real-Life Example

- Distributing Chocolates
```python
chocolates = 3
friends = ["Asha", "Manu", "Reema", "Dev"]

for f in friends:
    if chocolates > 0:
        print(f"{f} gets a chocolate 🍫")
        chocolates -= 1
    else:
        print("No chocolates left 😢")
```
# ✅ Summary (What I Learned Today)

- `for` loops repeat actions for each item in a sequence.

- `range()` is used for looping a certain number of times.

- You can loop through lists, strings, and ranges.

- Nested loops allow operations inside loops.

- `break` stops the loop early.

- `continue` skips the current iteration.

- `enumerate()` provides index + value.

- `else` runs after the loop finishes (if no break).
