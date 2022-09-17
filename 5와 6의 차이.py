A, B = map(int, input().split())

A_max = list(str(A))
A_min = list(str(A))
B_max = list(str(B))
B_min = list(str(B))

for i in range(len(A_max)):
    if A_max[i] == '5':
        A_max[i] = '6'
    elif A_max[i] == '6':
        A_min[i] = '5'

for i in range(len(B_max)):
    if B_max[i] == '5':
        B_max[i] = '6'
    elif B_max[i] == '6':
        B_min[i] = '5'

print((int(''.join(A_min)) + int(''.join(B_min))),
      (int(''.join(A_max)) + int(''.join(B_max))))
