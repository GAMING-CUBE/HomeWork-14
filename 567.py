a = [1, 5, 8, 0, 2, 9]
b = [8, 3, 6, 7, 1]

a_b = set(a) & set(b)

for i in a_b:
    print(i, end=" ")
