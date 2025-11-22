"""
Loops Practice File 
"""

# 1. PRINT 1 TO 20 (FOR LOOP)
for i in range(1, 21):
    print(i)


# 2. PRINT EVEN NUMBERS 1 TO 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# 3. SUM OF FIRST 10 NUMBERS
sum_total = 0
for i in range(1, 11):
    sum_total += i
print("Sum of first 10 numbers =", sum_total)


# 4. WHILE LOOP COUNTDOWN
n = 10
while n >= 1:
    print(n)
    n -= 1


# 5. PRINT "HELLO MITHUN" 7 TIMES
count = 1
while count <= 7:
    print("Hello Mithun")
    count += 1


# 6. BREAK EXAMPLE
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 7. CONTINUE EXAMPLE
for i in range(1, 11):
    if i == 3:
        continue
    print(i)


# 8. LIST LOOP (FRUITS)
fruits = ["apple", "banana", "mango", "orange", "grapes"]
for fruit in fruits:
    print(fruit)


# 9. NESTED LOOP (STAR PATTERN)
for i in range(1, 6):
    print("*" * i)


# 10. MULTIPLICATION TABLE
num = 5  # You can also take input using: num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
