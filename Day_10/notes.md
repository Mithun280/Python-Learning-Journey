# Day 10
# While Loops in Python 

- A while loop is used when you want to repeat something as long as a condition remains True.

Basic Syntax
```python
while condition:
    # repeat this block
```
## 1. Basic Example

Print numbers from 1 to 5:
```python
num = 1
while num <= 5:
    print(num)
    num += 1   # increase num by 1
```

## Output:
```python
1
2
3
4
5
```

Explanation:

- The loop starts with num = 1.

- It prints and increases it every time.

- When num becomes 6 → condition becomes False → loop stops.

## 2. Real-Life Example – Water Drinking Reminder
```PYTHON
glasses = 1
while glasses <= 4:
    print(f"Drink glass {glasses} of water 💧")
    glasses += 1
```

Output:
```python
Drink glass 1 of water 💧
Drink glass 2 of water 💧
Drink glass 3 of water 💧
Drink glass 4 of water 💧
```
## 3. Avoiding Infinite Loops

- If you forget to update the variable, the loop will run forever.
```python
x = 1
while x <= 3:
    print(x)   # ❌ x is not changing → loop never stops!
```

## Always update the variable inside the loop.

## 4. Using `break` (Stop the Loop Early)
```python
count = 1
while count <= 10:
    print(count)
    if count == 3:
        break   # stop the loop here
    count += 1
```

Output:
```python
1
2
3
```
##5. Using `continue` (Skip One Iteration)
```python
num = 1
while num <= 5:
    if num == 3:
        num += 1
        continue  # skip printing number 3
    print(num)
    num += 1
```

Output:
```python
1
2
4
5
```
## 6. While Loop for User Input

- Keep asking until correct password is entered:
```python
password = ""
correct = "python"

while password != correct:
    password = input("Enter password: ")
    if password != correct:
        print("Wrong password try again.")

print("Access granted ✅")
```
## 7. Ticket Booking Example (Simple Case)
```python
tickets = 3

while tickets > 0:
    print(f"{tickets} tickets available.")
    buy = input("Buy ticket? (yes/no): ").lower()
    
    if buy == "yes":
        tickets -= 1
        print("Ticket booked 🎫")
    else:
        print("No booking.")

print("Sold Out ❗")
```
## 8. Nested While Example

- Two loops working together:
```python
outer = 1
while outer <= 3:
    inner = 1
    while inner <= 2:
        print(f"outer={outer}, inner={inner}")
        inner += 1
    outer += 1
```

Output:
```python
outer=1, inner=1
outer=1, inner=2
outer=2, inner=1
outer=2, inner=2
outer=3, inner=1
outer=3, inner=2
```
# Quick Summary 
| Concept            | Meaning                                       |
| ------------------ | --------------------------------------------- |
| `while condition:` | Repeat as long as condition is True           |
| `num += 1`         | Important → prevents infinite loop            |
| `break`            | Stops the loop immediately                    |
| `continue`         | Skips only the current round and goes to next |
| Used for           | Repeating tasks until condition changes       |

## 📝 What I Learned Today 

- while loop repeats code as long as a condition is True.

- The loop variable must change inside the loop to avoid infinite looping.

- break is used to stop the loop immediately.

- continue is used to skip one iteration and move to the next.

- While loops are useful for input validation, counting, repetition, and conditional loops.

- While loops can be used in real-life logic such as ticket booking, PIN verification, wallet balance systems.

- Nested while loops allow multiple-level repetition (outer loop + inner loop).
