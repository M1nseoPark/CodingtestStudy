import sys

n = int(sys.stdin.readline())
card = {}
for _ in range(n):
    t = int(sys.stdin.readline())
    if t in card:
        card[t] += 1
    else:
        card[t] = 1
        
card = sorted(card.items(), key=lambda x:(x[1], x[0]), reverse=True)
ak, av = card[0][0], card[0][1]

if n >= 2:
    for i in range(1, n):
        if av == card[i][1]:
            ak = card[i][0]
            av = card[i][1]
        else:
            break

print(ak)
    
    


