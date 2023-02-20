import sys

n = int(input())
s = input()
answer = -1 * sys.maxsize

def dfs(idx, value):
    global answer

    if idx == n-1:
        answer = max(answer, value)
        return

    if idx + 2 < n:
        dfs(idx+2, eval(str(value)+s[idx+1]+s[idx+2]))

    if idx + 4 < n:
        dfs(idx+4, eval(str(value)+s[idx+1]+str(eval(s[idx+2:idx+5]))))


dfs(0, int(s[0]))
print(answer)
