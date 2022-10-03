r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

num = 0
while num < 100:
    if len(A) <= len(A[0]):   # R 연산 수행
        for i in range(len(A)):
            temp = {}
            for j in range(len(A[0])):
                if len(temp) == 0 or A[i][j] not in temp:
                    temp[A[i][j]] = 1
                else:
                    temp[A[i][j]] += 1

            temp = sorted(temp.items(), key=lambda x: x[1])
            A[i].clear()
            for key, value in temp.items():
                A[i].append(key)
                A[i].append(value)

    else:   # C 연산 수행
        for i in range(len(A[0])):
            temp = {}
            for j in range(len(A)):
                if len(temp) == 0 or A[j][i] not in temp:
                    temp[A[j][i]] = 1
                else:
                    temp[A[j][i]] += 1

            temp = sorted(temp.items(), key=lambda x: x[1])
            
        
                
        
