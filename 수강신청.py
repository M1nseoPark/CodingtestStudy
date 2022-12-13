import sys

k, l = map(int, sys.stdin.readline().split())
student = {}
for i in range(1, l+1):
    s = sys.stdin.readline().rstrip()
    student[s] = i

student = sorted(student.items(), key=lambda x: x[1])

for i in range(min(k, len(student))):
    print(student[i][0])
        
        
