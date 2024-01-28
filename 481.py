words = "horse, cat, parrot, goldfish, dog"

words = words.split(", ")
words = sorted(words)[::-1]
for i in words:
    print(i, end=" ")
