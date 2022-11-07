import sys

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    answer = 0
    while x <= m * n:
        if (x - y) % n == 0:
            answer = x
            break
        else:
            x += m

    if answer == 0:
        print(-1)
    else:
        print(answer)


        
        
    
