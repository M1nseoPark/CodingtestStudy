n = int(input())

five = n // 5
answer = 0
while True:
    if five < 0:
        answer = -1
        break
    
    temp = n - (5 * five)
    if temp % 3 == 0:
        answer = five + (temp // 3)
        break

    five -= 1

print(answer)
