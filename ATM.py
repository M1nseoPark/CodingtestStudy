n = int(input())
p = list(map(int, input().split()))

p.sort()
answer = 0
temp = 0
for i in range(len(p)):
    temp += p[i]
    answer += temp

print(answer)
