s = input()

d = []
stack = []
for i in range(len(s)):
    if s[i] == ' ' or s[i] == '<' or s[i] == '>':
        if len(stack) != 0:
            d.append(''.join(map(str, stack)))
            stack.clear()
        d.append(s[i])

    else:
        stack.append(s[i])

if len(stack) != 0:
    d.append(''.join(map(str, stack)))

answer = ''
tag = False
for i in range(len(d)):
    if d[i] == '<':
        answer += d[i]
        tag = True

    elif d[i] == ' ':
        answer += d[i]

    elif d[i] == '>':
        answer += d[i]
        tag = False

    else:
        if tag:
            answer += d[i]
        else:
            answer += d[i][::-1]

print(answer)
        
