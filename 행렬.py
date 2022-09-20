# 3x3 행렬을 골라 연산하는게 어려웠음
# 무작정 왼쪽 위부터 연산하는 것 같은데 이게 왜 최소횟수 코드인지 이해는 안됨

n, m = map(int, input().split())
A = []
B = []

for _ in range(n):
    A.append(list(map(int, input())))
for _ in range(n):
    B.append(list(map(int, input())))


def reverse(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0


answer = 0
if (n < 3 or m < 3) and A != B:
    answer = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if A[r][c] != B[r][c]:
                answer += 1   ##
                reverse(r, c)

if A != B:
    answer = -1

print(answer)



            
        
