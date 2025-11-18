# Advanced Function Concepts – Examples

# 1. Keyword Arguments

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Example call
# display_info(age=30, name="Mithun")


# 2. *args – Variable-Length Arguments

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

# Example call
# print(total_sum(1, 2, 3, 4))


# 3. **kwargs – Keyword Variable-Length Arguments

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Example call
# student_info(name="Anand", age=22, course="Python")


# 4. Lambda Functions

double = lambda x: x * 2

# Example call
# print(double(5))


# 5. Recursion – Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Example call
# print(factorial(5))


# 6. Nested Functions

def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

# Example call
# outer_function("Mithun")


# 7. Local vs Global Variables

x = 10  # global variable

def show():
    y = 5  # local variable
    print("Inside function:", x, y)

# Example call
# show()
# print("Outside function:", x)
