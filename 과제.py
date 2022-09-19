n = int(input())
homework = []
for _ in range(n):
    homework.append(list(map(int, input().split())))

homework.sort(key=lambda x:(x[1], x[0]), reverse=True)

print(homework)
    
