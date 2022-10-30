n = int(input())

def put(a, b, n):
    if n == 1:
        print(a, b)
        return
    
    put(a, 6-a-b, n-1)
    print(a, b)
    put(6-a-b, b, n-1)


print(2**n - 1)
if n <= 20:   # n이 20보다 큰 경우에는 과정은 출력할 필요 없음
    put(1, 3, n)
