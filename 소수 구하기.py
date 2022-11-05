import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    prime = True

    if i == 1:
        continue

    j = 2
    while j * j <= i:
        if i % j == 0:
            prime = False
            break

        j += 1

    if prime:
        print(i)

    
