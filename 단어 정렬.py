n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append([len(word), word])

words.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    if i != 0 and words[i-1][1] != words[i][1]:
        print(words[i][1])
    elif i == 0:
        print(words[i][1])

