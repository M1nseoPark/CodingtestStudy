import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

switch = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

    if s == t:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)

