n = int(input())
port = []
for _ in range(n):
    port.append(list(map(int, input().split())))

sx = 0   # 상어의 초기 위치
sy = 0
shark = 1   # 상어의 크기
fish = []   # 물고기의 크기 및 위치
for i in range(n):
    for j in range(n):
        if port[i][j] in [1, 2, 3, 4, 5, 6]:
            fish.append([port[i][j], i, j])

        if port[i][j] == 9:
            sx = j
            sy = i


move = []

if len(fish) == 0:
    print(0)
else:
    for i in range(len(fish)):
        
    

    
