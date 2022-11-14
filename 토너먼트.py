n, j, h = map(int, input().split())

r = 1

while (j - 1) // (2**r) != (h - 1) // (2**r):
    if 2**r > n:
        r = -1
        break
    
    r += 1

print(r)
