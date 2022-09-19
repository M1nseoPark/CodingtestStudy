board = input()

temp = 0
result = ''
answer = True
for i in range(len(board)):
    if temp == 4:
        result += 'AAAA'
        temp = 0
        
    if board[i] == 'X':
        temp += 1
    elif board[i] == '.':
        if temp % 2 == 1:
            answer = False
            break
        elif temp == 2:
            result += 'BB'

        result += '.'
        temp = 0

  
if temp % 2 == 1:
    answer = False
elif temp == 4:
    result += 'AAAA'
elif temp == 2:
    result += 'BB'

if answer:
    print(result)
else:
    print(-1)
            
            
        
