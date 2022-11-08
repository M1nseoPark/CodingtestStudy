t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        answer = h * 100 + (n // h)
    else:
        answer = (n % h) * 100 + (n // h) + 1
        
    print(answer)
