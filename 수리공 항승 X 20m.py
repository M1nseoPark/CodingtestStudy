n, l = map(int, input().split())
water = list(map(int, input().split()))

water.sort()
tape = []
for i in range(n-1):
    tape.append(water[i+1] - water[i])

k = 0
answer = 0
temp = 0
while True:
    if k == len(tape):
        if temp != 0:
            answer += 1
        break
    
    temp += tape[k]
    
    if (temp + 1) >= l:
        answer += 1
        temp = 0

    k += 1

    print(temp, k)

print(answer // 2 + 1)
        
        
