import sys

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


ab = {}
for a in A:
    for b in B:
        ab[a+b] = ab.get(a+b, 0) + 1
        

answer = 0
for c in C:
    for d in D:
        answer += ab.get(-(c+d), 0)

print(answer)
    
