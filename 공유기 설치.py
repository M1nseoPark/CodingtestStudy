import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
left, right = 1, arr[n-1] - arr[0]  # 집 사이의 최소 거리, 최대 거리
answer = 0

if c == 2:
    print(arr[n-1] - arr[0])
else:
    while left < right:
        mid = (left + right) // 2

        cnt = 1  # 공유기 설치한 집 개수 
        ts = arr[0]  # 시작점은 무조건 설치 

        for i in range(n):
            if arr[i] - ts >= mid:  # 예제의 경우 mid=4라 8에 있는 집에서 공유기 설치 가능
                cnt += 1
                ts = arr[i]

        if cnt >= c:  
            answer = mid
            left = mid + 1
        else:   # cnt가 2라 조건 충족 못함 -> 공유기 간격 좁혀야 함 
            right = mid

    print(answer)
