n, m = map(int, input().split())
card = list(map(int, input().split()))

card.sort(reverse=True)

def pick(result):
    if len(result) == 3:
        if sum(result) <= m:
            answer.append(sum(result))
    else:
        for i in range(n):
            if len(result) == 0:
                result.append(card[i])
                pick(result)
                result.pop()
            elif card[i] not in result:
                result.append(card[i])
                pick(result)
                result.pop()

result = []
answer = []
pick(result)
print(max(answer))
        

