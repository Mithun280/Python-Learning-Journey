# Day 8
# Dictionaries in Python 

## A dictionary in Python is a collection that stores data in key-value pairs.
## Think of a dictionary like a real dictionary:

- You look up a word (key)

- You get its meaning (value)

Example of Key → Value:
```python
"Apple" → "A fruit"
```

In Python:
```python
my_dict = {"Apple": "A fruit"}
```
## ✅ 1. How to Create a Dictionary

You can create a dictionary using {}.
```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}
```

Or using dict():
```python
student = dict(name="Rahul", age=21, course="Python")
```
## ✅ 2. Accessing Values from a Dictionary

- Use the key to access the value.
```PYTHON
print(student["name"])      # Output: Rahul
```
- Using get() (safer method)
```PYTHON
print(student.get("course"))      # Output: Python
print(student.get("grade", "Not Available"))  
# If key not found → Prints default value
```
## ✅ 3. Adding & Updating Items
- Add a new key-value pair:
```PYTHON
student["city"] = "Bengaluru"
```
## Update an existing value:
```python
student["age"] = 22
```
## ✅ 4. Removing Items
| Method     | What it does                      | Example                 |
| ---------- | --------------------------------- | ----------------------- |
| `pop(key)` | Removes key and returns its value | `student.pop("age")`    |
| `del`      | Deletes a key-value pair          | `del student["course"]` |
| `clear()`  | Removes everything                | `student.clear()`       |

Example:
```python
print(student.items())  
# Output: dict_items([('name', 'Rahul'), ('city', 'Bengaluru'), ('marks', 85)])
```
## ✅ 6. Important Characteristics

| Feature                    | Explanation                                                                     |
| -------------------------- | ------------------------------------------------------------------------------- |
| **Unordered**              | Items don’t follow index order (but maintain insertion order in modern Python). |
| **Mutable**                | You can change values.                                                          |
| **Keys must be immutable** | Strings, numbers, tuples are allowed as keys. Lists cannot be keys.             |
| **Keys are unique**        | Duplicate keys overwrite older values.                                          |

Example:
```python
x = {"a": 10, "a": 50}
print(x)  # Output: {'a': 50}
```
## ✅ 7. Difference Between List, Tuple, Set & Dictionary
| Feature          | List        | Tuple       | Set                | Dictionary                 |
| ---------------- | ----------- | ----------- | ------------------ | -------------------------- |
| Structure        | Values only | Values only | Unique values only | Key-Value pairs            |
| Order            | Ordered     | Ordered     | Unordered          | Ordered (insertion)        |
| Mutable          | Yes         | No          | Yes                | Yes                        |
| Duplicate Values | Allowed     | Allowed     | Not allowed        | Keys not allowed to repeat |
| Access Type      | Index       | Index       | No indexing        | Key                        |

## ⭐ Quick Real-Life Example

- Store product prices in a dictionary:
```python
prices = {
    "Milk": 45,
    "Bread": 30,
    "Eggs": 60
}

print(prices["Milk"])   # Output: 45
prices["Bread"] = 35    # Update value
prices["Tea"] = 150     # Add new item

print(prices)
```
# 📌 What I Learned Today

- What a Dictionary is and how it stores data in key-value pairs

- How to create dictionaries using {} and dict()

- How to access values using keys and get()

- How to add, update, and remove items

- Common dictionary methods:
  keys(), values(), items(), update(), pop(), clear()

- Characteristics of dictionaries (mutable, unique keys, keys must be immutable)

- Difference between List, Tuple, Set, and Dictionary
