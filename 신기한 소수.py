n = int(input())
m = 10 ** n

def isPrime(a):
    if a < 2:
        return False

    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
        

def dfs(num):
    if len(str(num)) == n:
        print(num)

    else:
        for i in range(10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(temp)

# 1의 자리 소수는 2,3,5,7 밖에 없음
dfs(2)
dfs(3)
dfs(5)
dfs(7)

