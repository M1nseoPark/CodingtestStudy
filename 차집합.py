na, nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = list(set(A) - set(B))
answer.sort()
if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(' '.join(map(str, answer)))
