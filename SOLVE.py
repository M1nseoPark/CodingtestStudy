r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

rc, cc = 3, 3   # 행의 크기, 열의 크기
time = 0
while True:
    if rc >= r and cc >= c:
        if A[r-1][c-1] == k:
            print(time)
            break
    
    time += 1
    
    if time > 100:
        print(-1)
        break

    # R 연산 수행 
    if rc >= cc:
        tc = 0
        for i in range(rc):
            temp = {}
            for j in range(cc):
                if A[i][j] != 0:
                    if A[i][j] in temp:
                        temp[A[i][j]] += 1
                    else:
                        temp[A[i][j]] = 1

            arr = list(zip(temp.keys(), temp.values()))
            arr.sort(key=lambda x: (x[1], x[0]))
            A[i] = list(sum(arr, ()))
            tc = max(tc, len(A[i]))

        for i in range(rc):
            if len(A[i]) < tc:
                A[i] += [0] * (tc - len(A[i]))

        cc = tc

    # C 연산 수행
    else:
        tr = 0
        for i in range(cc):
            temp = {}
            for j in range(rc):
                if A[j][i] != 0:
                    if A[j][i] in temp:
                        temp[A[j][i]] += 1
                    else:
                        temp[A[j][i]] = 1

            arr = list(zip(temp.keys(), temp.values()))
            arr.sort(key=lambda x: (x[1], x[0]))
            arr = list(sum(arr, ()))
            rc = max(rc, len(arr))

            if rc > len(A):
                for _ in range(rc - len(A)):
                    A.append([0] * cc)
            else:
                for j in range(len(arr), len(A)):
                    A[j][i] = 0

            for j in range(len(arr)):
                A[j][i] = arr[j]


