n = int(input())

cnt = {}
for _ in range(n):
    p = input()
    if p[0] in cnt:
        cnt[p[0]] += 1
    else:
        cnt[p[0]] = 1

answer = []
for k, v in cnt.items():
    if v >= 5:
        answer.append(k)

answer.sort()
if len(answer) == 0:
    print('PREDAJA')
else:
    print(''.join(map(str, answer)))
    
    
