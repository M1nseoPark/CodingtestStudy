text = input()
find = input()

k = len(find)

i = 0
answer = 0
while True:
    if i >= len(text):
        break
    
    if text[i:i+k] == find:
        answer += 1
        i += k
    else:
        i += 1

print(answer)
