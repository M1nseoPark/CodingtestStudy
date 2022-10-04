dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

dwarf.sort()
result, i = 0, 0
answer = []

while True:
    if result == 100:
        break

    if result > 100:
        result -= answer[-1]
        answer.pop()
        answer.append(dwarf[i])
    else:
        answer.append(dwarf[i])

    i += 1
        
for i in range(7):
    print(answer[i])

    
    
