t = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    if len(zero) <= n:   # 이미 계산해둔 수보다 클 때만 계산함
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[n], one[n])


for _ in range(t):
    n = int(input())    
    fibonacci(n)

  
