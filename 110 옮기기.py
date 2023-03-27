from collections import deque

def solution(s):
    answer = []

    for i in range(len(s)):
        stack = []
        cnt = 0

        for j in s[i]:
            if j == '0':
                if stack[-2:] == ['1', '1']:
                    cnt += 1
                    stack.pop()
                    stack.pop()
                # 앞에 2개가 1,1이 아니면 그냥 0을 추가 
                else:
                    stack.append(j)
            else:
                stack.append(j)

        # 110이 없기 때문에 변화 불가능 
        if cnt == 0:
            answer.append(s[i])
            
        # 110이 있다면 
        else:
            q = deque()

            # 0이 나오기 전까지는 append
            while stack:
                if stack[-1] == '1':
                    q.append(stack.pop())
                else:
                    break

            # 0이 나왔다면 110을 주어진 cnt만큼 append
            while cnt > 0:
                q.appendleft('0')
                q.appendleft('1')
                q.appendleft('1')
                cnt -= 1

            # stack에 남아있는거 다 추가
            while stack:
                q.appendleft(stack.pop())
                
            answer.append(''.join(q))

    return answer
            
