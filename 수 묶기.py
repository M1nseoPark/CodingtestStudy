n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

zero = False
plus = 0
minus = 0

for i in range(n):
    if data[i] == 0:
        zero = True

    if data[i] < 0:
        minus += 1

    if data[i] > 1:
        plus += 1

answer = 0
while True:
    if minus <= 0 and plus <= 1:
        break

    if minus > 1:
        answer += (data[0] * data[1])
        data.pop(0)
        data.pop(0)
        minus -= 2
    elif minus == 1:
        if zero:
            data.pop(0)
            data.pop(0)
            zero = False
        else:
            answer += data[0]
            minus -= 1
            data.pop(0)

    if plus > 1:
        answer += (data[-1] * data[-2])
        data.pop()
        data.pop()
        plus -= 2
    
print(answer + sum(data))
        
        
        
    
    
        
        

    
    
    
