n = int(input())
top = list(map(int, input().split()))

stack = []
answer = []

for i in range(n-1, -1, -1):
    while stack:
        if stack[0] < top[i]:
            answer.append(i)
            stack.pop(0)

    stack.append(top[i])
print(stack)
print(answer)
        
