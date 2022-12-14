s = input()
n = len(s)

left, right = 0, 0
answer = set()

# 이중 for문으로 풀 수도 있음 
while left < n:
    if right >= n:
        left += 1
        right = left

    else:
        answer.add(s[left:right+1])
        right += 1

print(len(answer))
    
