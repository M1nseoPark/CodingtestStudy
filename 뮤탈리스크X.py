from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))

q = deque()
for c in permutations(scv, n):
    q.append([list(c), 0])

while q:
    here = q.popleft()
    print(here)

    if len(here[0]) == 0:
        print(here[1])
        break

    elif len(here[0]) == 3:
        temp = []
        if here[0][0] - 9 > 0:
            temp.append(here[0][0]-9)
        if here[0][1] - 3 > 0:    
            temp.append(here[0][1]-3)
        if here[0][2] - 1 > 0:
            temp.append(here[0][2]-1)
            
        q.append([temp, here[1]+1])

    elif len(here[0]) == 2:
        temp = []
        if here[0][0] - 9 > 0:
            temp.append(here[0][0]-9)
        if here[0][1] - 3 > 0:
            temp.append(here[0][1]-3)
            
        q.append([temp, here[1]+1])

    elif len(here[0]) == 1:
        temp = []
        if here[0][0] - 9 > 0:
            temp.append(here[0][0]-9)
            
        q.append([temp, here[1]+1])

