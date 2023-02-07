import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline()))

left, right = 0, 0
kind = {}
kind[sushi[left]] = 1
cnt, answer = 1, 0

while left < n:
    if cnt == k:
        if c in kind:
            answer = max(answer, len(kind))
        else:
            answer = max(answer, len(kind) + 1)
            
        if kind[sushi[left]] == 1:
            del kind[sushi[left]]
        else:
            kind[sushi[left]] -= 1
            
        left += 1
        cnt -= 1

    else:
        right = (right + 1) % n
        cnt += 1
        if sushi[right] in kind:
            kind[sushi[right]] += 1
        else:
            kind[sushi[right]] = 1

print(answer)
        
        
