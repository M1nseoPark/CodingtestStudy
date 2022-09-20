# 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 단어

from collections import deque

name = input()
match = {}
for i in range(len(name)):
    if len(match) == 0:
        match[name[i]] = 1
    elif name[i] in match:
        match[name[i]] += 1
    else:
        match[name[i]] = 1

match = deque(sorted(match.items(), reverse=True))
temp = 0
answer = ''
for i in range(len(match)):
    if match[i][1] % 2 == 1:
        temp += 1
        match.appendleft(match.pop(i))

if temp > 1:
    print("I'm Sorry Hansoo")
else:
    if temp == 1:
        answer += match[0][0]
        answer = match[0][0] * match[0][1] - 1 // 2
        
    for i in range(len(match)):
        
        
