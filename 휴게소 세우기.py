n, m, l = map(int, input().split())
arr = list(map(int, input().split()))

# 82 201 411 555 622 755
#  119 210 144 67  133

rest = m
while rest != 0:
    arr.sort()
    temp = []

    for i in range(len(arr)-1):
        temp.append([arr[i+1]-arr[i], arr[i]])

    temp.sort()

    if len(temp) >= rest:
        for i in range(rest):
            arr.append(temp[i][1] + (temp[i][0] // 2))
            rest -= 1
    else:
        for i in range(len(temp)):
            arr.append(temp[i][1] + (temp[i][0] // 2))
            rest -= 1

arr.sort()
print(arr)
answer = 0
for i in range(len(arr)-1):
    answer = max(answer, arr[i+1]-arr[i])

print(answer)
            
        
        
