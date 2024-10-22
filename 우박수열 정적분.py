def solution(k, ranges):
    answer = []
    arr = [k]
    result = []
    
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        arr.append(k)
    
    for i in range(1, len(arr)):
        temp = min(arr[i-1], arr[i])
        temp += (max(arr[i-1], arr[i]) - min(arr[i-1], arr[i])) * 0.5
        result.append(temp)

    for a, b in ranges:
        temp = 0
        
        if a > len(arr)+b-1:
            answer.append(-1)
        
        elif a == len(arr)+b-1:
            answer.append(0)
        
        else:
            for i in range(a, len(arr)+b-1):
                temp += result[i]
            answer.append(temp)
            
    return answer