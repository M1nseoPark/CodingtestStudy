import math

n, a, b, c, d = map(int, input().split())
answer = 1000000000000000

# a와 c의 최소공배수 구하기 
at, ct = a, c
while ct != 0:
    tt = at
    at = ct
    ct = tt % at

lcm = (a * c) // at


# 첫번째 가게가 가성비가 안좋은 경우, 첫번째 가게에서 lcm개 이상 사면 안됨
if b/a > d/c:
    m = math.ceil(lcm / a)
    
    for i in range(m):
        j = math.ceil((n - i*a) / c)
        answer = min(answer, i*b+j*d)

else:
    m = math.ceil(lcm / b)

    for i in range(m):
        j = math.ceil((n - j*c) / a)
        answer = min(answer, i*b+j*d)
        
print(answer)
        
        
        
        
    
    

    
    
