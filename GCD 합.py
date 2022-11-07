from itertools import combinations

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    temp = list(combinations(arr[1:], 2))
    answer = 0
    
    for i in range(len(temp)):
        a, b = max(temp[i][0], temp[i][1]), min(temp[i][0], temp[i][1])

        while b != 0:
            k = a
            a = b
            b = k % b

        answer += a

    print(answer)

        
            
