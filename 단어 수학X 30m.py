n = int(input())
word = []
length = []
match = {}

for i in range(n):
    w = input()
    word.append(w)
    length.append([len(w), i])

length.sort(reverse=True)
answer = 0
k = 9
for i in range(n):
    temp = ''
    for j in range(length[i][0]):
        if (len(match) == 0) or (word[length[i][1]][j] not in match):
            match[word[length[i][1]][j]] = k
            temp += str(k)
            k -= 1
        elif word[length[i][1]][j] in match:
            temp += str(match[word[length[i][1]][j]])

        print(match)
    answer += int(temp)

print(answer)
        
    
    

