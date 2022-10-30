t = int(input())

one = [0] * 41
zero = [0] * 41
zero[0] = 1
one[1] = 1


def fibonacci(n):
    for i in range(2, n+1):
        if one[i] == 0 or zero[i] == 0:
            one[i] = one[i-1] + one[i-2]
            zero[i] = zero[i-1] + zero[i-2]


for _ in range(t):
    n = int(input())
    fibonacci(n)
    print(zero[n], one[n])
