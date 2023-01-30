# 어렵당 

n, m, l, k = map(int, input().split())
star = [[] for _ in range(k)]
for i in range(k):
    star[i] = list(map(int, input().split()))


def pick(x, y):
    global answer
    cnt = 0
    
    for i in range(k):
        if x <= star[i][0] and x+l >= star[i][0] and y <= star[i][1] and y+l >= star[i][1]:
            cnt += 1

        answer = max(answer, cnt)
        
    
answer = 0
for i in range(k):
    for j in range(k):
        pick(star[i][0], star[j][1])

print(k - answer)
