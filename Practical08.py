
lst = eval(input("Enter a list: "))

# Using for loop
cubes = []
for x in lst:
    if type(x) == int and x % 2 == 0:
        cubes.append(x ** 3)
print("Using for loop:", cubes)

# Using list comprehension
cubes = [x ** 3 for x in lst if type(x) == int and x % 2 == 0]
print("Using list comprehension:", cubes)
