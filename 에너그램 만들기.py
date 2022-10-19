# 1. 아스키코드를 이용하여 알파벳 개수를 세기
# 2. collections 라이브러리의 Counter 함수 쓰기

a = list(input())
b = list(input())

rst = 0
visited = [False for _ in range(len(b))]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and not visited[j]:
            rst += 1
            visited[j] = True
            break

print(len(a) + len(b) - (rst * 2))
