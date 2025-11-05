# Day 5 Practice - Operators

print("---- Assignment Operator Practice ----")
x = 10
print("Initial x =", x)

x += 5
print("After x += 5 :", x)

x -= 3
print("After x -= 3 :", x)

x *= 2
print("After x *= 2 :", x)

x /= 4
print("After x /= 4 :", x)


print("\n---- Comparison Operator Practice ----")
a = 7
b = 12

print("a == b:", a == b)
print("a != b:", a != b)
print("a < b :", a < b)
print("a > b :", a > b)
print("a >= 7:", a >= 7)


print("\n---- Logical Operator Practice ----")
age = 20
city = "Chennai"

print(age > 18 and city == "Chennai")   # True
print(age > 25 or city == "Chennai")    # True
print(not(age < 18))                    # True


print("\n---- Membership Operator Practice ----")
fruits = ["apple", "banana", "mango"]

print("mango" in fruits)
print("grape" not in fruits)

name = "python learning"
print("p" in name)
print("z" not in name)


print("\n---- Bitwise Operator Practice ----")
a = 6   # 110
b = 4   # 100

print("a & b:", a & b)   # 4
print("a | b:", a | b)   # 6
print("a ^ b:", a ^ b)   # 2

print("a << 1:", a << 1) # 12
print("b >> 1:", b >> 1) # 2
