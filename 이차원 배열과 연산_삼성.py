# 어려운 문제가 아닌 것 같은데.. 왜 틀리는지 모르겠음..
r, c, k = map(int, input().split())
A = [[0] * 100 for _ in range(100)]
for i in range(3):
    a, b, d = map(int, input().split())
    A[i][0], A[i][1], A[i][2] = a, b, d

# [2, 1, 3, 1, 1, 2]
def array(line):
    temp = {}
    for i in range(len(line)):
        if line[i] == 0:
            break

        if len(temp) == 0 or line[i] not in temp:
            temp[line[i]] = 1
        else:
            temp[line[i]] += 1

    temp = sorted(temp.items(), key=lambda x:(x[1], x[0]))
    result = []
    for i in range(len(temp)):
        result.append(temp[i][0])
        result.append(temp[i][1])

    return result


# array([3, 1, 1, 2, 0, 0, 0])
rc, lc = 3, 3   # 열의 개수, 행의 개수
cnt = 0
while True:
    if cnt == 100:
        print(-1)
        break

    if A[r-1][c-1] == k:
        print(cnt)
        break

    if rc <= lc:
        for i in range(lc):
            rst = array(A[i])
            A[i][:len(rst)] = rst
            A[i][len(rst):rc] = [0] * (rc - len(rst))
            rc = max(rc, len(rst))
    else:
        for i in range(rc):
            rst = array(list(z[i] for z in A))
            for z in range(len(rst)):
                A[z][i] = rst[z]
            for z in range(len(rst), 100):
                if A[z][i] != 0:
                    A[z][i] = 0
                else:
                    break

            lc = max(lc, len(rst))

    cnt += 1
