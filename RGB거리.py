n = int(input())
price = []
for _ in range(n):
    price.append(list(map(int, input().split())))

for i in range(1, n):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + price[i][0]
    price[i][1] = min(price[i-1][0], price[i-1][2]) + price[i][1]
    price[i][2] = min(price[i-1][0], price[i-1][1]) + price[i][2]

print(min(price[n-1][0], price[n-1][1], price[n-1][2]))
    
    
    
