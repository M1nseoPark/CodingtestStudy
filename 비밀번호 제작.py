from collections import deque


n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 0~N 이진수 구하기

# 문자열로 바꿔서 안전도 구하기

# 완전탐색으로 풀면 100,000,000,000 정도라 시간초과
# 완전탐색 말고는 어떻게 풀지 감도 안오는데 BFS로 푼다고???

# n의 최댓값인 1000000을 이진수로 바꾸면 20자리 -> 안전거리 최댓값은 20
safe = [21 for _ in range(n+1)]
q = deque()

for i in range(m):
    safe[arr[i]] = 0   # 시도한 비밀번호는 안전거리가 0임
    q.append(arr[i])   # 시도한 비밀번호 큐에 넣기

answer = 0

while q:
    cur = q.popleft()   # 예제의 경우 cur=3, 4

    for i in range(20):
        x = (1<<i) ^ cur   # 오른쪽 비트시프트(1, 10, 100,...) XOR cur
        if x <= n and safe[cur] + 1 < safe[x]:
            safe[x] = safe[cur] + 1
            answer = max(safe[x], answer)
            q.append(x)


print(answer)

    
    

