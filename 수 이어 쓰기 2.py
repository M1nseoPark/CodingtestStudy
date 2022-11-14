n, k = map(int, input().split())

idx = 9
num = 1
answer = 0

while k > idx * num:
    k -= idx * num
    answer += idx
    num += 1
    idx *= 10

answer = (answer + 1) + (k - 1) // num

if answer > n:
    print(-1)
else:
    print(str(answer)[(k-1)%num])
