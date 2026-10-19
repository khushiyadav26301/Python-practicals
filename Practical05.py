
s = input("Enter a string: ")

# a. Find the frequency of a character
ch = input("Enter the character to find its frequency: ")
print("Frequency:", s.count(ch))

# b. Replace a character with another character
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")
print("After replacement:", s.replace(old, new))

# c. Remove the first occurrence of a character
ch = input("Enter the character to remove first occurrence: ")
print("After removing first occurrence:", s.replace(ch, "", 1))

# d. Remove all occurrences of a character
ch = input("Enter the character to remove completely: ")
print("After removing all occurrences:", s.replace(ch, ""))
