# 난 순열로 풀었는데 피보나치 수열로도 푸는듯

n = int(input())

result = [1 for _ in range(n+1)]
for i in range(1, n+1):
    result[i] = result[i-1] * i   # 순열 연산 수행 결과 리스트에 저장

v = n
h = 0
answer = 0
while v >= 0:
    answer += (result[v+h] // (result[v] * result[h]))
    v -= 2
    h += 1

print(answer % 10007)
    

