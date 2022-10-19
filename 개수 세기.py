n = int(input())
A = list(map(int, input().split()))
v = int(input())

A.sort()
answer = 0
for i in range(n):
    if A[i] == v:
        answer += 1
    elif A[i] > v:
        break

print(answer)
        
    
        
