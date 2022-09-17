n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
k = n
temp = 0
for i in range(n):
    if temp < rope[i] * k:
        temp = rope[i] * k

    k -= 1


print(temp)

