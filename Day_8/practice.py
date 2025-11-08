# practice.py - Dictionary Practice Exercises

# 1. Create a dictionary named person with keys: name, age, and city.
#    Fill them with any values. Then print the dictionary.

person = {
    "name": "Rahul",
    "age": 21,
    "city": "Bengaluru"
}
print(person)


# 2. Access the value of 'city' from the person dictionary and print it.

print(person["city"])


# 3. Add a new key 'profession' with any value to the person dictionary.
#    Then print the updated dictionary.

person["profession"] = "Developer"
print(person)


# 4. Update the age value in the dictionary to a new number.

person["age"] = 25
print(person)


# 5. Remove the key 'city' using pop() and print the removed value.

removed_value = person.pop("city")
print("Removed:", removed_value)
print(person)


# 6. Create another dictionary called scores with subjects and marks.
#    Example: Math: 85, English: 90, Science: 88

scores = {
    "Math": 85,
    "English": 90,
    "Science": 88
}
print(scores)


# 7. Use keys(), values(), and items() on the scores dictionary and print each result.

print(scores.keys())
print(scores.values())
print(scores.items())


# 8. Merge scores dictionary into person dictionary using update(). Print the result.

person.update(scores)
print("Merged Dictionary:", person)


# 9. Clear the scores dictionary and print it.

scores.clear()
print("Scores after clearing:", scores)


# 10. Bonus:
#     Create a dictionary called prices with item names as keys and prices as values.
#     Ask the user to enter a product name, then print the price if it exists,
#     otherwise print 'Product not found'.
#     (Hint: Use get() method)

prices = {
    "Milk": 45,
    "Bread": 35,
    "Eggs": 60
}

product = input("Enter product name: ")
print(prices.get(product, "Product not found"))
