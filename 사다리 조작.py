n, m, h = map(int, input().split())
line = []
for _ in range(m):
    line.append(list(map(int, input().split())))


# 목적지로 가는 마지막 선 밑에 선을 추가하면 됨(목적지-출발지 개수만큼)
