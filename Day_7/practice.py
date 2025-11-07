# Day 7 Practice - Tuples & Sets 


print("\n--- TUPLES PRACTICE ---\n")

# 1) Create a tuple of 5 fruits and print it
fruits_tuple = ("apple", "banana", "cherry", "kiwi", "grape")
print("My tuple:", fruits_tuple)

# 2) Access first and last item
print("First fruit:", fruits_tuple[0])
print("Last fruit:", fruits_tuple[-1])

# 3) Slice the tuple (middle 3 items)
print("Middle fruits:", fruits_tuple[1:4])

# 4) Tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print("Combined tuple:", combined)

# 5) Tuple repetition
repeat_tuple = ("Hi",) * 3
print("Repeated tuple:", repeat_tuple)

# 6) Tuple methods
numbers = (1, 2, 3, 1, 1)
print("Count of 1:", numbers.count(1))
print("Index of 2:", numbers.index(2))



print("\n--- SETS PRACTICE ---\n")

# 7) Create a set
fruits_set = {"apple", "banana", "cherry"}
print("Initial set:", fruits_set)

# 8) Add an item
fruits_set.add("orange")
print("After adding orange:", fruits_set)

# 9) Remove an item (safe way)
fruits_set.discard("banana")
print("After discarding banana:", fruits_set)

# 10) Pop removes a random value
removed_item = fruits_set.pop()
print("Random item removed:", removed_item)
print("Set after pop:", fruits_set)

# 11) Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)


print("\n--- DIFFERENCE SUMMARY ---\n")
print("List  = Ordered, Mutable, Allows duplicates")
print("Tuple = Ordered, Immutable, Allows duplicates")
print("Set   = Unordered, Mutable, No duplicates")
