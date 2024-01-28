a = "1 4 5 2 10 15 4 10 3".split()

b = set()

for i in a:
    if i in b:
        print("YES")
    else:
        print("NO")
        b.add(i)
