r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

time = 0
while True:
    if time > 100:
        time = -1
        break

    n = len(A)  # 행 개수 
    m = len(A[0])  # 열 개수
    
    if 0 <= (r - 1) < n and 0 <= (c - 1) < m and A[r-1][c-1] == k:
        break
    
    # R 연산
    if n >= m:
        rn = 0
        rst = []
        for i in range(n):
            dic = {}
            for j in range(m):
                if A[i][j] != 0:
                    if A[i][j] in dic:
                        dic[A[i][j]] += 1
                    else:
                        dic[A[i][j]] = 1

            dic = sorted(dic.items(), key=lambda x:(x[1], x[0]))
            arr = []
            for a, b in dic:
                arr.append(a)
                arr.append(b)

            rn = max(rn, len(arr))
            rst.append(arr)

        A = []
        for i in range(n):
            A.append(rst[i] + [0]*(rn-len(rst[i])))

    # C 연산 
    else:
        cn = 0
        rst = []
        for j in range(m):
            dic = {}
            for i in range(n):
                if A[i][j] != 0:
                    if A[i][j] in dic:
                        dic[A[i][j]] += 1
                    else:
                        dic[A[i][j]] = 1

            dic = sorted(dic.items(), key=lambda x:(x[1], x[0]))
            arr = []
            for a, b in dic:
                arr.append(a)
                arr.append(b)

            cn = max(cn, len(arr))
            rst.append(arr)
        
        A = [[0] * m for _ in range(cn)]
        for j in range(m):
            for i in range(cn):
                if 0 <= i < len(rst[j]):
                    A[i][j] = rst[j][i]

    A = A[:101][:101]
    time += 1

print(time)
