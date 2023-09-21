## 내가 짠 코드 
def solution(n, build_frame):
    answer = [[]]
    board = [[[0, 0] for _ in range(n)] for _ in range(n)]   # [위쪽(기둥), 오른쪽(보)]
    
    def build(type, y, x):
        if 0 > y or 0 > x or y >= n or x >= n:
            return False
        
        if type == 0:   # 기둥 
            if y == 0 or (x > 0 and board[y][x-1][1] == 1) or (y > 0 and board[y-1][x][0] == 1):
                return True
        else:   # 보 
            if (y > 0 and board[y-1][x][0] == 1) and (0 < x < n-2 and board[y][x-1][1] == 1 and board[y][x+1][1] == 1):
                return True
        return False
    
    
    for x, y, a, b in build_frame:
        if b == 1:   # 설치 
            if build(a, y, x):
                board[y][x][a] = 1
                
        else:   # 삭제 
            flag = True
            if a == 0:   # 기둥 
                if y + 1 < n and board[y+1][x][1] == 1 and not build(y+1, x, 1):
                    flag = False
                
                if 0 <= x - 1 and board[y][x-1][1] == 1 and not build(y, x-1, 1):
                    flag = False
                
                if 0 <= y - 1 and board[y-1][x][0] == 1 and not build(y-1, x, 0):
                    flag = False
                
                if y + 1 < n and board[y+1][x][0] == 1 and not build(y+1, x, 0):
                    flag = False
            
            else:  # 보 
                if y + 1 < n and board[y+1][x][1] == 1 and not build(y+1, x, 1):
                    flag = False
                
                if 0 <= y - 1 and board[y-1][x][1] == 1 and not build(y-1, x, 1):
                    flag = False
                
                if 0 <= y - 1 and board[y-1][x][0] == 1 and not build(y-1, x, 0):
                    flag = False
                
                if x + 1 < n and board[y][x+1][0] == 1 and not build(y, x+1, 0):
                    flag = False
            
            if not flag:
                board[y][x][a] = 0
        
    return answer


## 답안 
def solution(n, build_frame):
    result = set()

    def impossible():
        for x, y, a in result:
            if a == 0:  # 기둥일 때 
                if y != 0 and (x, y-1, 0) not in result and (x-1, y, 1) not in result and (x, y, 1) not in result:
                    return True

            else:  # 보일 때 
                if (x, y-1, 0) not in result and (x+1, y-1, 0) not in result and not ((x-1, y, 1) in result and (x+1, y, 1) in result):
                    return True
            return False


    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:  # 설치 
            result.add(item)
            if impossible():  # 설치 
                result.remove(item)
        
        elif item in result:  # 삭제 
            result.remove(item)
            if impossible():
                result.add(item)
    
    return sorted(list(result))
