from collections import deque
import sys


n, m, p = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()))

castle = [deque() for _ in range(p+1)]   # 플레이어별 성의 위치
answer = [0] * (p + 1)   # 플레이어별 성의 개수 

for i in range(n):
    for j in range(m):
        if board[i][j] != '.' and board[i][j] != '#':
            answer[int(board[i][j])] += 1
            castle[int(board[i][j])].append([i, j])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def expand():
    finish = False
    while finish:
        finish = True
        



            
                
            




    

        
            


            

    
            
            


                

            
    
    




    
    
