# 순열 라이브러리 써서 pypy로 힘겹게 돌아가는 코드..
from itertools import permutations

n = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

answer = []
count = []

for i in range(4):
    for j in range(operator[i]):
        count.append(i+1)

for p in permutations(count, len(count)):
    temp = A[0]
    for i in range(len(count)):
        if p[i] == 1:
            temp += A[i+1]
        elif p[i] == 2:
            temp -= A[i+1]
        elif p[i] == 3:
            temp *= A[i+1]
        else:
            if temp < 0:
                temp *= -1
                temp //= A[i+1]
                temp *= -1
            else:
                temp //= A[i+1]
    answer.append(temp)

print(max(answer))
print(min(answer))


'''
# 백트래킹으로 푸는 빠른 방법
def calculate(i, ret, operator):
    if i == n:
        result.append(ret)
        return
    if operator[0] != 0:
        operator[0] -= 1
        calculate(i+1, ret + A[i], operator)
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        calculate(i+1, ret - A[i], operator)
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        calculate(i+1, ret * A[i], operator)
        operator[2] += 1
    if operator[3] != 0:
        d = abs(ret) // A[i]
        if ret < 0:
            d *= -1
            
        operator[3] -= 1
        calculate(i+1, d, operator)
        operator[3] += 1
'''
        
        

    
