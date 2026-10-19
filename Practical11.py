
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in each line
print("First half:", t1[:5])
print("Second half:", t1[5:])

# b. Print even numbers in the tuple
t2 = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers:", t2)

# c. Concatenate t2 with t1
t3 = (11, 13, 15)
t4 = t1 + t3
print("Concatenated tuple:", t4)

# d. Find maximum and minimum values
print("Maximum value:", max(t1))
print("Minimum value:", min(t1))
