n, m = map(int, input().split())
j = int(input())
answer = 0

s, e = 1, m
for _ in range(j):
    t = int(input())
    if t > e:
        answer += (t - e)
        s, e = t-m+1, t
    elif t < s:
        answer += (s - t)
        s, e = t, t+m-1

print(answer)
