n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

down = sorted(A, reverse=True)
up = sorted(A)
big, small = down[0], up[0]
i = 1

while True:
    if B[0] == 0 and B[1] == 0 and B[2] == 0 and B[3] == 0:
        print(big)
        print(small)
        break

    if B[2] != 0:
        big = big * down[i]
        small = small * up[i]
        i += 1
        B[2] -= 1

    elif B[0] != 0:
        big = big + down[i]
        small = small + up[i]
        i += 1
        B[0] -= 1

    elif B[1] != 0:
        big = big - down[i]
        small = small - up[i]
        i += 1
        B[1] -= 1

    elif B[3] != 0:
        big = big // down[i]
        small = small // up[i]
        i += 1
        B[3] -= 1
        
        

    
