# 회전 초밥 -> 원형 (이걸 고려 안해줌)
n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

left, right = 0, 0
kind = {}
kind[sushi[0]] = 1
temp, answer = 1, 0

while left < n:
    if temp == k:
        if c in kind:
            answer = max(answer, len(kind))
        else:
            answer = max(answer, len(kind) + 1)

        if kind[sushi[left]] == 1:
            del kind[sushi[left]]
        else:
            kind[sushi[left]] -= 1
        left += 1
        temp -= 1

    else:
        right = (right + 1) % n
        if sushi[right] in kind:
            kind[sushi[right]] += 1
        else:
            kind[sushi[right]] = 1
        temp += 1

print(answer)
