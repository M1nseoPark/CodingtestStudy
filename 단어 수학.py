n = int(input())

word1 = []
dic = {}

for i in range(n):
    word1.append(input())

for i in range(n):
    for j in range(len(word1[i])):
        if word1[i][j] in dic:
            dic[word1[i][j]] += 10 ** (len(word1[i])-j-1)
        else:
            dic[word1[i][j]] = 10 ** (len(word1[i])-j-1)

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
dic2 = {}
idx = 9
for i in range(len(dic)):
    dic2[dic[i][0]] = idx
    idx -= 1

answer = 0
for i in range(n):
    temp = ''
    for j in range(len(word1[i])):
        temp += str(dic2[word1[i][j]])

    answer += int(temp)

print(answer)
        
        
    
    
        
                
                
                
            
        
    
    

