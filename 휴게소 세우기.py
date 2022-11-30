n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]

arr.sort()
left, right = 1, l-1
answer = 0

while left <= right:
    cnt = 0
    mid = (right + left) // 2

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid:   # 현재 거리 중 mid보다 큰 거리를 찾아서 
            cnt += (arr[i] - arr[i-1] - 1) // mid  # 나눈 만큼 휴게소 설치(현재 설치돼있는 구역 -1)

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)



            
        
        
