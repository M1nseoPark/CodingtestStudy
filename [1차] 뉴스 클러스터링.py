def solution(str1, str2):
    # 문자열 두 글자씩 끊기
    A, B = {}, {}
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        flag = True
        for j in range(2):
            if (65 <= ord(temp[j]) <= 90) or (97 <= ord(temp[j]) <= 122):
                continue
            else:
                flag = False
                break
        
        if flag:
            temp = temp.upper()
            if temp not in A:
                A[temp] = 1
            else:
                A[temp] += 1
    
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        flag = True
        for j in range(2):
            if (65 <= ord(temp[j]) <= 90) or (97 <= ord(temp[j]) <= 122):
                continue
            else:
                flag = False
                break
        
        if flag:
            temp = temp.upper()
            if temp not in B:
                B[temp] = 1
            else:
                B[temp] += 1

                
    # 자카드 유사도 구하기
    SA = set(A)
    SB = set(B)
    
    union = SA | SB
    inter = SA & SB
    
    result1, result2 = 0, 0
    for i in inter:
        result1 += min(A[i], B[i])
    for i in union:
        if (i in A) and (i in B):
            result2 += max(A[i], B[i])
        elif i in A:
            result2 += A[i]
        else:
            result2 += B[i]
    
    answer = 0
    if result1 == 0 and result2 == 0:
        answer = 1
    else:
        answer = result1 / result2
    
    answer = int(answer * 65536)
    return answer

