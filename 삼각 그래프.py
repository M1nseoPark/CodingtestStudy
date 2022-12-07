import sys
sys.setrecursionlimit(10000000)

def pick(y, x):
    if y == n:
        if x == 1:
            return arr[y][x] + arr[y][x+1]
        elif x == 2:
            return arr[y][x]
        else:
            return 100000000

    if dp[y][x] != -1:
        return dp[y][x]

    if x == 1:
        dp[y][x] = arr[y][x] + min(pick(y+1, x), pick(y+1, x+1), pick(y, x+1))
    elif x == 2:
        dp[y][x] = arr[y][x] + min(pick(y+1, x-1), pick(y+1, x), pick(y+1, x+1), pick(y, x+1))
    else:
        dp[y][x] = arr[y][x] + min(pick(y+1, x-1), pick(y+1, x))

    return dp[y][x]
        

t = 1
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    arr = [[0, 0, 0, 0]]
    for _ in range(n):
        arr.append([0] + list(map(int, sys.stdin.readline().split())))

    dp = [[-1] * 4 for _ in range(n+1)]

    print(str(t) + '. ' + str(pick(1, 2)))
    t += 1

    
            
