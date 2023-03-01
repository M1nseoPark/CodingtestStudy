arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def postorder(start, end):   # start가 루트
    if start > end:
        return

    mid = end + 1
    for i in range(start+1, end+1):
        # 루트보다 큰 값이 존재하면 이 값을 기준으로 왼쪽 트리, 오른쪽 트리 나눠줌 
        if arr[start] < arr[i]:   
            mid = i
            break

    postorder(start+1, mid-1)   # 왼쪽 트리 
    postorder(mid, end)   # 오른쪽 트리 
    print(arr[start])   # 루트 

postorder(0, len(arr)-1)

    
