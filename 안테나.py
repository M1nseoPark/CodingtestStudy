n = int(input())
house = list(map(int, input().split()))

house.sort()
answer1 = 0
answer2 = 0
if n % 2 == 1:
    print(house[n//2])
else:
    for i in range(n):
        answer1 += abs(house[n//2-1] - house[i])
        answer2 += abs(house[n//2] - house[i])

    if answer1 >= answer2:
        print(house[n//2-1])
    else:
        print(house[n//2])
        
    
