num_rows = int(input())

word_counts = {}

for _ in range(num_rows):
    row = input().split()
    for word in row:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

max_count = max(word_counts.values())
most_common_words = [word for word, count in word_counts.items() if count == max_count]

most_common_words.sort()
print(most_common_words[0])
