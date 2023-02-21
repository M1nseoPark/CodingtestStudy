import sys

k = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split())

ans1, ans2 = '', ''
visited = [False] * 10


def check(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j


def solve(depth, s):
    global ans1, ans2   # ans1 = 최대 정수, ans2 = 최소 정수 

    if depth == k+1:
        if len(ans2) == 0:
            ans2 = s   # 처음 생긴 문자열이 최소값
        else:
            ans1 = s   # 마지막에 생긴 문자열이 최대값 
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth-1]):
                visited[i] = True
                solve(depth+1, s+str(i))
                visited[i] = False


solve(0, '')
print(ans1)
print(ans2)
    
    
            
        
    
            
            
