n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    a, b = max(arr), min(arr)

    while b != 0:
        t = a
        a = b
        b = t % b

    print(arr[0] * arr[1] // a)
