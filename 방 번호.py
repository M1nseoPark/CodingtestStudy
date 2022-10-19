import math

n = list(map(int, input()))

count = [0] * 10

for i in range(len(n)):
    if n[i] == 9:
        count[6] += 1
    else:
        count[n[i]] += 1

if count[6] > 1:
    count[6] = math.ceil(count[6] / 2)

ans = 1
for i in range(10):
    if ans < count[i]:
        ans = count[i]

print(ans)

'''
if n[i] == 6 or n[i] == 9:
    if count[6] <= count[9]:
        count[6] += 1
    else:
        count[9] += 1
'''
        
    

