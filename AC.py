# 두 번 뒤집는 건 안 뒤집는 것과 같다 = 이거때매 시간초과 계속 남
from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    if n != 0:
        arr = deque(list(map(int, sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split(','))))
    else:
        temp = sys.stdin.readline()
        arr = deque()
    error = False

    reverse = 0
    for i in range(len(p)):
        if p[i] == 'R':
            reverse += 1

        elif p[i] == 'D':
            if len(arr) == 0:
                print('error')
                error = True
                break
            else:
                if reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if reverse % 2 == 1:
        arr.reverse()

    answer = ''
    if not error:
        answer += '['
        for i in range(len(arr)):
            answer += str(arr[i])
            answer += ','
        if len(arr) >= 1:
            answer = answer[:-1]
        answer += ']'

        print(answer)
            

        
                
