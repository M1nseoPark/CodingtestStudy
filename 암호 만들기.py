l, c = map(int, input().split())
arr = list(input().split())

code = []
visited = [False for _ in range(c)]
arr.sort()

def pick(code):
    if len(code) == l:
        vo, co = 0, 0
        for i in code:
            if i in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1

        if co >= 2 and vo >= 1:
            print(''.join(code))

    else:
        for i in range(c):
            if (not visited[i]) and (len(code) == 0 or code[-1] < arr[i]):
                code.append(arr[i])
                visited[i] = True
                pick(code)
                code.pop()
                visited[i] = False

pick(code)

