import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for start in range(n-i):
        end = start + i

        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면 
        elif arr[start] == arr[end]:
            # 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end:
                dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

        
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])

    

    

        
        

        
        
    
