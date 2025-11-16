# practice.py
# For Loops • While Loops • Break • Continue • Range

print("===== For Loop Practice =====")

# 1. Print the sum of numbers from 1 to 50
sum_nums = 0
for i in range(1, 51):
    sum_nums += i
print("1) Sum of 1 to 50:", sum_nums)
print()

# 2. Print only names that have more than 5 characters
names = ["Arun", "Sneha", "Rahul", "Karthikeyan", "Megha", "Praveen"]
print("2) Names with more than 5 characters:")
for n in names:
    if len(n) > 5:
        print(n)
print()

# 3. Print squares of even numbers from a list
nums = [3, 6, 10, 13, 2, 8]
print("3) Squares of even numbers:")
for num in nums:
    if num % 2 == 0:
        print(num * num)
print()

print("===== While Loop Practice =====")

# 4. Print numbers from 10 down to 1
print("4) Countdown from 10:")
x = 10
while x >= 1:
    print(x)
    x -= 1
print()

# 5. Ask user input until they type 'stop'
inputs = ["hi", "ok", "stop"]  # simulation for GitHub example
print("5) Simulated user input until 'stop':")
i = 0
while True:
    word = inputs[i]
    print("Input:", word)
    if word == "stop":
        break
    i += 1
print()

# 6. Print numbers from a list until you find a number greater than 50
numbers = [12, 25, 39, 48, 52, 30]
print("6) Stop when a number > 50:")
index = 0
while index < len(numbers):
    if numbers[index] > 50:
        print("Found:", numbers[index])
        break
    index += 1
print()

print("===== Mixed Practice =====")

# 7. Print only unique values from a list (manual method using loops)
data = [1, 2, 2, 5, 1, 7, 8, 8, 3]
print("7) Unique values:")
unique = []
for d in data:
    if d not in unique:
        unique.append(d)
        print(d)
print()

# 8. Using while loop: print first 5 multiples of 7
print("8) First 5 multiples of 7:")
c = 1
count = 0
while True:
    if c % 7 == 0:
        print(c)
        count += 1
        if count == 5:
            break
    c += 1
print()

print("===== End of Practice File =====")
