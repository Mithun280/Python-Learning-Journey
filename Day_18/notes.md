# Day 18
# Functions – Advanced Concepts
## 1. Keyword Arguments

- Keyword arguments allow you to pass values by specifying parameter names.

- Order doesn't matter when using keyword arguments.

### Example:
```python
def greet(person, city):
    print(f"{person} lives in {city}")

greet(city="Mumbai", person="Rahul")
```

### Output:
```python
Rahul lives in Mumbai
```
## 2. Variable-Length Arguments
### a) `*args` (Non-keyword arguments)

- Used when you don’t know how many arguments will be passed.

- `*args` collects values into a tuple.

### Example:
```python
def multiply_all(*nums):
    product = 1
    for n in nums:
        product *= n
    return product

print(multiply_all(2, 3, 4))
```

### Output:
```python
24
```
### b) `**kwargs` (Keyword arguments)

- Used when you want to accept any number of named arguments.

- `**kwargs` collects values into a dictionary.

### Example:
```python
def show_employee(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_employee(name="Sneha", salary=45000, role="Developer")
```

### Output:
```python
name: Sneha
salary: 45000
role: Developer
```
## 3. Lambda Functions

- Anonymous, one-line functions.

- Useful for short calculations or as arguments to other functions.

### Syntax:
`lambda arguments: expression`

### Example:
```python
square = lambda x: x * x
print(square(6))
```

### Output:
```python
36
```
## 4. Recursion

- A recursive function is a function that calls itself.

- Used for problems that can be broken into smaller subproblems.

- Must include a base case to avoid infinite recursion.

### Example:
```python
def sum_until(n):
    if n == 0:
        return 0
    return n + sum_until(n - 1)

print(sum_until(5))
```

### Output:
```python
15
```
## 5. Nested Functions

- A function defined inside another function.

- The inner function has access to the outer function’s variables.

- Used for creating helper functions or closures.

### Example:
```python
def welcome_message(user):
    def message():
        print(f"Welcome, {user}!")
    message()

welcome_message("Mithun")
```

### Output:
```python
Welcome, Mithun!
```
## 6. Local vs Global Variables
### Local Variables

- Declared inside a function.

- Can be used only inside that function.

### Global Variables

- Declared outside all functions.

- Can be accessed anywhere in the program.

### Example:
```python
x = 10      # global variable

def show():
    y = 5   # local variable
    print("Inside function:", x, y)

show()
print("Outside function:", x)
```

### Output:
```python
Inside function: 10 5
Outside function: 10
```
# What I Learned Today 

- Keyword arguments let you pass values using parameter names (order doesn’t matter).

- `*args `allows a function to accept multiple non-keyword arguments.

- `**kwargs` allows a function to accept multiple keyword arguments.

- Lambda functions are small, one-line anonymous functions.

- Recursion means a function calling itself with a base case.

- Nested functions are functions defined inside other functions.

- Local variables exist only inside a function; global variables exist everywhere.
