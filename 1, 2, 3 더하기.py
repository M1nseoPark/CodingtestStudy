t = int(input())
plus = [1, 2, 4]

for _ in range(t):
    n = int(input())

    for i in range(len(plus), n):
        plus.append(plus[i-1] + plus[i-2] + plus[i-3])

    print(plus[n-1])
    
