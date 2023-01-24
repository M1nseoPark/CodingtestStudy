def count(game):
    result = []
    for i in range(3):
        if game[3*i] == game[3*i+1] == game[3*i+2] and game[3*i] != '.':
            result.append(game[3*i])

        if game[i] == game[3+i] == game[6+i] and game[i] != '.':
            result.append(game[i])

    if game[0] == game[4] == game[8] and game[0] != '.':
        result.append(game[0])

    if game[2] == game[4] == game[6] and game[2] != '.':
        result.append(game[2])

    return result
    

while True:
    game = input()
    if game == 'end':
        break

    turn, ot, xt = 0, 0, 0
    flag = True
    
    for i in range(9):
        if game[i] == '.':
            turn += 1

        if game[i] == 'O':
            ot += 1

        if game[i] == 'X':
            xt += 1

    turn = 9 - turn
    if turn % 2 == 1 and xt - ot != 1:
        print('invalid')
        flag = False
    elif turn % 2 == 0 and xt - ot != 0:
        print('invalid')
        flag = False

    if flag:
        if turn == 9:
            if 'O' in count(game):
                print('invalid')
            else:
                print('valid')
                
        elif turn % 2 == 1:
            result = count(game)
            if 'O' in result or len(result) == 0:
                print('invalid')
            else:
                print('valid')
                
        else:
            result = count(game)
            if 'X' in result or len(result) == 0:
                print('invalid')
            else:
                print('valid')
        
