n, m = -1, -1
head, tail = [0] * 100001, [0] * 100001
prev, next = [0] * 100001, [0] * 100001
dic = {}   # 물건 번호: [무게, 벨트 번호]

# 100 12 3 / 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
def build(order):
    n, m = order[1], order[2]   # 12 3
    belt = [[] for _ in range(m)]

    idx = 0
    for i in range(0, n, n//m):  # 0 4 8 
        for j in range(n//m):
            belt[idx].append(order[i+j+3])
            dic[order[i+j+3]] = [order[i+j+3+n], idx]
        idx += 1
    
    print(belt)
    print(dic)
    


q = int(input())
for _ in range(q):
    order = list(map(int, input().split()))

    if order[0] == 100:
        build(order)
