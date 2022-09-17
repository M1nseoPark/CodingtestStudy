n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
result = price[0]
k = 0
i = 1
while True:
    if k == (n - 2):
        answer += (result * distance[k])
        break
    
    if result >= price[i]:
        answer += (result * distance[k])
        result = price[i]
    else:
        answer += (result * distance[k])

    k += 1
    i += 1

print(answer)
