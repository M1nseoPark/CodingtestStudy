import sys

r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))

count = 1
visited = {}
end = False

for x in range(c):
    temp = ''
    for y in range(r):
        temp += arr[y][x]

    visited[temp] = 1
            

while True:
    new = {}
    for i in visited:
        if i[count:] not in new:
            new[i[count:]] = 1
        else:
            end = True
            break

    if end:
        break
    else:
        count += 1
        
print(count-1)
    
        
