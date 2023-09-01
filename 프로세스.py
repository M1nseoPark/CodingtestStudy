from collections import deque

# 첫 번째 풀이 
# def solution(priorities, location):
#     answer = 1
#     q = deque(priorities)
    
#     while len(q) > 1:
#         cur = q.popleft()
        
#         if cur < max(q):
#             q.append(cur)
#             if location == 0:
#                 location = len(q) - 1
#             else:
#                 location -= 1
#         else:
#             if location == 0:
#                 return answer
#             else:
#                 answer += 1
#                 location -= 1
        
#         #print(q, location, answer)
            
#     return answer

#solution([1, 1, 1, 2], 2)


# 두 번째 풀이 
def solution(priorities, location):
	stack = deque()
	for i in range(len(priorities)):
		stack.append([priorities[i], i])
	
	answer = 0
	while True:
		target = stack.popleft()
		
		flag = True
		for i in range(len(stack)):
			if target[0] < stack[i][0]:
				flag = False
				break
		if flag:
			answer += 1
			if target[1] == location:
				break
		else:
			stack.append(target)
            
	return answer
