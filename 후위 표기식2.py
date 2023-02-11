n = int(input())
s = input()
dic = {}
for i in range(n):
    dic[chr(65+i)] = int(input())

stack = []
for i in range(len(s)):
    if s[i].isalpha():
        stack.append(dic[s[i]])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(str(b)+s[i]+str(a)))

print(f"{stack[0]:.2f}")
    
