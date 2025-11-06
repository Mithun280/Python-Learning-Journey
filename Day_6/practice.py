# Day 6 Practice - Lists in Python 


# 1) Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("My fruits list:", fruits)


# 2) Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# 3) Changing an item
fruits[1] = "kiwi"
print("After changing 2nd fruit:", fruits)


# 4) Adding items to the list
fruits.append("mango")  # add at end
print("After adding mango:", fruits)

fruits.insert(2, "papaya")  # insert in middle
print("After inserting papaya at index 2:", fruits)


# 5) Removing items
fruits.remove("orange")  # remove by name
print("After removing orange:", fruits)

fruits.pop()  # removes last item
print("After popping last item:", fruits)


# 6) Slicing examples
print("First 3 fruits:", fruits[:3])


# 7) Reverse the list
fruits.reverse()
print("Reversed list:", fruits)


# 8) Nested list example (like a table or matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing value (2nd row, 2nd column)
print("Value in matrix (row 2, col 2):", matrix[1][1])  # should print 5
