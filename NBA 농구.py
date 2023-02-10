n = int(input())
goal = []
for _ in range(n):
    a, b = input().split()
    t, m = b.split(':')
    goal.append([int(a), int(t)*60+int(m)])

goal.sort(key=lambda x:x[1])

a, b, sa, sb = 0, 0, 0, 0
for i in range(n):
    if goal[i][0] == 1:
        sa += 1
    else:
        sb += 1
        
    if sa > sb:
        if i+1 == n:
            a += (2880 - goal[i][1])
        else:
            a += (goal[i+1][1] - goal[i][1])
    elif sb > sa:
        if i+1 == n:
            b += (2880 - goal[i][1])
        else:
            b += (goal[i+1][1] - goal[i][1])

aa, ab = '', ''
if (a // 60) < 10:
    aa += '0'
    aa += str(a//60)
else:
    aa += str(a//60)
aa += ':'
if (a % 60) < 10:
    aa += '0'
    aa += str(a%60)
else:
    aa += str(a%60)

if (b // 60) < 10:
    ab += '0'
    ab += str(b//60)
else:
    ab += str(b//60)
ab += ':'
if (b % 60) < 10:
    ab += '0'
    ab += str(b%60)
else:
    ab += str(b%60)

print(aa)
print(ab)
    
    
