test = int(input())
for _ in range(test):
    a, b = input().split()
    A = list(a)
    B = list(b)

    A.sort()
    B.sort()

    if A == B:
        print('Possible')
    else:
        print('Impossible')
