def solution(n, k, cmd):
    graph = {i:[i-1, i+1] for i in range(n)}
    graph[0] = [None, 1]
    graph[n-1] = [n-2, None]
    cur = k

    dele = []
    answer = ['O'] * n

    for c in cmd:
        # 삭제 
        if c == 'C':
            answer[cur] = 'X'
            prev, next = graph[cur]
            dele.append([prev, cur, next])
            # 현재 선택된 행 구하기
            if next == None:   # 삭제된 행이 가장 마지막 행일 때
                cur = graph[cur][0]
            else:
                cur = graph[cur][1]

            # 표 상태 변경하기
            if prev == None:   # 삭제된 행이 가장 처음 행일 때
                graph[next][0] = None
            elif next == None:   # 삭제된 행이 가장 마지막 행일 때 
                graph[prev][1] = None
            else:
                graph[prev][1] = next
                graph[next][0] = prev

        # 복구
        elif c == 'Z':
            prev, now, next = dele.pop()
            answer[now] = 'O'
            if prev == None:
                graph[next][0] = now
            elif next == None:
                graph[prev][1] = now
            else:
                graph[next][0] = now
                graph[prev][1] = now

        # 커서 이동
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = graph[cur][1]
            else:
                for _ in range(c2):
                    cur = graph[cur][0]


    return ''.join(answer)
                

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
