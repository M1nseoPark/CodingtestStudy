n = int(input())

answer = 0
if n >= 100:
    answer += 99
    for i in range(100, n+1):
        a = i // 100
        i = i % 100
        b = i // 10
        i = i % 10
        
        if (a - b) == (b - i):
            answer += 1
else:
    answer += n

print(answer)
            
