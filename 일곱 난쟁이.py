# 브론즈 치고는 어려운 문제
# 나는 라이브러리 써서 풀었는데 sum(A) - (난쟁이1 + 난쟁이2) = 100으로 푸는게 좋은듯
from itertools import combinations

A = []
for _ in range(9):
    A.append(int(input()))

for i in combinations(A, 7):
    if sum(i) == 100:
        i = list(i)
        for j in range(7):
            i.sort()
            print(i[j])
        break
