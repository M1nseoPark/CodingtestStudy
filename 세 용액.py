# 투포인터 O, 거의 다 풀었는데 while 범위때매 

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 3000000001  # 초기 최댓값 지정해줄땐 항상 주의 
answer = [0, 0, 0]

for i in range(n-2):
    left, right = i+1, n-1

    while left < right:
        temp = arr[left] + arr[right] + arr[i]

        # answer 갱신 부분을 while문 내부로 넣어주기 
        if abs(temp) < result:
            answer[0], answer[1], answer[2] = arr[i], arr[left], arr[right]
            result = abs(temp)

        if temp > 0:
            right -= 1

        elif temp < 0:
            left += 1

        else:
            answer[0], answer[1], answer[2] = arr[i], arr[left], arr[right]
            break

print(answer[0], answer[1], answer[2])
    
    
    


        
    

