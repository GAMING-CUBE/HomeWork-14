input_string = input()

char_count = {}

for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    if not count == 1:
        print(char, count)
