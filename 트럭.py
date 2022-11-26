n, w, l = map(int, input().split())
arr = list(map(int, input().split()))

idx = 0
bridge = []
cross, answer = 0, 1

while len(bridge) != 0 or idx != n:
    if idx != n and cross + arr[idx] <= l:
        bridge.append([arr[idx], 0])
        cross += arr[idx]
        idx += 1

    for i in range(len(bridge)):
        bridge[i][1] += 1

    if bridge[0][1] == w:
        cross -= bridge[0][0]
        bridge.pop(0)

    answer += 1


print(answer)


    
        

    
    
    
