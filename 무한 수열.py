n, p, q = map(int, input().split())

answer = {}

def dfs(num):
    if num < 1:
        return 1

    elif num in answer:
        return answer[num]

    answer[num] = dfs(num//p) + dfs(num//q)
    return answer[num]


print(dfs(n))
    
