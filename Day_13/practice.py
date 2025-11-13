# practice.py
# For Loops • While Loops • Break • Continue • Range • List Comprehension

print("------ Example 1: Simple for loop printing numbers ------")
for i in range(1, 6):
    print(i)
print()


print("------ Example 2: For loop + list printing ------")
nums = [10, 20, 30, 40]
for n in nums:
    print("Number:", n)
print()


print("------ Example 3: Sum of list using for loop ------")
total = 0
for n in nums:
    total += n
print("List:", nums)
print("Total:", total)
print()


print("------ Example 4: Using break in a loop ------")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("Stopped because break hit at 5")
print()


print("------ Example 5: Using continue in a loop ------")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
print("Printed only odd numbers (continue skipped evens)")
print()


print("------ Example 6: While loop counting ------")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
print()


print("------ Example 7: While loop with break ------")
x = 1
while True:
    print(x)
    if x == 3:
        break
    x += 1
print()


print("------ Example 8: Simple list comprehension ------")
squares = [i * i for i in range(1, 11)]
print("Squares 1 to 10:", squares)
print()


print("------ Example 9: List comprehension with condition  ------")
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print("Numbers:", numbers)
print("Evens:", evens)
print()


print("------ Example 10: Reading numbers from a string  ------")
input_string = "5 10 15 20"
converted = []

for part in input_string.split():
    converted.append(int(part))

print("Input string:", input_string)
print("Converted list:", converted)
print()
