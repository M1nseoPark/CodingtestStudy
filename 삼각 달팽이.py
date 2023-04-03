def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    y, x = -1, 0
    idx = 1

    # n=5이면 [1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12], [13, 14], [15]
    # 즉 5번, n번만큼 작동하면 모든 값이 들어감 
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:   # 하
                y += 1
            elif i % 3 == 1:   # 우
                x += 1
            else:   # 상
                x -= 1
                y -= 1

            arr[y][x] = idx
            idx += 1

    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])

    return answer
