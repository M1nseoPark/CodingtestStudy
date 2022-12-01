n, m, t = map(int, input().split())
disk = []
for i in range(n):
    disk.append(list(map(int, input().split())))

def move(x, d, k):
    for i in range(x-1, n, x):
        if d == 0:
            for j in range(k):
                disk[i] = [disk[i].pop()] + disk[i]
        else:
            for j in range(k):
                temp = disk[i].pop(0)
                disk[i] = disk[i] + [temp]


def find():
    global disk
    same = [[0] * m for _ in range(n)]
    flag = False
    result, count = 0, 0

    for i in range(n):
        for j in range(m):
            if disk[i][j-1] == disk[i][j] and disk[i][j] != 0:
                same[i][j-1] = 1
                same[i][j] = 1
                flag = True


    for i in range(1, n):
        for j in range(m):
            if disk[i-1][j] == disk[i][j] and disk[i][j] != 0:
                same[i-1][j] = 1
                same[i][j] = 1
                flag = True

    for i in range(n):
        for j in range(m):
            if disk[i][j] != 0:
                result += disk[i][j]
                count += 1
                

    if flag:
        for i in range(n):
            for j in range(m):
                if same[i][j] == 1:
                    disk[i][j] = 0
                    
    elif not flag and count != 0:
        temp = result / count
        for i in range(n):
            for j in range(m):
                if float(disk[i][j]) > temp:
                    disk[i][j] -= 1
                elif disk[i][j] != 0 and float(disk[i][j]) < temp:
                    disk[i][j] += 1
        
    
for _ in range(t):
    x, d, k = map(int, input().split())
    move(x, d, k)
    find()

answer = 0
for i in range(n):
    for j in range(m):
        answer += disk[i][j]

print(answer)


