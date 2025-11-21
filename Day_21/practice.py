# List Comprehension Practice

# 1. Given a list of numbers, create a new list with each number squared.
numbers = [2, 5, 7, 10, 12]
squared = [n*n for n in numbers]
print("1) Squares:", squared)


# 2. From a list of words, create a list of words that have more than 3 letters.
words = ["cat", "lion", "sun", "elephant", "dog", "tree"]
long_words = [w for w in words if len(w) > 3]
print("2) Words with more than 3 letters:", long_words)


# 3. Create a list of even numbers from 1 to 30 using list comprehension.
evens = [x for x in range(1, 31) if x % 2 == 0]
print("3) Even numbers from 1 to 30:", evens)


# 4. Given a list of temperatures in Celsius, convert them to Fahrenheit.
celsius = [0, 10, 20, 25, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("4) Temperatures in Fahrenheit:", fahrenheit)


# 5. From a list of names, keep only names that start with the letter 'A'.
names = ["Asha", "Ravi", "Anil", "Meera", "Arjun", "Sita"]
starts_with_a = [name for name in names if name.startswith("A")]
print("5) Names starting with A:", starts_with_a)
