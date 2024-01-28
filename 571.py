a = "a bb acD bb abc ac BCD a".split()

b = {}

for i in a:
    c = i.lower()
    b[c] = b.get(c, 0) + 1

for i, o in b.items():
    print(i, o)
