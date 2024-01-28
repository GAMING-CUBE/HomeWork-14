w = []
d = []
num = 0

while True:
    inp = input()
    if not inp == "":
        if inp[0] == "W" or inp[0] == "w":
            w.append(int(inp[2:]))
        elif inp[0] == "D" or inp[0] == "d":
            d.append(int(inp[2:]))
    else:
        break

for i in w:
    num -= i
for i in d:
    num += i

print(num)
