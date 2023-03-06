import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n, p, t, m = map(int, sys.stdin.readline().split())
    sol = [{} for i in range(n+1)]
    sub = [[i+1, 0, 0, 0] for i in range(n)]  # 팀ID, 최종 점수, 제출 횟수, 마지막 제출 시간 
    
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if b in sol[a]:
            if sol[a][b] < c:
                sol[a][b] = c
        else:
            sol[a][b] = c

        sub[a-1][2] += 1
        sub[a-1][3] = i

    for i in range(1, n+1):
        for k, v in sol[i].items():
            sub[i-1][1] += v

    sub.sort(key=lambda x:(-x[1], x[2], x[3]))
    for i in range(n):
        if sub[i][0] == t:
            print(i+1)
            break
    
    
            

    
            
