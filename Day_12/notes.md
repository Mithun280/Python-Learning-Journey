# Day 12
# Lists & Dictionaries with Loops and Comprehensions
## 🟢 1. Looping Through Lists

- A for loop helps you go through each element (item) in a list one by one.
- Think of it like: “Hey Python, go through every item in this list and do something with it.”

### 🔹 Example 1: Find the total marks of students
```python
marks = [50, 60, 70, 80, 90]
total = 0

for m in marks:
    total += m

print("Total Marks:", total)
```

### 🧾 Output:
```python
Total Marks: 350
```

### 📘 Explanation:

- for m in marks: → goes through each number (50, 60, 70…)

- total += m → adds each mark to total

- Finally prints the total sum.

### 🔹 Example 2: Creating a list of square numbers
```python
numbers = [2, 4, 6, 8]
squares = []

for n in numbers:
    squares.append(n ** 2)

print("Squares:", squares)
```

### 🧾 Output:
```python
Squares: [4, 16, 36, 64]
```

## 🧩 Concept: append() adds the new value (n squared) to the list.

### 🔹 Example 3: Printing favorite fruits
```python
fruits = ["Apple", "Banana", "Grapes", "Orange"]

for fruit in fruits:
    print(f"I like {fruit}")
```

### 🧾 Output:
```python
I like Apple
I like Banana
I like Grapes
I like Orange
```

## ✅ Use Case: Loops are perfect for repeating actions on lists — like printing, calculating, or modifying items.

## 🟠 2. Looping Through Dictionaries

- A dictionary stores key-value pairs (like a name and its mark).
- You can loop through keys, values, or both.

### 🔹 Example 1: Loop through dictionary keys
```python
students = {"Amit": 80, "Ravi": 75, "Sneha": 90}

for name in students:
    print(name)
```

### 🧾 Output:
```python
Amit
Ravi
Sneha
```

 ### 🧩 By default, looping through a dictionary gives keys.

## 🔹 Example 2: Loop through dictionary values
```python
students = {"Amit": 80, "Ravi": 75, "Sneha": 90}

for marks in students.values():
    print(marks)
```

### 🧾 Output:
```
80
75
90
```
### 🔹 Example 3: Loop through both keys and values
```python
students = {"Amit": 80, "Ravi": 75, "Sneha": 90}

for name, marks in students.items():
    print(f"{name} scored {marks}")
```

### 🧾 Output:
```python
Amit scored 80
Ravi scored 75
Sneha scored 90
```

# 🧠 Tip: .items() → gives both key and value together.

## 🔵 3. Using range() in for Loops

- range() gives you a sequence of numbers to loop through — often used when working with indexes.

### 🔹 Example: Match student names and marks
```python
names = ["Amit", "Ravi", "Sneha"]
marks = [80, 75, 90]
student_data = {}

for i in range(len(names)):
    student_data[names[i]] = marks[i]

print(student_data)
```

### 🧾 Output:
```python
{'Amit': 80, 'Ravi': 75, 'Sneha': 90}

```
### 📘 Explanation:
```python

range(len(names)) → gives numbers [0, 1, 2]

names[i] → picks name at index i

marks[i] → picks matching mark
```

## 🟣 4. List Comprehension

- List comprehension is a shorter, elegant way to create new lists from old ones.

### 📘 Syntax:

`new_list = [expression for item in iterable if condition]`

### 🔹 Example 1: Cube of numbers
```python
numbers = [1, 2, 3, 4, 5]
cubes = [n ** 3 for n in numbers]
print(cubes)
```

### 🧾 Output:
```python
[1, 8, 27, 64, 125]
```
### 🔹 Example 2: Extract odd numbers only
```python
numbers = [10, 11, 12, 13, 14, 15]
odd_numbers = [n for n in numbers if n % 2 != 0]
print(odd_numbers)
```

### 🧾 Output:
```python
[11, 13, 15]
```
### 🔹 Example 3: Convert movie titles to uppercase
```python
movies = ["Leo", "Kantara", "Jailer", "KGF"]
upper_movies = [movie.upper() for movie in movies]
print(upper_movies)
```

### 🧾 Output:
```python
['LEO', 'KANTARA', 'JAILER', 'KGF']
```
## 🟤 5. Dictionary Comprehension

- Dictionary comprehension helps you create dictionaries in one line, similar to list comprehension.

### 📘 Syntax:

`new_dict = {key_expression: value_expression for item in iterable if condition}`

