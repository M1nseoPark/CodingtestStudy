# 굳이 이렇게 복잡하게 풀 필요 없었음..
# 커플석의 수에 따라 출력이 변함

n = int(input())
seat = input()

holder = []
i = 0
while True:
    if i >= (n - 1):
        holder.append('*')
        break

    if seat[i] == 'S':
        holder.append('*')
        holder.append('S')
        i += 1

    if seat[i] == 'L':
        holder.append('*')
        holder.append('L')
        holder.append('L')
        i += 2

l = 0
r = 1
flag = False
while True:
    if len(holder) == 0:
        break
    
    if '*' not in holder:
        break

    if ('S' not in holder) and ('L' not in holder):
        flag = True
        break
    
    if (holder[r] == 'S' or holder[r] == 'L') and (holder[l] == '*'):
        holder.pop(r)
        holder.pop(l)
    elif (holder[l] == 'S' or holder[l] == 'L') and (holder[r] == '*'):
        holder.pop(r)
        holder.pop(l)
    else:
        l += 1
        r += 1

if flag:
    print(n)
else:
    print(n - len(holder))

    
        
