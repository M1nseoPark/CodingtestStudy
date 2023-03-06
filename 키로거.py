from collections import deque

t = int(input())
for _ in range(t):
    s = input()

    ls, rs = deque(), deque()
    for i in range(len(s)):
        if s[i] == '<':
            if len(ls) != 0:
                rs.appendleft(ls.pop())

        elif s[i] == '>':
            if len(rs) != 0:
                ls.append(rs.popleft())

        elif s[i] == '-':
            if len(ls) != 0:
                ls.pop()

        else:
            ls.append(s[i])

    print(''.join(map(str, ls)) + ''.join(map(str, rs)))
