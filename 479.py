x = 0
y = 0

while True:
    inp = input()
    if not inp:
        break
    direction, steps = inp.split()
    steps = int(steps)
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5

print(int(distance))
