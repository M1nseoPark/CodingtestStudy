def solution(s):
    answer = 0

    # 난 왜 문자열을 절반으로 나누는데 집착했지?
    def isTrue(x):
        if x == x[::-1]:
            return True

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isTrue(s[i:j]):
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
    
    return answer
