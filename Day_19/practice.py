


# ----------------------------
# 1. Basic Function
# ----------------------------
def greet():
    return "Hello Mithun!"

# ----------------------------
# 2. Positional Arguments
# ----------------------------
def multiply(x, y):
    return x * y

# ----------------------------
# 3. Keyword Arguments
# ----------------------------
def intro(name, role):
    return f"My name is {name} and I am a {role}."

# Example call:
# intro(name="Mithun", role="Data Scientist")

# ----------------------------
# 4. Default Parameters
# ----------------------------
def welcome(name="Guest"):
    return f"Welcome, {name}!"

# ----------------------------
# 5. Return Statement
# ----------------------------
def double(n):
    return n * 2

# ----------------------------
# 6. *args
# ----------------------------
def add_all(*nums):
    return sum(nums)

# ----------------------------
# 7. **kwargs
# ----------------------------
def print_profile(**details):
    return details

# ----------------------------
# 8. Lambda Function
# ----------------------------
add10 = lambda x: x + 10

# ----------------------------
# 9. Recursion
# ----------------------------
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

# ----------------------------
# 10. Greatest of 3 numbers
# ----------------------------
def greatest(a, b, c):
    return max(a, b, c)

# ----------------------------
# 11. Even or Odd
# ----------------------------
def is_even(n):
    return n % 2 == 0

# ----------------------------
# 12. Reverse String (without slicing)
# ----------------------------
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

# ----------------------------
# 13. Word Count
# ----------------------------
def word_count(sentence):
    return len(sentence.split())

# ----------------------------
# 14. Discount Calculation
# ----------------------------
def calculate_discount(price, discount):
    return price - (price * (discount / 100))

# ----------------------------
# 15. Simple Login
# ----------------------------
def login(username, password):
    return username == "mithun" and password == "1234"

# ----------------------------
# 16. Average using *args
# ----------------------------
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

# ----------------------------
# 17. Lambda: last character
# ----------------------------
last_char = lambda s: s[-1]

# ----------------------------
# 18. Recursion: Sum to N
# ----------------------------
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

# END
