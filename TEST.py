'''
1 3 6 10
3 5 9 
3 7 12 18
4 9 15 22

1 3 6 10
3 8 15 24
6 15 27 42
10 24 42 64
'''
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]

for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i-1][j]


for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    if x1 > 2 and y1 > 2:
        print(arr[y2-1][x2-1] - arr[y2-1][x1-2] - arr[y1-2][x1-1] + arr[y1-2][x1-2])
    elif x1 > 2:
        print(arr[y2-1][x2-1] - arr[y2-1][x1-2])
    elif y1 > 2:
        print(arr[y2-1][x2-1] - arr[y1-2][x1-1])
    else:
        print(arr[y2-1][x2-1])