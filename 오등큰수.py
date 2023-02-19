n = int(input())
A = list(map(int, input().split()))

dic = {}
for i in range(n):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1

stack = []
answer = [-1] * n

for i in range(n-1, -1, -1):
    while stack and dic[stack[-1]] <= dic[A[i]]:
        stack.pop()

    if stack:
        answer[i] = stack[-1]
        
    stack.append(A[i])

print(' '.join(map(str, answer)))
    
