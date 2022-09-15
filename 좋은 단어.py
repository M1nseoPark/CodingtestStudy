n = int(input())
answer = 0

for _ in range(n):
    word = input()
    stack = []
    
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
            
        elif stack[-1] == word[i]:
            stack.pop()

        else:
            stack.append(word[i])

    if len(stack) == 0:
        answer += 1

print(answer)
            
