t = int(input())

A = t // 300
B = (t % 300) // 60
C = ((t % 300) % 60) // 10
answer = True

while True:
    if ((A * 300) + (B * 60) + (C * 10)) == t:
        break

    if A > 0:
        A -= 1
        B = (t - (A * 300)) // 60
        C = (t - (A * 300) - (B * 60)) // 10
    elif B > 0:
        B -= 1
        C = (t - (A * 300) - (B * 60)) // 10
    else:
        answer = False
        break

if answer:
    print(A, B, C)
else:
    print(-1)
    
    
