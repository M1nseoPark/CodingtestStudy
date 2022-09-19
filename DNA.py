n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(input())

answer = ''
for i in range(m):
    temp = {}
    for j in range(n):
        if len(temp) == 0:
            temp[dna[j][i]] = 1
        elif dna[j][i] in temp:
            temp[dna[j][i]] += 1
        else:
            temp[dna[j][i]] = 1

    temp = sorted(temp.items(), key=lambda x:(x[1], x[0]), reverse=True)
    k = 0
    for t in range(len(temp)):
        if temp[t][1] == temp[0][1]:
            k += 1
        else:
            break

    answer += temp[k-1][0]

distance = 0
for i in range(n):
    for j in range(m):
        if dna[i][j] != answer[j]:
            distance += 1
            
print(answer)
print(distance)

    
    
    
    
    
