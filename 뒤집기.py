s = input()

one = 0
zero = 0
change = False
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        change = True
    else:
        change = False

    if change and s[i] == '0':
        zero += 1
    if change and s[i] == '1':
        one += 1

if s[-1] == '0':
    zero += 1
else:
    one += 1

print(min(zero, one))
