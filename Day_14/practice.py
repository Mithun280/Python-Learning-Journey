

# ------------------------------
# Example 1: Simple for loop
# ------------------------------
print("------ Example 1: Simple for loop printing numbers ------"): Simple for loop printing numbers ------")
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

print("------ Example 9: List comprehension with condition ------")
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print("Numbers:", numbers)
print("Evens:", evens)
print()

print("------ Example 10: Reading numbers from a string ------")
input_string = "5 10 15 20"
converted = []
for part in input_string.split():
    converted.append(int(part))
print("Input string:", input_string)
print("Converted list:", converted)
print()

# ----------examples ----------

print("------ Example 11: Enumerate with start index ------")
names = ['alice', 'bob', 'charlie']
for idx, name in enumerate(names, start=1):
    print(idx, name)
print()

print("------ Example 12: Zip to iterate two lists together ------")
questions = ['q1', 'q2', 'q3']
answers = ['a1', 'a2', 'a3']
for q, a in zip(questions, answers):
    print(q, '->', a)
print()

print("------ Example 13: Nested loops (multiplication table) ------")
for i in range(1, 4):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    print('Row', i, '->', row)
print()

print("------ Example 14: For-else (search example) ------")
items = [2, 4, 6, 8]
for x in items:
    if x == 5:
        print('Found 5')
        break
else:
    # else runs when loop finishes without break
    print('5 not found in items')
print()

print("------ Example 15: While-else (count until limit) ------")
ctr = 0
limit = 3
while ctr < limit:
    print('ctr =', ctr)
    ctr += 1
else:
    print('Loop finished normally (no break)')
print()

print("------ Example 16: Reverse iterate using reversed() ------")
for v in reversed([1, 2, 3, 4]):
    print(v)
print()

print("------ Example 17: Nested list comprehension (matrix flatten) ------")
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [val for row in matrix for val in row]
print('Matrix:', matrix)
print('Flattened:', flat)
print()

print("------ Example 18: Dict and set comprehensions ------")
words = ['apple', 'banana', 'cherry']
lengths = {w: len(w) for w in words}
unique_first_letters = {w[0] for w in words}
print('Word lengths dict:', lengths)
print('Unique first letters set:', unique_first_letters)
print()

print("------ Example 19: Generator expression (memory efficient) ------")
sq_gen = (i * i for i in range(1, 6))
print('Generator produced values:')
for s in sq_gen:
    print(s)
print()

# ------------------------------
# Example  Manual iterator usage
# ------------------------------
print("------ Example 20: Using an iterator manually with iter() and next() ------")
vals = [10, 20, 30]
it = iter(vals)
print(next(it))
print(next(it))
try:
    print(next(it))
    print(next(it))  # will raise StopIteration
except StopIteration:
    print('Reached end of iterator')
print()

print('--- End of 20 loop examples ---')
