n = int(input())
dice = list(map(int, input().split()))

# n=1이면 제일 큰 수 제외 나머지 합
# n=2이면 3면 보이는 거 4개(1,2,3), 2면 보이는 거 4개(1,2)
# n=3이면 2면 보이는 거 12개, 1면 보이는 거 9개, 3면 보이는 거 4개, 0면 보이는 거 2개
# 3면 4개, 2면 4*(n-1)+4*(n-2), 1면 4*(n-1)(n-2)+(n-2)*(n-2)

# 마주보는 면은 제외해야 함!!! -> 이거때매 틀림
temp = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
temp.sort()
answer = 0

if n == 1:
    print(sum(dice) - max(dice))
else:
    answer += sum(temp) * 4
    answer += (temp[0] + temp[1]) * (4 * (n - 1) + 4 * (n - 2))
    answer += temp[0] * ((n - 2) * 4 * (n - 1) + (n - 2) * (n - 2))
    print(answer)
    
    

