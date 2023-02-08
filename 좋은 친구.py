import sys

n, k = map(int, sys.stdin.readline().split())
student = [0] * n
num = [0] * 21  # 이름의 길이(최대 20글자)
answer = 0

for i in range(n):
    student[i] = len(sys.stdin.readline().rstrip())   # 이름의 길이만 저장 
    if i > k:
        num[student[i-k-1]] -= 1   # 등수 차이가 K보다 크면 친구 아님 
    answer += num[student[i]]   
    num[student[i]] += 1

print(answer)
    
    
