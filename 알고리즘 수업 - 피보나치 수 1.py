import sys

n = int(sys.stdin.readline())
code1, code2 = 0, 0

def fib(n):
    global code1
    
    if n == 1 or n == 2:
        return 1

    else:
        code1 += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global code2

    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        code2 += 1
        f[i] = f[i-1] + f[i-2]

    return f[n]


fib(n)
fibonacci(n)
print(code1 + 1, code2)
