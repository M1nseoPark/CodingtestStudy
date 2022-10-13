for _ in range(3):
    A = list(map(int, input().split()))
    rst = sum(A)

    if rst == 3:
        print('A')
    elif rst == 2:
        print('B')
    elif rst == 1:
        print('C')
    elif rst == 0:
        print('D')
    else:
        print('E')
