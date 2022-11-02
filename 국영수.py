n = int(input())
student = []
for _ in range(n):
    a, b, c, d = input().split()
    student.append([a, int(b), int(c), int(d)])

student.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(student[i][0])