### 🔹 Example 1: Squares of numbers as key-value pairs
```python
numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n ** 2 for n in numbers}
print(squares_dict)
```

### 🧾 Output:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
### 🔹 Example 2: Names and their first letters
```python
names = ["Amit", "Ravi", "Sneha"]
first_letter = {name: name[0] for name in names}
print(first_letter)
```

### 🧾 Output:
```python
{'Amit': 'A', 'Ravi': 'R', 'Sneha': 'S'}
```
### 🔹 Example 3: Filter products above ₹500
```python
product_price = {
    "Mouse": 300,
    "Keyboard": 700,
    "Monitor": 8000,
    "USB Cable": 150
}
```
### expensive = {product: price for product, price in product_price.items() if price > 500}
print(expensive)


### 🧾 Output:
```python
{'Keyboard': 700, 'Monitor': 8000}
```
## 🟢 6. Splitting Strings into Lists

- The split() method breaks a string into smaller parts (called list elements) based on a separator like a space or comma.

### 📘 Syntax:
```python
string.split(separator, maxsplit)
```
### 🔹 Example 1: Splitting a sentence
```python
sentence = "Python makes coding easy"
words = sentence.split()
print(words)
```

### 🧾 Output:
```python
['Python', 'makes', 'coding', 'easy']
```

### 👉 Default separator is space.

### 🔹 Example 2: Splitting with commas
```python
data = "Red,Green,Blue,Yellow"
colors = data.split(",")
print(colors)
```

### 🧾 Output:
```python
['Red', 'Green', 'Blue', 'Yellow']
```
### 🔹 Example 3: Limiting splits
```python
sentence = "Learning Python is fun and useful"
limited = sentence.split(" ", 3)
print(limited)
```

### 🧾 Output:
```python
['Learning', 'Python', 'is', 'fun and useful']
```

### 📘 Explanation:

- The string splits 3 times only.

- Remaining part stays together.

  ## 🌟 Real-Life Example (Combining Everything)

- Let’s combine list comprehension and dictionary comprehension with split().
```python
data = "Ravi:85, Sneha:90, Amit:78, Priya:88"

# Step 1: Split by commas
pairs = data.split(", ")

# Step 2: Create dictionary using comprehension
marks_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in pairs}

print(marks_dict)
```

### 🧾 Output:
```python
{'Ravi': 85, 'Sneha': 90, 'Amit': 78, 'Priya': 88}
```

### 💡 We combined:

- `split()` to break the string

- `Dictionary` comprehension to form a key-value pair

- `int()` to convert marks from string to number

## 🎯 Summary Cheat Sheet
| Concept                         | Example                                 | Purpose                          |
| ------------------------------- | --------------------------------------- | -------------------------------- |
| `for num in list:`              | `for n in [1,2,3]: print(n)`            | Loop through list items          |
| `for key, val in dict.items():` | Print both key and value                | Loop through dictionary          |
| `range()`                       | `for i in range(5):`                    | Loop through sequence of numbers |
| **List Comprehension**          | `[x*2 for x in list]`                   | Short way to create list         |
| **Dictionary Comprehension**    | `{k:v for k,v in dict.items() if v>10}` | Short way to create dict         |
| **split()**                     | `"a,b,c".split(",")`                    | Break string into list           |

# 🧾 What I Learned Today

## ✅ For Loops with Lists

- Used to go through each item in a list.

- Can perform actions like addition, printing, or modifying elements.

- Example: Summing numbers or doubling each number in a list.

## ✅ For Loops with Dictionaries

- Can loop through keys, values, or both using .items().

- Example: Printing each student’s name and marks.

## ✅ For Loops with range()

- range() helps loop using index numbers.

- Commonly used when you need both position and value.

## ✅ List Comprehension

- Short and elegant way to create new lists from old ones.

- Syntax: [expression for item in iterable if condition]

- Example: [n**2 for n in numbers] → squares of all numbers.

## ✅ Dictionary Comprehension

- Short way to create new dictionaries.

- Syntax: {key: value for item in iterable if condition}

- Example: {n: n**2 for n in numbers} → dictionary of squares.

## ✅ split() Method

- Splits a string into a list using a separator (like space or comma).

- Example: "apple,banana".split(",") → ['apple', 'banana']

- Can also limit number of splits using maxsplit.

## ✅ Practical Combination Example

- Used split() + dictionary comprehension together to convert string data into a dictionary.
