from collections import deque

n = int(input())
arr = list(map(int, input().split()))
area = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]+1):
        area[i].append(temp[j]-1)


def check(que):
    ans, cnt = arr[que[0]], 1
    checked = [False] * n
    q = deque()
    q.append(que[0])
    checked[que[0]] = True
    
    while q:
        here = q.popleft()

        for i in area[here]:
            if i in que and not checked[i]:
                q.append(i)
                cnt += 1
                ans += arr[i]
                checked[i] = True

    if cnt == len(que):
        return ans
    else:
        return False
            

def dfs(num, x, m):
    global answer
    
    if num == m:
        q1 = deque()
        q2 = deque()
        ans1, ans2 = 0, 0

        for i in range(n):
            if visited[i]:
                q1.append(i)
            else:
                q2.append(i)

        ans1, ans2 = check(q1), check(q2)
        if not ans1:
            return
        if not ans2:
            return

        answer = min(answer, abs(ans1-ans2))

    else:
        for i in range(x, n):   # 모든 경우 고려
            if not visited[i]:
                visited[i] = True
                dfs(num, i+1, m+1)
                visited[i] = False

    
answer = 1001
for i in range(1, n//2+1):
    visited = [False] * n
    dfs(i, 0, 0)

if answer == 1001:
    print(-1)
else:
    print(answer)
