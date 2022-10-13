n = int(input())
call = list(map(int, input().split()))

y = []
m = []

for i in range(n):
    y.append((call[i] // 30 + 1) * 10)
    m.append((call[i] // 60 + 1) * 15)

ysum = sum(y)
msum = sum(m)

if ysum < msum:
    print('Y', ysum)
elif ysum > msum:
    print('M', msum)
else:
    print('Y', 'M', msum)
