def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def compress(y, x, r):
        temp = arr[y][x]
        flag = True
        
        for i in range(y, y+r):
            for j in range(x, x+r):
                if temp != arr[i][j]:
                    flag = False
                    break
            if not flag:
                break
        
        if flag:
            answer[temp] += 1
        else:
            compress(y, x, r//2)
            compress(y+r//2, x, r//2)
            compress(y, x+r//2, r//2)
            compress(y+r//2, x+r//2, r//2)
    
    compress(0, 0, n)
    return answer