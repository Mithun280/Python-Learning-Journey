# -----------------------------
# EASY QUESTION
# -----------------------------
# Print numbers from 1 to 4
i = 1
while i <= 4:
    print(i)
    i += 1


# -----------------------------
# MEDIUM QUESTION 1
# -----------------------------
# Print odd numbers from 1 to 10
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1


# -----------------------------
# MEDIUM QUESTION 2
# -----------------------------
# Ask user until number > 50
num = 0
while num <= 50:
    num = int(input("Enter a number greater than 50: "))
print("Thank you!")


# -----------------------------
# MEDIUM QUESTION 3
# -----------------------------
# Skip printing number 5
n = 1
while n <= 7:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1


# -----------------------------
# HARD QUESTION 1
# -----------------------------
# Password System (3 Attempts Only)
correct_password = "python123"
attempts = 0

while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Login Successful ✅")
        break
    else:
        print("Wrong Password ❌")
        attempts += 1

if attempts == 3:
    print("Account Locked 🔒")


# -----------------------------
# HARD QUESTION 2
# -----------------------------
# Mobile Recharge Balance System
balance = 50

while balance > 0:
    print(f"Balance: ₹{balance}")
    call = input("Do you want to make a call? (yes/no): ").lower()

    if call == "yes":
        balance -= 5
        print("Call made 📞")
    else:
        print("No call made.")

print("Balance over. Recharge needed! ⚠️")


# -----------------------------
# SUMMARY - WHAT I LEARNED TODAY
# (Just notes for revision)
# -----------------------------
# - while loop repeats as long as the condition is True.
# - Must update the loop variable to avoid infinite loops.
# - break stops the loop immediately.
# - continue skips one iteration and continues the loop.
# - Useful for input checking, repeat processes, countdowns, etc.
# - Real-life uses: login system, balance deduction, ticket booking.
