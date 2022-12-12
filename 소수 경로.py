from collections import deque

t = int(input())

# 네 자리 소수 구하기 
prime = [True for _ in range(10000)]
prime[1] = False

for i in range(2, int(9999**0.5)+1):
    if prime[i]:
        for j in range(i+i, 10000, i):
            prime[j] = False


def bfs():
    q = deque()
    q.append([a, 0])
    visited = [0 for i in range(10000)]
    visited[a] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)

        # 먼저 리턴되는 게 최소 횟수 방법
        if now == b:
            return cnt

        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[temp] == 0 and prime[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt+1])

    return -1
                

for _ in range(t):
    a, b = map(int, input().split())
    
    result = bfs()
    if result != -1:
        print(result)
    else:
        print("Impossible")
    

    
