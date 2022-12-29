

a, b, c = map(int, input().split())

visited = []
answer = 0

def dfs(arr):
    global answer
    if answer == 1:
        return
    
    if arr[0] == arr[1] and arr[1] == arr[2]:
        answer = 1
        return
    
    arr.sort()
    if arr in visited:
        answer = 0
        return

    visited.append(arr)

    a, b, c = arr[0], arr[1], arr[2]

    if a != b:
        dfs([a+a, b-a, c])
    if a != c:
        dfs([a+a, b, c-a])
    if b != c:
        dfs([a, b+b, c-b])


dfs([a, b, c])
print(answer)

        
    
