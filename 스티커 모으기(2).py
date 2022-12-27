def solution(sticker):
    answer = 0

    if len(sticker) % 2 == 0:
        n = len(sticker) // 2
        temp = [0, 0]
        for i in range(n):
            temp[0] += sticker[2*i+1]
            temp[1] += sticker[2*i]
        answer = max(temp)
    
    else:
        temp = []
        n = len(sticker)
        for i in range(n):
            d, rst = 0, 0
            for j in range(n//2):
                rst += sticker[(i+d)%n]
                d += 2
            temp.append(rst)
        answer = max(temp)
                
    return answer

print(solution([5, 1, 16, 17, 16]))
