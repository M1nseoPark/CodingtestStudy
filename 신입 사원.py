import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    grade = []
    for i in range(n):
        grade.append(list(map(int, sys.stdin.readline().split())))
    
    grade.sort()
    answer = n
    temp = grade[0][1]
    for j in range(1, n):
        if temp > grade[j][1]:
            temp = grade[j][1]
        else:
            answer -= 1
            
    print(answer)
