n = int(input())

for i in range(n):
    word = list(input().split())
    answer = word[::-1]
    
    print("Case #" + str(i+1) + ": ", end='')
    print(' '.join(answer))
    
