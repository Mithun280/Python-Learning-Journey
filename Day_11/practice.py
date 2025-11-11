# ---------- EASY (1) ----------
# E1) Print squares of numbers 1..7
# Expected:
# 1 4 9 16 25 36 49
for n in range(1, 8):
    print(n * n, end=" ")
print("\n" + "-"*20)

# ---------- MEDIUM (3) ----------
# M1) Count how many vowels across a list of words
# words = ["data", "science", "python", "loop"]
# Expected count: 10
words = ["data", "science", "python", "loop"]
vowels = 0
for w in words:
    for ch in w.lower():
        if ch in "aeiou":
            vowels += 1
print("Total vowels:", vowels)
print("-"*20)

# M2) Print multiples of 3 from 1..30 but skip those ending with digit 9 (i.e., 9, 19, 29)
# Expected:
# 3 6 12 15 21 24 27 30
for n in range(1, 31):
    if n % 3 == 0:
        if str(n).endswith("9"):
            continue
        print(n, end=" ")
print("\n" + "-"*20)

# M3) Find first number in 50..100 divisible by both 4 and 9 (use break)
# LCM(4,9)=36 -> first in range should be 72
for n in range(50, 101):
    if n % 4 == 0 and n % 9 == 0:
        print("First divisible by 4 and 9:", n)  # Expected: 72
        break
print("-"*20)

# ---------- HARD (2) ----------
# H1) Print a 5x5 pattern using nested loops as:
# *
# **
# ***
# ****
# *****
# then invert it:
# *****
# ****
# ***
# **
# *
# (No lists; only loops and print)
for i in range(1, 6):
    line = ""
    for _ in range(i):
        line += "*"
    print(line)
for i in range(5, 0, -1):
    line = ""
    for _ in range(i):
        line += "*"
    print(line)
print("-"*20)

# H2) Prime numbers between 2 and 50 using for..else
# Expected primes: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
for n in range(2, 51):
    # assume prime; try to prove composite
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            # composite -> stop checking
            break
    else:
        # no break happened -> prime
        print(n, end=" ")
print()
