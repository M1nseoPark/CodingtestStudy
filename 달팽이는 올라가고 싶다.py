a, b, v = map(int, input().split())

if v % (a - b) == 0:
    if (a - b) == b:
        print(v // (a - b) - 1)
    else:
        print(v // (a - b))
else:
    print((v - a) // (a - b))
