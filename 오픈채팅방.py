def solution(record):
    answer = []
    name = {}
    result = []
    
    for i in range(len(record)):
        temp = record[i].split(' ')
        if temp[0] == 'Enter':
            name[temp[1]] = temp[2]
            result.append([temp[0], temp[1]])
        
        elif temp[0] == 'Leave':
            result.append([temp[0], temp[1]])
        
        else:
            name[temp[1]] = temp[2]
    
    for i in range(len(result)):
        if result[i][0] == 'Enter':
            answer.append(name[result[i][1]] + '님이 들어왔습니다.')
        else:
            answer.append(name[result[i][1]] + '님이 나갔습니다.')        
            
    return answer
