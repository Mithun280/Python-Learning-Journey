# Day 7 – Tuples and Sets in Python
## 1. Tuples

- A tuple is like a list, but cannot be changed after creation.

- Tuples are ordered and allow duplicates.

- Use tuples when the data should not change.

 Syntax:
```python
my_tuple = (element1, element2, element3)
```

Examples:
```python
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4)
```

## Tuple with One Item
```python
single_item = ("apple",)   # Notice the comma
```

## 2. Accessing Tuple Elements

Works the same as lists (using index):
```python

fruits = ("apple", "banana", "cherry")

print(fruits[0])   # apple
print(fruits[-1])  # cherry

print(fruits[1:3]) # ('banana', 'cherry')
```
## 3. Tuple Operations
| Operation     | Example             | Result          |
| ------------- | ------------------- | --------------- |
| Concatenation | `(1,2,3) + (4,5,6)` | `(1,2,3,4,5,6)` |
| Repetition    | `(1,2) * 3`         | `(1,2,1,2,1,2)` |
| Membership    | `"apple" in fruits` | `True`          |

## 4. Tuple Methods
```python
my_tuple = (1, 2, 3, 1, 1)

my_tuple.count(1)   # 3
my_tuple.index(2)   # 1
```

## 5. Why Use Tuples?

- Immutable → data stays safe

- Faster than lists

- Can be dictionary keys (lists cannot)

## 6. Sets

- A set is a collection of unique items.

- Sets are unordered (no fixed index).

- Used when you need to avoid duplicates & work with math-like operations.
```python
Syntax:

my_set = {1, 2, 3}
```

Important:
```python
empty_set = set()  # not {}
```
## 7. Set Operations
| Operation            | Symbol | Example             | Result      |          |               |
| -------------------- | ------ | ------------------- | ----------- | -------- | ------------- |
| Union                | `      | `                   | `{1,2,3}    | {3,4,5}` | `{1,2,3,4,5}` |
| Intersection         | `&`    | `{1,2,3} & {3,4,5}` | `{3}`       |          |               |
| Difference           | `-`    | `{1,2,3} - {3,4,5}` | `{1,2}`     |          |               |
| Symmetric Difference | `^`    | `{1,2,3} ^ {3,4,5}` | `{1,2,4,5}` |          |               |

## 8. Set Methods
```python
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")      # add item
fruits.remove("banana")   # remove (error if missing)
fruits.discard("banana")  # remove safely
fruits.pop()              # removes random item
fruits.clear()            # empty set
```
## 9. Comparison Table
| Feature           | List               | Tuple      | Set                            |
| ----------------- | ------------------ | ---------- | ------------------------------ |
| Ordered           | ✅                  | ✅          | ❌                              |
| Mutable           | ✅                  | ❌          | ✅                              |
| Allows Duplicates | ✅                  | ✅          | ❌                              |
| Indexing          | ✅                  | ✅          | ❌                              |
| Best Use          | General collection | Fixed data | Unique items & math operations |

## ✅ What I Learned Today

- Tuples are unchangeable & faster.

- Sets store unique values and support union, intersection, difference.

- Lists vs Tuples vs Sets differences are now clear.
