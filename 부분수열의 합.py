import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

def pick(cnt, tot):
    global answer
    
    if cnt == n:
        if tot == s:
            answer += 1

    else:
        # arr[cnt]를 더한 경우와 더하지 않은 경우
        pick(cnt+1, tot)
        pick(cnt+1, tot+arr[cnt])
        

pick(0, 0)

# 크기가 양수인 부분수열만 세줌 -> s가 0이면 공집합도 포함됨!!
if s == 0:
    answer -= 1
    
print(answer)
                
                
