# dp[시작][끝] = (시작~끝) 범위에 있는 행렬을 모두 곱할 때 최소 연산 수
def solution(sizes):
    dp = [[[0] * len(sizes)] for _ in range(len(sizes))]

    for gap in range(1, len(sizes)):
        for s in range(len(sizes)-gap):
            e = s + gap

            temp = []
            for m in range(s, e):
                temp.append(dp[s][m]+dp[m+1][e]+size[s][0]*size[m][1]*size[e][1])

            dp[s][e] = min(temp)
