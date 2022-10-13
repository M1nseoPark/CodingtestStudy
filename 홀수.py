answer = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        answer.append(num)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))
