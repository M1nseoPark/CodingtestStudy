a, b = map(int, input().split())

answer = []
s = min(a, b)
e = max(a, b)

for i in range(s+1, e):
    answer.append(i)

print(len(answer))
answer.sort()
print(' '.join(map(str, answer)))


