# 가장 큰 크기의 색종이를 먼저 사용하는 것이 최선이 아님! -> 모든 경우 검사 필요 

papers = []
one, answer = 0, 100
used = [0] + [5]*5   # 남은 색종이의 수(5종류의 색종이 각각 5개씩)
for _ in range(10):
    paper = list(map(int, input().split()))
    one += sum(paper)   # 종이의 1의 개수
    papers.append(paper)


def check(r, c, leng, full):
    for i in range(leng):
        full -= sum(papers[r+i][c:c+leng])
    if full != 0:
        return False
    else:
        return True
    

def recursive(one, cnt):
    global answer

    # 1이 적힌 모든 칸에 색종이를 붙였다면 
    if one == 0:
        answer = min(answer, cnt)
        return

    # 이전에 구한 색종이 개수보다 필요한 색종이가 많아지면 
    if cnt >= answer:
        return

    # 색종이를 모두 써버렸으면 
    if sum(used) == 0:
        return

    for r in range(10):
        for c in range(10):
            # 1. 종이 내 1의 위치 찾기 
            if papers[r][c] == 1:
                for i in range(5, 0, -1):   # 큰 색종이부터
                    if used[i] != 0 and r+i <= 10 and c+i <= 10:
                        # 2. 각 색종이를 붙일 수 있는지 검사(sum 이용)
                        if check(r, c, i, i**2):
                            for y in range(r, r+i):
                                for x in range(c, c+i):
                                    papers[y][x] = 0

                            used[i] -= 1
                            recursive(one-i**2, cnt+1)  # 재귀 이용(다른 부분 채우러가기)

                            # 백트래킹
                            for y in range(r, r+i):
                                for x in range(c, c+i):
                                    papers[y][x] = 1
                            used[i] += 1
                return
                            

if not one:   # 색종이에 1이 없으면 
    print(0)
else:
    recursive(one, 0)
    if answer == 100:
        print(-1)
    else:
        print(answer)

