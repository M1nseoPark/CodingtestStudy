# 어려운 문제는 아닌데 이중 for문을 너무 두려워했음

n, k = map(int, input().split())
use = list(map(int, input().split()))

plug = []
answer = 0

for i in range(k):
    # 이미 있다면
    if use[i] in plug:
        continue

    if len(plug) < n:
        plug.append(use[i])
        continue

    far = 0  # 가장 나중에 사용하게 될 것
    temp = 0  # 뽑아버릴 후보
    for j in range(n):
        # 앞으로 사용할 일이 없으면
        if plug[j] not in use[i:]:
            temp = plug[j]
            break

        # 현재 플러그에 꽂혀있는 것의 사용 순서 -> 현재 플러그에 꽂혀있는 것 중 가장 나중에 쓸거 찾기
        elif use[i:].index(plug[j]) > far:
            far = use[i:].index(plug[j])
            temp = plug[j]

    plug[plug.index(temp)] = use[i]
    answer += 1


print(answer)
    
    
        
