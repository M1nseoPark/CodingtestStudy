def solution(files):
    answer = []
    
    for file in files:
        # 인덱스로 풀면 런타임 에러남.. head, number은 한 글자 이상이라는 조건이 있는데 왜?
        head, number, tail = '', '', ''
        
        for i in range(len(file)):
            if not file[i].isdigit() and number == '':
                head += file[i]
            elif file[i].isdigit() and tail == '':
                number += file[i]
            else:
                tail += file[i]
        
        answer.append([head, number, tail])
    
    
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
            
    return [''.join(i) for i in answer]
