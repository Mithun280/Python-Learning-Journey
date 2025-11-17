# Day 17
# Python File Handling 

- File handling in Python allows you to read, write, update, and delete files stored on your computer. 
- Python provides the built-in open() function and several helpful methods to work with files.

### 🔹 1. Opening a File
```python
file = open("filename", mode)
```

### filename → name of the file
### mode → how you want to open it

## 🔹 2. File Modes
| Mode  | Description                               |
| ----- | ----------------------------------------- |
| `'r'` | Read (error if file doesn’t exist)        |
| `'w'` | Write (creates file / overwrites content) |
| `'a'` | Append (adds content to the end)          |
| `'x'` | Create (fails if file exists)             |
| `'b'` | Binary mode (images, videos, PDFs)        |
| `'t'` | Text mode (default)                       |

## 🔹 3. Reading Files

### ✔ Read entire file — read()
```python
file = open("example.txt", "r")
content = file.read()
file.close()
```
### ✔ Read one line — readline()
```python
file = open("example.txt", "r")
line = file.readline()
file.close()
```
### ✔ Read all lines — readlines()
```python
file = open("example.txt", "r")
lines = file.readlines()
file.close()
```
## 🔹 4. Writing to Files

### ✔ Write text — write()
```python
file = open("example.txt", "w")
file.write("Hello, Python!")
file.close()
```
### ✔ Write multiple lines — writelines()
```python
lines = ["Line 1\n", "Line 2\n"]
file = open("example.txt", "w")
file.writelines(lines)
file.close()
```
## 🔹 5. Appending to a File
```python
file = open("example.txt", "a")
file.write("\nThis is an appended line.")
file.close()
```
## 🔹 6. Using with open() (Best Practice)

- Automatically closes the file.
```python
with open("example.txt", "r") as file:
    data = file.read()
```
## 🔹 7. Checking if a File Exists
```python
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")
```
## 🔹 8. Deleting a File
```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
```
## 🔹 9. Working With Binary Files

### ✔ Reading binary file
```python
with open("image.jpg", "rb") as file:
    data = file.read()
```
### ✔ Writing binary file
```python
with open("new_image.jpg", "wb") as file:
    file.write(data)
```
# 📘 Summary Table
| Operation   | Description        | Example                  |
| ----------- | ------------------ | ------------------------ |
| Open file   | Create file object | `open("file.txt", "r")`  |
| Read all    | Read full content  | `read()`                 |
| Read line   | Read one line      | `readline()`             |
| Read lines  | Read list of lines | `readlines()`            |
| Write       | Overwrite file     | `write()`                |
| Append      | Add new content    | `write()` in append mode |
| Check file  | Check existence    | `os.path.exists()`       |
| Delete file | Remove a file      | `os.remove()`            |

# 📌 File Handling

- File handling allows Python to read and write files.

- `open`(filename, mode) is used to open files.

- Modes: `'r'`, `'w'`, `'a'`, `'x'`, `'b'`, `'t'`.

- `read()` → read entire file.

- `readline()` → read one line.

- `readlines()` → read all lines as list.

- `write()` → write (overwrite) content.

- `writelines()` → write multiple lines.

- `'a'` mode → append new content.

- `with open()` → best practice (auto-close).

- `os.path.exists()` → check if file exists.

- `os.remove()` → delete file.

- Binary mode (`rb`, `wb`) is for images, PDFs, etc.
