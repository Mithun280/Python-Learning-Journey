# Day 6 – Lists in Python
## 1. What is a List?

- A list is a collection of items.

Lists are:

- Ordered

- Mutable (you can change them)

- Allow duplicates

## Lists can store different data types.
```python
Example:

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = ["apple", 3, True]
```

## 2. Accessing List Elements

Python uses 0-based indexing.
```python
fruits[0]      # apple
fruits[2]      # cherry
```


## Negative Indexing (from end):
```python
fruits[-1]     # cherry
fruits[-2]     # banana
```

## 3. Modifying Lists
- Change an item
```python
fruits[1] = "orange"
```

- Add Items
```python
fruits.append("grape")     # add at end
fruits.insert(1, "kiwi")   # add at specific index
```

- Remove Items
```python
fruits.remove("orange")  # remove by value
fruits.pop()             # remove last item
fruits.pop(0)            # remove first item
fruits.clear()           # remove all items
```
## 4. Slicing Lists

`list[start : stop : step]`
```python
numbers = [0, 1, 2, 3, 4, 5, 6]

numbers[1:4]   # [1, 2, 3]
numbers[:4]    # [0, 1, 2, 3]
numbers[2:]    # [2, 3, 4, 5, 6]
numbers[::2]   # [0, 2, 4, 6]
```
## 5. Useful List Functions & Methods
| Function / Method | Description                                   | Example                 |
| ----------------- | --------------------------------------------- | ----------------------- |
| `len(list)`       | Length of list                                | `len(fruits)`           |
| `sorted(list)`    | Returns sorted list (doesn’t change original) | `sorted(numbers)`       |
| `sum(list)`       | Sum of numeric list                           | `sum(numbers)`          |
| `index(value)`    | Returns index of value                        | `fruits.index("apple")` |
| `count(value)`    | Counts occurrences                            | `numbers.count(1)`      |
| `reverse()`       | Reverses list in place                        | `fruits.reverse()`      |
| `sort()`          | Sorts list in place                           | `numbers.sort()`        |

## 6. Nested Lists

- Lists can contain other lists.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0]      # [1, 2, 3]
matrix[1][1]   # 5
```

# ✅ What I Learnt Today

- Lists are flexible and changeable

- How to access, modify, add, and remove items

- How slicing works

- Useful list functions & methods

- Nested lists (lists inside lists)
