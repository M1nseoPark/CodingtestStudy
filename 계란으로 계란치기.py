import sys

n = int(sys.stdin.readline())
egg = []
for _ in range(n):
    egg.append(list(map(int, sys.stdin.readline().split())))

def hit(idx):
    global answer

    if idx == n:
        temp = 0
        for i in range(n):
            if egg[i][0] <= 0:
                temp += 1
        answer = max(temp, answer)
        return

    # 자기가 깨져있는 경우 다음 계란으로
    if egg[idx][0] <= 0:
        hit(idx + 1)
        return

    # 자기 빼고 다 깨져있는 경우
    broken = True
    for i in range(n):
        if idx == i:
            continue
        
        if egg[i][0] > 0:
            broken = False
            break

    if broken:
        answer = max(n - 1, answer)
        return
    
    for i in range(n):
        if idx == i or egg[i][0] <= 0:
            continue

        egg[i][0] -= egg[idx][1]
        egg[idx][0] -= egg[i][1]
        hit(idx + 1)
        egg[i][0] += egg[idx][1]
        egg[idx][0] += egg[i][1]
        
        
answer = 0
hit(0)
print(answer)
        
