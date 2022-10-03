word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

answer = 0
i = 0
while True:
    if i >= len(word):
        break
        
    if (i < len(word) - 1) and word[i] + word[i+1] in croatia:
        answer += 1
        i += 2
    elif (i < len(word) - 2) and word[i] + word[i+1] + word[i+2] in croatia:
        answer += 1
        i += 3
    else:
        answer += 1
        i += 1

print(answer)
