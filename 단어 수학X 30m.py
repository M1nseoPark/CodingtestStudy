n = int(input())
word = []
maxi = 0
match = {}

for _ in range(n):
    w = input()
    word.append(w)
    if maxi <= len(w):
        maxi = len(w)

change = [0 for _ in range(n)]
temp = 9
for i in range(maxi-1, -1, -1):
    for j in range(n):
        if len(word[j]) == (i + 1):
            if len(match) == 0:
                change[j] += temp * (10 ** i)
                match[word[j][0]] = temp
                temp -= 1
            elif word[j][0] in match:
                change[j] += match[word[j][0]] * (10 ** i)
            else:
                change[j] += temp * (10 ** i)
                match[word[j][0]] = temp
                temp -= 1

            word[j] = word[j][1:]

print(sum(change))
                
                
                
            
        
    
    

