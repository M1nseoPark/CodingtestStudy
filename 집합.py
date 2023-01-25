# 시간초과와의 싸움..
import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    oper = list(sys.stdin.readline().split())
    if len(oper) == 1:
        fun = oper[0]
    else:
        fun, x = oper[0], int(oper[1])
    
    if fun == 'add':
        s.add(x)

    elif fun == 'remove':
        s.discard(x)

    elif fun == 'check':
        if x in s:
            print(1)
        else:
            print(0)

    elif fun == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif fun == 'all':
        s = set([i for i in range(1, 21)])

    else:
        s = set()
