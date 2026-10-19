
# Read the file
f = open("File.txt", "r")
data = f.read()
f.close()

# a. Count characters, words and lines
print("Total characters:", len(data))
print("Total words:", len(data.split()))
print("Total lines:", len(data.splitlines()))

# b. Frequency of each character
freq = {}
for ch in data:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequency:")
print(freq)

# c. Print words in reverse order
words = data.split()
print("Words in reverse order:")
print(" ".join(words[::-1]))

# d. Copy even lines to File1 and odd lines to File2
f = open("File.txt", "r")
lines = f.readlines()
f.close()

f1 = open("File1", "w")
f2 = open("File2", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f1.write(lines[i])
    else:
        f2.write(lines[i])

f1.close()
f2.close()

print("Even lines copied to File1")
print("Odd lines copied to File2")
