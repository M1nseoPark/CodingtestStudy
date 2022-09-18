# 완전히 이해는 안됨

n, l = map(int, input().split())
water = list(map(int, input().split()))

water.sort()

start = water[0]
answer = 1
for i in water[1:]:
    if start <= i and i < start + l:
        continue
    else:
        start = i
        answer += 1

print(answer)
            
            
    


        
        
