n, k = map(int, input().split())

divide = 1
answer = []
while True:
    if len(answer) == k or divide > n:
        break
        
    if n % divide == 0:
        answer.append(divide)

    divide += 1

if len(answer) < k:
    print(0)
else:
    print(answer[k-1])
        
