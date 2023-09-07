def solution(begin, end):
    answer = []
    
    def count(num):
        if num < 2:
            return 0
        
        result = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 and i <= 10000000:
                if num // i <= 10000000:    # (num//i <= 천만)이면 num//i도 n이 될 수 있음 
                    result = max(result, i, num//i)
                else:    
                    result = max(result, i) 
        
        return result
    
    
    for num in range(begin, end+1):
        answer.append(count(num))
        
    return answer