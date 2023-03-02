test = int(input())
for _ in range(test):
    n, kv = map(int, input().split())
    time = list(map(int, input().split()))
    temp = [0] * n
    arr = []
    
    for i in range(kv):
        arr.append(list(map(int, input().split())))
    arr.sort()

    for i in range(kv):
        temp[arr[i][1]-1] = temp[arr[i][0]-1] + 1

    order = {}
    for i in range(n):
        if temp[i] in order:
            order[temp[i]].append(i)
        else:
            order[temp[i]] = [i]

    order = sorted(order.items())
    w = int(input())
    answer = [-1] * n
    b = 0
    for k, v in order:
        t = []
        for i in range(len(v)):
            answer[v[i]] = time[v[i]] + b
            t.append(answer[v[i]])
            
        if answer[w-1] != -1:
            break
        b = max(t)

    print(answer[w-1])
        
        
