# 16953번 A->B
A, B = map(int, input().split())

answer = 0
while True:
    if B == A:
        break
    elif B < A:
        answer = -1
        break
    
    if B % 2 == 0:
        B = B // 2
        answer += 1
    elif B % 10 == 1:
        B = B // 10
        answer += 1
    else:
        answer = -1
        break

if answer == -1:
    print(-1)
else:
    print(answer + 1)


'''
<< BFS로 풀 경우 <- 필요한 연산의 최솟값 >>
q = deque()
q.append((A, 1))   # (A, 연산횟수)

while q:
    n, t = q.popleft()
    if n > B:
        continue
    if n == B:
        print(t)
        break

    q.append((int(str(n) + 1)), t+1)  ## 1을 수의 가장 오른쪽에 추가한다
    q.append((n*2, t+1))  ## 2를 곱한다
else:
    print(-1)
'''
