for _ in range(3):
    n = int(input())
    total = 0   # 선생님한테 받은 전체 금액 
    coin = []
    
    for i in range(n):
        k, c = map(int, input().split())
        total += k * c
        coin.append([k, c])

    # 홀수는 반으로 나눠질 수 없으므로 굳이 확인 안해도 됨
    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    # dp[n] = 주어진 동전들로 n원을 만들 수 있는가?
    dp = [True] + [False] * total

    answer = 0
    for i in range(n):
        k, c = coin[i]   # k는 동전의 종류(500원), c는 해당 동전의 개수(1개)
        
        for j in range(total, k-1, -1):   # 나눈 금액~500원 
            if dp[j-k]:   # j-k가 True라면, j원도 지불할 수 있음(k원 동전이 하나 생긴 것)
                for t in range(c):   # 마찬가지로 j+k*t원도 지불할 수 있음 
                    if j + k * t <= total:
                        dp[j+k*t] = True
                    else:
                        break

        if dp[-1]:
            answer = 1
            break

    print(answer)



    
        

    
