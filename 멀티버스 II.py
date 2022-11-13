# 두 개를 고르는 조합 연산은 굳이 조합 라이브러리를 안써도 됨
# 정렬 연산이라는 걸 몰랐음
import sys

m, n = map(int, sys.stdin.readline().split())
arr = []
answer = 0

# 2차원 리스트 만들 필요 없이 나중에 순위 리스트로 대체하기
for i in range(m):
    arr.append(list(map(int, sys.stdin.readline().split()))) 


# 순위 리스트 만들기 [12, 50, 10] -> [2, 3, 1]
for i in range(m):
    temp = sorted(arr[i])
    idx = []
    for k in arr[i]:
        idx.append(temp.index(k) + 1)  

    arr[i] = idx


# 2중 for문 -> 우주의 쌍 구하기
for i in range(m-1):
    for j in range(i+1, m):
        if arr[i] == arr[j]:
            answer += 1

print(answer)

    
