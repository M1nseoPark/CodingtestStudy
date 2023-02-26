from itertools import combinations
import sys

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])


def count(arr):
    result = 0
    for hy, hx in home:
        cnt = sys.maxsize
        for cy, cx in arr:
            if cnt > abs(cy-hy) + abs(cx-hx):
                cnt = abs(cy-hy) + abs(cx-hx)
        result += cnt

    return result
    

answer = sys.maxsize
for i in range(1, m+1):
    for c in combinations(chicken, i):
        answer = min(answer, count(c))

print(answer)


