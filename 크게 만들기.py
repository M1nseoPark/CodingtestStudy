n, k = map(int, input().split())
num = list(map(int, input()))

stack = []
idx = 0
for i in range(n):
    while stack and stack[-1] < num[i] and idx < k:
        stack.pop()
        idx += 1

    stack.append(num[i])

while idx < k:
    stack.pop()
    idx += 1

print(int(''.join(map(str, stack))))
