modify = input()

subtract = modify.split('-')
answer = 0

for i in range(len(subtract)):
    temp = list(map(int, subtract[i].split('+')))
    if i == 0:
        answer += sum(temp)
    else:
        answer -= sum(temp)
    
print(answer)
