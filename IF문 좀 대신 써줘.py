import sys, copy

n, m = map(int, sys.stdin.readline().split())
level = []
for _ in range(n):
    level.append(list(sys.stdin.readline().rstrip().split()))

char = []
for _ in range(m):
    char.append(int(sys.stdin.readline()))

schar = copy.deepcopy(char)
schar.sort()
answer = {}

s = 0
for i in range(m):
    for j in range(s, n):
        if int(level[j][1]) >= schar[i]:
            answer[schar[i]] = level[j][0]
            s = j
            break

for i in range(m):
    print(answer[char[i]])
        
