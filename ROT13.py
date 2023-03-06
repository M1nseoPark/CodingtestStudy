s = input()
answer = ''

for i in range(len(s)):
    a = ord(s[i])
    if 65 <= a <= 90:
        if a + 13 > 90:
            answer += chr(a-13)
        else:
            answer += chr(a+13)

    elif 97 <= a <= 122:
        if a + 13 > 122:
            answer += chr(a-13)
        else:
            answer += chr(a+13)

    else:
        answer += s[i]

print(answer)
        
    
    
