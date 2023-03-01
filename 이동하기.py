n, m = map(int, input().split())
candy = []
for _ in range(n):
    candy.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0:
            if j != 0:
                candy[i][j] += candy[i][j-1]
        elif j == 0:
            candy[i][j] += candy[i-1][j]
        else:
            candy[i][j] += (candy[i-1][j] + candy[i][j-1] + candy[i-1][j-1])

for i in range(n):
    print(candy[i])
print(candy[n-1][m-1])
            
