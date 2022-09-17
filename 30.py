n = int(input())

text = str(n)
answer = True

temp = 0
for i in range(len(text)):
    temp += int(text[i])
    
if (text.find('0') == -1) or (temp % 3 != 0):
    answer = False

if not answer:
    print(-1)
else:
    print(''.join(sorted(text)[::-1]))


    
