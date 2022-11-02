import sys

n = int(sys.stdin.readline())
card = {}
for _ in range(n):
    t = int(sys.stdin.readline())
    if t in card:
        card[t] += 1
    else:
        card[t] = 1
        
card = sorted(card.items(), key=lambda x:(x[1], -x[0]), reverse=True)

print(card[0][0])
    
    


