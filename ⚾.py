from itertools import permutations

n = int(input())
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

answer = 0
for pick in range(list(permutations([0,1,2,4,5,6,7,8], 8))):
    for i in range(n):
        odd = []
        even = []
        temp = pick[:3] + [3] + pick[3:]
        base = []
        out = 0

        while True:
        
        



