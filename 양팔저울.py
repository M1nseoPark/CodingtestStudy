n = int(input())
weight = list(map(int, input().split()))  # 추의 무게 
m = int(input())
beads = list(map(int, input().split()))  # 구슬 무게

# dp[i][j] = i번째까지의 추를 놓았을 때, j 무게를 만들 수 있는지
dp = [[0]*(30*500+1) for _ in range(n+1)]
result = set()

def dfs(idx, left, right):
    new = abs(left - right)

    if new not in result:
        result.add(new)

    # 모든 추를 다 올려놓았을 때 
    if idx == n:
        return

    if dp[idx][new] == 0:
        dfs(idx+1, left+weight[idx], right)   # 왼쪽에 놓기 
        dfs(idx+1, left, right+weight[idx])   # 오른쪽에 놓기 
        dfs(idx+1, left, right)   # 놓지 않기 
        dp[idx][new] = 1

dfs(0, 0, 0)
answer = []

for i in beads:
    if i in result:
        answer.append('Y')
    else:
        answer.append('N')

print(' '.join(map(str, answer)))
    
