# b가 최대 21억이라서 O(b)로는 해결할 수 없음
# 계산 결과를 c로 나눈 나머지를 구함 = 곱하는 중간중간 계속 m으로 나눠서 나머지만 챙김
# 23423616x268921x29123을 10으로 나눈 나머지를 구할 때, 6,1,3만 곱하는 것과 같은 원리
# a^n x a^n = a^2n

a, b, c = map(int, input().split())

def multiply(d):
    if d == 1:
        return a % c

    else:
        if d % 2 == 0:
            temp = multiply(d // 2)  # temp 변수 사용해야 시간초과가 안남
            return temp * temp % c

        else:
            temp = multiply((d - 1) // 2)
            return temp * temp * a % c

print(multiply(b))

    
  
