from itertools import permutations
import sys

n = int(sys.stdin.readline())
score = []
for _ in range(n):
    score.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for pick in list(permutations([1,2,3,4,5,6,7,8], 8)):
    result, k = 0, 0
    for i in range(n):
        temp = list(pick[:3]) + [0] + list(pick[3:])
        base1, base2, base3 = 0, 0, 0
        out = 0

        while out != 3:
            t = temp[k%9]
            if score[i][t] == 0:
                out += 1

            elif score[i][t] == 1:
                result += base3
                base1, base2, base3 = 1, base1, base2

            elif score[i][t] == 2:
                result += base3
                result += base2
                base1, base2, base3 = 0, 1, base1

            elif score[i][t] == 3:
                result += base3
                result += base2
                result += base1
                base1, base2, base3 = 0, 0, 1

            else:
                result += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0

            k += 1

    answer = max(answer, result)

print(answer)
                
                    
            
