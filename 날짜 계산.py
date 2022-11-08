e, s, m = map(int, input().split())

d = 1
while True:
    if d % 15 == e and d % 28 == s and m % 19 == m:
        print(d)
        break
    else:
        d += 1
