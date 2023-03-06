h, w, n, m = map(int, input().split())

hn = (h + n) // (1 + n)
wm = (w + m) // (1 + m)

print(hn * wm)
