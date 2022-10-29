def hanoi(a, b, n):
    if n == 1:
        move.append([a, b])
        return

    hanoi(a, 6-a-b, n-1)
    move.append([a, b])
    hanoi(6-a-b, b, n-1)
    
       
n = int(input())
move = []

hanoi(1, 3, n)

print(len(move))
for i in range(len(move)):
    print(move[i][0], move[i][1])
