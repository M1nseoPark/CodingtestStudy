import sys

n, m = map(int, sys.stdin.readline().split())
keyword = {}
for _ in range(n):
    key = sys.stdin.readline().rstrip()
    keyword[key] = 1

for _ in range(m):
    write = list(sys.stdin.readline().rstrip().split(','))
    for i in range(len(write)):
        if write[i] in keyword:
            del keyword[write[i]]

    print(len(keyword))
    
    
