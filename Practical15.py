
try:
    name = input("Enter your name: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters.")

    print("Name:", name)

except ValueError as e:
    print("Error:", e)
