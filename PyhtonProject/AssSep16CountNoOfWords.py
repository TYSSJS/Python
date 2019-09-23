f = open("file2.txt", "r")
words = 0
for i in f:
    word = i.split()
    words += len(word)
print(words)
