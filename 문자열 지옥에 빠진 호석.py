from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(input())

like = {}
whole = []
for _ in range(k):
    t = sys.stdin.readline().rstrip()
    like[t] = 0
    whole.append(t)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def find():
    while q:
        y, x, rst = q.popleft()

        if rst in like:
            like[rst] += 1

        if len(rst) > 5:
            break

        for i in range(8):
            nx = (x + dx[i] + m) % m
            ny = (y + dy[i] + n) % n
            q.append([ny, nx, rst+arr[ny][nx]])
            

q = deque()
for i in range(n):
    for j in range(m):
        q.append([i, j, arr[i][j]])

find()
for i in whole:
    print(like.get(i))
