# 어렵다.. 풀이를 읽어도 모르겠음..

n = int(input())
scale = list(map(int, input().split()))

scale.sort()

answer = 1
for i in range(n):
    if answer < scale[i]:
        break

    answer += scale[i]

print(answer)



        
        
