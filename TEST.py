def solution(n, k, cmd):
    answer = ''
    arr = [[i-1, i+1] for i in range(1, n+1)]
    arr[0][0], arr[-1][1] = -1, -1
    live = [True] * (n + 1)
    pre = -1
    
    for i in range(len(cmd)):
        if cmd[i][0] == 'U':
            x = int(cmd[i][2])
            while x > 0:
                if live[k]:
                    x -= 1
                    k -= 1
                    
        elif cmd[i][0] == 'D':
            x = int(cmd[i][2])
            while x > 0:
                if live[k]:
                    x -= 1
                    k += 1
            
        elif cmd[i][0] == 'C':
            pre = k
            live[k] = False
            
            if (k - 1) > 0:
                arr[k-1][1] = -1
                
            if (k + 1) <= n:
                arr[k+1][0] = -1
                k += 1
            else:
                k -= 1
        
        else:
            live[pre] = True
            for j in range(pre-1, 0, -1):
                if live[j]:
                    arr[pre][0] = j
                    break
            
            for j in range(pre+1, n+1):
                if live[j]:
                    arr[pre][1] = j
                    break
    print(live)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
