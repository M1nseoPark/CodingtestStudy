import sys

n, k = sys.stdin.readline().split()
people = set()
for _ in range(int(n)):
    people.add(sys.stdin.readline().rstrip())

p = len(people)

if k == 'Y':
    print(p)
elif k == 'F':
    print(p//2)
else:
    print(p//3)
    
    
