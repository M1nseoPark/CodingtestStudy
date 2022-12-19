n, q = map(int, input().split())
A = list(map(int, input().split()))
hyeon = 0

for i in range(q):
    c = list(map(int, input().split()))

    if c[0] == 1:
        if A[c[1]-1] == 1:
            A[c[1]-1] = 0
        else:
            A[c[1]-1] = 1

    elif c[0] == 2:
        hyeon = (hyeon + c[1]) % n

    else:
        if sum(A) == 0:
            print(-1)
        else:
            move = 0
            left, right = hyeon-1, hyeon+1
            while 0 <= left and right < n:
                if arr[left] == 1:
                    move = left
                    break

                elif arr[right] == 1:
                    move = right
                    break

                left -= 1
                right += 1
            
            print(abs(hyeon-move))
                    

