import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline()))


left, right = 0, 0
answer = 0

# 회전 초밥 -> 원형 (이걸 고려 안해줌)
while left != n:
    right = left + k
    eat = set()  # 가능한 한 다양한 종류의 초밥 -> set 이용
    flag = True

    for i in range(left, right):
        i %= n   # 원형 리스트 
        eat.add(sushi[i])
        if sushi[i] == c:
            flag = False

    cnt = len(eat)
    if flag:
        cnt += 1

    answer = max(answer, cnt)
    left += 1


print(answer)



    
    
    




        
    
        
    
                    
    

    



    
