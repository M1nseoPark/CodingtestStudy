# 십자 모양으로 선택해야 하면 DFS
# 어떤 경우가 이미 선택되었는지 코드를 짜기 힘들었음

seat = []
for _ in range(5):
    seat.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [0 for _ in range(25)]
checked = [[0] * 5 for _ in range(5)]

def pick(
    

        
        
