import sys

answer = 0
for i in range(5):
    a, b = input().split()
    al = list(map(int, a.split(':')))
    at = al[0] * 60 + al[1]
    bl = list(map(int, b.split(':')))
    bt = bl[0] * 60 + bl[1]
    answer += (bt - at)

print(answer)
