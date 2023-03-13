import sys

test = int(sys.stdin.readline())
for _ in range(test):
    k = int(sys.stdin.readline())   # 소설을 구성하는 장의 개수 
    file = list(map(int, sys.stdin.readline().split()))   # 1장부터 K장까지 수록된 파일 크기

    # dp[a][b] = a부터 b까지의 그룹의 압축 최소 비용
    dp = [[0] * k for _ in range(k)]
    dic = {-1: 0}   # key까지의 부분합
    for i in range(k):
        dic[i] = dic[i-1] + file[i]

    for size in range(1, k):   # 그룹의 크기
        for start in range(k-size):   # 그룹의 시작 인덱스 범위는 0부터 k-2까지
            end = start + size

            rst = float('inf')
            for i in range(start, end):
                rst = min(rst, dp[start][i] + dp[i+1][end] + dic[end] - dic[start-1])

            dp[start][end] = rst

    print(dp[0][-1])            
            
