# 10은 2와 5로 구성되어 있음!!
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수 중 더 작은 게 10의 개수임
# nCr = n! / (n-r)!r!
# n!의 2의 지수 - (n-r)!의 2의 지수 - r!의 2의 지수 (나누기라 뺄셈으로 계산)

n, m = map(int, input().split())

def count(n, k):
    num = 0
    while n:
        n //= k
        num += n
    return num

five = count(n, 5) - count(m, 5) - count(n-m, 5)
two = count(n, 2) - count(m, 2) - count(n-m, 2)

answer = min(five, two)
print(answer)

