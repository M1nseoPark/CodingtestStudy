from itertools import permutations

n, k = map(int, input().split())
outcome = []
for _ in range(n):
    outcome.append(list(map(int, input().split())))

friend = []
for _ in range(2):
    friend.append(list(map(int, input().split())))

def find(y, x):
    if y != 1 and x != 1:
        return 1
    elif y != 2 and x != 2:
        return 2
    else:
        return 0
    

answer = 0
for case in list(permutations([i for i in range(1, n+1)], n)):
    friend.append(case)
    winner, absence, jiwoo = 0, 1, 0
    
    a = friend[2][0]
    b = friend[0][0]
    
    if outcome[a-1][b-1] == 2:
        winner = 2
        jiwoo += 1
    elif outcome[a-1][b-1] == 0:
        winner = 0
    else:
        winner = 0

    if jiwoo == k:
        answer = 1
        break

    i = 1
    while True:
        if jiwoo == k:
            answer = 1
            break

        if i >
        
        a = friend[winner][i]
        b = friend[absence][i]
        temp = find(winner, absence)

        if outcome[a-1][b-1] == 0:
            winner = absence
            if winner == 2:
                jiwoo += 1
        elif outcome[a-1][b-1] == 1:
            winner = absence
            if winner == 2:
                jiwoo += 1
        else:
            if winner == 2:
                jiwoo += 1
                
        absence = temp

    if answer == 1:
        break

print(answer)
        
        
        
