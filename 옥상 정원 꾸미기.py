n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
answer = 0

for i in range(n):
    while stack and stack[-1] <= arr[i]:
        stack.pop()

    stack.append(arr[i])
    answer += len(stack) - 1

print(answer)

    

    
