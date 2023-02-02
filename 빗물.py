h, w = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, w-1):
    lm = max(A[:i])
    rm = max(A[i+1:])

    # 물이 고이기 위해선 자신보다 더 높은 블록으로 왼쪽과 오른쪽이 둘러싸여 있어야 함
    # 한 칸씩 물이 얼만큼 쌓일 수 있는지 검사하기 
    compare = min(lm, rm)

    if A[i] < compare:
        cnt += compare - A[i]
    
print(cnt)

    
    
