n = int(input())
speak = input()
m = len(speak)

left, right = 0, 0
kind = {}
kind[speak[left]] = 1
answer = 0

while left < m and right < m:
    if len(kind) > n:
        if kind[speak[left]] == 1:
            del kind[speak[left]]
        else:
            kind[speak[left]] -= 1
        left += 1

    else:
        answer = max(answer, right - left + 1)
        right += 1
        if right < m:
            if speak[right] not in kind:
                kind[speak[right]] = 1
            else:
                kind[speak[right]] += 1


print(answer)
        
        
        
        
    
    
    
