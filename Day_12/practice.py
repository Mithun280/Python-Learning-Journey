# practice.py

# -----------------------------

# 1. For Loops with Lists
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("1) Total sum:", total)

# Doubling numbers using a for loop
nums = [1, 2, 3, 4, 5]
doubled = []
for n in nums:
    doubled.append(n * 2)
print("2) Doubled List:", doubled)


# 2. For Loops with Dictionaries
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

print("3) Dictionary Keys:")
for student in student_marks:
    print(student)

print("4) Dictionary Values:")
for marks in student_marks.values():
    print(marks)

print("5) Keys and Values:")
for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")


# 3. For Loop with range() - using index
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]
student_marks_index = {}

for i in range(len(students)):
    student_marks_index[students[i]] = marks[i]

print("6) Student Marks (using index):", student_marks_index)


# 4. List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

print("7) Squares:", squares)
print("8) Even Numbers:", even_numbers)


# 5. Dictionary Comprehension
squares_dict = {n: n ** 2 for n in numbers}
name_lengths = {name: len(name) for name in ["Anand", "Geetha", "Kumar"]}

print("9) Squares Dictionary:", squares_dict)
print("10) Name Lengths:", name_lengths)


# 6. split() method examples
sentence = "I love coding in Python"
words = sentence.split()
print("11) Split sentence:", words)

data = "apple,banana,mango"
fruits = data.split(",")
print("12) Split CSV:", fruits)

limited = "Python is fun to learn".split(" ", 2)
print("13) Limited split:", limited)


# 7. Combined Example - split + comprehension
data = "Ravi:85, Sneha:90, Amit:78, Priya:88"
pairs = data.split(", ")
marks_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in pairs}
print("14) Converted Marks Dictionary:", marks_dict)


# ----------------------------------------------------------------------------------
