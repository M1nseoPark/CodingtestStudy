# 범위 500,000 -> 이중 반복문 250,000,000,000

n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0] * n

# 가장 높은 탑 말고 자신의 왼쪽에 있는 탑의 영향을 받음
# 최대최소 X, 스택 O
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append([i, top[i]])  # [인덱스, 값]으로 스택 활용하는 것도 고려하기


for i in range(n):
    print(answer[i], end=' ')
            
