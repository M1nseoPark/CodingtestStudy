card = []
for i in range(1, 21):
    card.append(i)

locate = []
for i in range(10):
    a, b = map(int, input().split())
    temp = card[a-1:b]
    card = card[:a-1] + temp[::-1] + card[b:]

print(' '.join(map(str, card)))
