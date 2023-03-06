a, b, c = map(int, input().split())
park = [0] * 101

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        park[i] += 1

time = [0] * 4
for i in range(101):
    time[park[i]] += 1

print(time[1]*a + time[2]*b*2 + time[3]*c*3)
    
