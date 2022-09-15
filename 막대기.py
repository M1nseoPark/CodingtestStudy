import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    stick = int(sys.stdin.readline())

    while stack:
        if stack[-1] <= stick:
            stack.pop()
        else:
            break
        
    stack.append(stick)

print(len(stack))
