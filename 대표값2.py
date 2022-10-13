A = []
for _ in range(5):
    A.append(int(input()))

A.sort()
print(sum(A) // 5)
print(A[2])
