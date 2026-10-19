
n = int(input("Enter the number of rows: "))

print("Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("Reverse Pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
