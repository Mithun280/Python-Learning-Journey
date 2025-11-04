# Day 4 Practice - String Manipulation & Escape Sequences

#  Simple Greeting Program
name = input("Enter your name: ")
age = input("Enter your age: ")

# Using + operator
print("Hello " + name + "! You are " + age + " years old.")

# Using f-string
print(f"Hey {name}, you are {age} years young ")

# String Manipulation Practice
sentence = input("\nEnter any sentence: ")

print("\nUppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Without extra spaces:", sentence.strip())
print("Spaces replaced with underscores:", sentence.replace(" ", "_"))

# Just for fun
print("Wow! You typed:", sentence.upper(), "🔥")

# Character Counter (excluding spaces)
text = input("\nType something, I’ll count the characters: ")
count = len(text.replace(" ", ""))
print(f"Characters (excluding spaces): {count}")

if count < 5:
    print("Short and sweet! ")
elif count < 15:
    print("Nice length ")
else:
    print("That’s a long message! ")

# Escape Sequence Practice
print("\nLet's try some escape sequences:\n")
print("Hello\n\tWorld")
print("This is a backslash: \\")
print("He said, \"I love Python!\"")

# Bonus pattern
print("\nPython Ladder:")
print("P\n\tY\n\t\tT\n\t\t\tH\n\t\t\t\tO\n\t\t\t\t\tN")

print("\n✅ Day 4 practice completed! Feeling good 😎")
