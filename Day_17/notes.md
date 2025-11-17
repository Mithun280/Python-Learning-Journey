# JSON 
# ✅ What is JSON?

- JSON = JavaScript Object Notation

- A lightweight text format used for sending data between server ↔ app.

- Looks similar to Python dictionaries but always in string form.

### Example JSON text:
```javascript
{"brand": "Toyota", "model": "Innova", "year": 2022}
```
### 📌 Python’s json Module

- To work with JSON in Python:
```javascript
import json
```
## 🚀 1. Converting Python → JSON (Serialization)

- This means: Convert Python object into JSON string.

🔹 `json.dumps()` → Python object → JSON string

### Example:

```javascript
import json
```
```javascript
car = {"brand": "Honda", "model": "City", "price": 1200000}

json_string = json.dumps(car)
print(json_string)  
print(type(json_string))
```

### Output:
```javascript
{"brand": "Honda", "model": "City", "price": 1200000}
<class 'str'>

🔹 json.dump() → Write JSON directly to a file
```
### Example:
```javascript
with open("car.json", "w") as f:
    json.dump(car, f)
```

- This creates a JSON file with the data.

### 🔄 2. Converting JSON → Python (Deserialization)

- Meaning: Convert JSON string/file → Python object.

🔹 `json.loads()` → JSON string → Python object

### Example:
```javascript
json_text = '{"movie": "Interstellar", "rating": 9, "genre": "Sci-Fi"}'

python_data = json.loads(json_text)
print(python_data)
print(type(python_data))
```

### Output:
```javascript
{'movie': 'Interstellar', 'rating': 9, 'genre': 'Sci-Fi'}
<class 'dict'>
```
## 🔹 json.load() → JSON file → Python object

### Example:
```javascript
with open("movie.json", "r") as f:
    data = json.load(f)

print(data)
```
### ✨ 3. Pretty-print JSON (Readable format)

### Using `indent`:
```javascript
pretty = json.dumps(car, indent=4)
print(pretty)
```

### Output:
```javascript
{
    "brand": "Honda",
    "model": "City",
    "price": 1200000
}
```
# 🧠 Quick Summary Table
| Method                 | Meaning              | Example                 |
| ---------------------- | -------------------- | ----------------------- |
| `json.dumps(obj)`      | Python → JSON string | `json.dumps(car)`       |
| `json.dump(obj, file)` | Python → JSON file   | `json.dump(car, f)`     |
| `json.loads(str)`      | JSON string → Python | `json.loads(json_text)` |
| `json.load(file)`      | JSON file → Python   | `json.load(f)`          |

# 🎯 Extra Simple Examples 

## ✔ List to JSON
```python
nums = [10, 20, 30]
print(json.dumps(nums))
```
## ✔ JSON with nested dictionary
```python
student = {
    "name": "Ravi",
    "marks": {"math": 85, "science": 90}
}
print(json.dumps(student, indent=4))
```
## ✔ Convert JSON string of list
```python
json_list = '[1, 2, 3, 4]'
print(json.loads(json_list))   # Output: [1, 2, 3, 4]
```
✅ What I Learned Today — `JSON `

- `JSON` is a text format used for sharing data.

- Python has a built-in json module.

- `json.dumps()` → converts Python object to a JSON string.

- `json.dump()` → writes Python data into a JSON file.

- `json.loads()` → converts JSON string into a Python object.

- `json.load()` → reads JSON file and converts it into Python data.

- `Serialization = Python → JSON.`

- `Deserialization = JSON → Python.`

- `indent=4` is used to format JSON neatly.

- `JSON` looks like a dictionary but it is always a string.
