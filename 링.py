n = int(input())
ring = list(map(int, input().split()))

for i in range(1, n):
    a, b = ring[0], ring[i]

    while b != 0:
        temp = a
        a = b
        b = temp % a

    print(str(ring[0]//a) + '/' + str(ring[i]//a))
