test = int(input())

def count(num, d):
    rst = 0
    while num:
        num //= d
        rst += num

    return rst


for _ in range(test):
    n = int(input())

    t, f = count(n, 2), count(n, 5)

    print(min(t, f))
        
    
