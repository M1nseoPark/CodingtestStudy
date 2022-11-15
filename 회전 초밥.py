n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

eat = [sushi[0]]
left, right = 0, 0
answer = 0

while left < n and right < n:
    if k == len(eat):
        if c in eat:
            answer = k
            left += 1
            eat.pop(0)
        else:
            answer = k + 1
            break
        
    else:
        answer = max(answer, len(eat))

        right += 1
        if right < n:
            if sushi[right] not in eat:
                eat.append(sushi[right])
            else:
                left += 1
                right -= 1
                eat.pop(0)

print(answer)
