import sys

n, m = map(int, sys.stdin.readline().split())
word = {}
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if len(w) >= m:
        if w in word:
            word[w][0] -= 1
        else:
            word[w] = [0, -len(w), w]

word = sorted(word.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))
for i in range(len(word)):
    print(word[i][0])
