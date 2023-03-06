def solution(commands):
    answer = []
    table = [[[0, []] for _ in range(51)] for _ in range(51)]
    kind = {}
    
    for i in range(len(commands)):
        com = commands[i].split(' ')
        if com[0] == 'UPDATE':
            if len(com) == 4:
                r, c, v = int(com[1]), int(com[2]), com[3]
                table[r][c][0] = v
                for r1, c1 in table[r][c][1]:
                    table[r1][c1][0] = v
                
                if v in kind:
                    kind[v].append([r, c] + table[r][c][1])
                else:
                    kind[v] = [r, c] + table[r][c][1]
            
            else:
                v1, v2 = com[1], com[2]
                if v1 in kind:
                    for r1, c1 in kind[v1]:
                        table[r1][c1] = v2
                    
                    kind[v2] = kind[v1]
                    del kind[v1]
        
        elif com[0] == 'MERGE':
            r1, c1, r2, c2 = int(com[1]), int(com[2]), int(com[3]), int(com[4])
            if table[r2][c2][0] != 0 and table[r1][c1][0] == 0:
                table[r1][c1][0] = table[r2][c2][0]
            else:
                table[r2][c2][0] = table[r1][c1][0]
            
            table[r1][c1][1].append([r2, c2])
            table[r2][c2][1].append([r1, c1])
        
        elif com[0] == 'UNMERGE':
            r, c = int(com[1]), int(com[2])
            for r1, c1 in table[r][c][1]:
                table[r1][c1][1].remove([r, c])
                table[r1][c1][0] = 0
                
            table[r][c][1] = []
        
        else:
            r, c = int(com[1]), int(com[2])
            if table[r][c] == 0:
                answer.append('EMPTY')
            else:
                answer.append(table[r][c])
            
    return answer

solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
