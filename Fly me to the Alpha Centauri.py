# 규칙은 찾았는데 구현을 못함

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    cnt, rst = 0, 0
    move = 1

    while rst < y - x:
        cnt += 1
        rst += move
        if cnt % 2 == 0:
            move += 1

    print(cnt)
        
    
