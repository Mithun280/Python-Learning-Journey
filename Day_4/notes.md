# 🐍 Day 4 – String Manipulation and Escape Sequences in Python
## 1. String Manipulation
# 🔹 What is a String?

## A string is a collection of characters inside quotes.
Example:
```python
text = "Python is fun!"
```

# 🔹 Concatenation (Joining Strings)

## You can join two or more strings using the + operator.
```python
first_name = "Mithun"
last_name = "Raj"
full_name = first_name + " " + last_name
print(full_name)  # Output: Mithun Raj
```

# 🔹 Repetition (Repeating Strings)

## Use the * operator to repeat a string multiple times.
```python
greet = "Hi! " * 3
print(greet)  # Output: Hi! Hi! Hi!
```
# 🔹 Common String Methods

| Method               | Description           | Example                                   | Output          |
| -------------------- | --------------------- | ----------------------------------------- | --------------- |
| `.upper()`           | Converts to uppercase | `"hello".upper()`                         | `HELLO`         |
| `.lower()`           | Converts to lowercase | `"HELLO".lower()`                         | `hello`         |
| `.strip()`           | Removes spaces        | `"  hi  ".strip()`                        | `hi`            |
| `.replace(old, new)` | Replaces words        | `"I love Java".replace("Java", "Python")` | `I love Python` |


```python
msg = "   python is cool!   "
print(msg.upper())    # PYTHON IS COOL!
print(msg.lower())    # python is cool!
print(msg.strip())    # python is cool!
print(msg.replace("python", "coding"))  # coding is cool!
```
# Understanding Indexing in Python Strings
## What is Indexing?

  - Indexing means picking individual letters (characters) from a string using position numbers.
  - Each character in a string has a position (index) number.
  

# 🔹 Accessing Characters (Indexing)

## Strings have index numbers starting from 0.
```python
word = "Hello"
print(word[0])  # H
print(word[1])  # e
```


## 👉 You can also count backward using negative indexes:
```python
print(word[-1])  # o
print(word[-2])  # l
```

# Index vs Position in Python

Position means normal counting that humans use — starts from 1.
Example:
```python
Word:   P   Y   T   H   O   N
Position: 1   2   3   4   5   6
```


Index means Python’s way of counting — starts from 0.
Example:
```python
Word:   P   Y   T   H   O   N
Index:  0   1   2   3   4   5
```


So, H is at position 4 but index 3.

## Easy trick:
🧠 Position = Human counting (1-based)
🐍 Index = Python counting (0-based)

Example:
```python
text = "MITHUN"
print(text[0])  # M (1st position, index 0)
print(text[2])  # T (3rd position, index 2)
print(text[-1]) # N (last letter)
```

# 🔹 Slicing (Getting Parts of a String)

## You can cut parts of a string using slicing:
```python
fruit = "Pineapple"
print(fruit[0:4])  # Pine
print(fruit[4:])   # apple
print(fruit[:5])   # Pinea
```

# 💡 2. Escape Sequences

## Escape sequences help print special characters like new lines, tabs, or quotes.

| Escape Code | Meaning      | Example                                | Output                    |
| ----------- | ------------ | -------------------------------------- | ------------------------- |
| `\n`        | New line     | `print("Hello\nPython")`               | Hello ↵ Python            |
| `\t`        | Tab space    | `print("Name:\tMithun")`               | Name:    Mithun           |
| `\\`        | Backslash    | `print("This is a backslash: \\")`     | This is a backslash: \    |
| `\"`        | Double quote | `print("He said, \"I love coding!\"")` | He said, "I love coding!" |

Example:
```python
print("Hello\nWorld")
print("Name:\tMithun")
print("This is a backslash: \\")
print("He said, \"I love coding!\"")
```
#What I Learned Today – Day 4
Topic: `String Manipulation` and `Escape Sequences in Python`

- A string is a group of characters inside quotes.
 `Example: "Python is fun!"`

- Concatenation (+) joins strings together.
 `Example: "Hello" + " World"`

- Repetition (*) repeats a string multiple times.
 `Example: "Hi! " * 3 → Hi! Hi! Hi!"`

- Learned string methods:

`.upper() → converts to uppercase`

`.lower() → converts to lowercase`

`.strip() → removes spaces`

`.replace(old, new) → replaces words`

- Indexing helps get one character from a string.
 `Example: text[0] → first letter, text[-1] → last letter`

- Slicing is used to get a part of the string.
  `Example: text[0:5] → characters from 0 to 4`

- Escape sequences are special symbols:

- `\n → new line`

- `\t → tab space`

- `\\ → backslash`

- `\" → double quote`

- Practiced printing text with new lines, tabs, and quotes using escape sequences.

-  Understood how strings can be displayed, formatted, and modified easily in Python.

- Learned that strings are very flexible and used everywhere in Python programming.
