n = int(input())

# 소수 구하기 
arr = [True for _ in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if arr[i]:
        for j in range(i+i, n+1, i):
            arr[j] = False

prime = []
for i in range(2, n+1):
    if arr[i]:
        prime.append(i)


# n을 연속된 소수의 합으로 나타낼 수 있는 경우의 수 구하기
answer = 0
if len(prime) != 0:
    left, right = 0, 0
    m = len(prime)
    temp = prime[0]

    while left < m and right < m:
        if temp == n:
            answer += 1
            temp -= prime[left]
            left += 1

        elif temp < n:
            right += 1
            if right == m:
                break
            else:
                temp += prime[right]

        else:
            temp -= prime[left]
            left += 1

print(answer)
        
            
        

    
    
    


    
