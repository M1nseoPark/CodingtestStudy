m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

new = [[] for _ in range(m)]   # 각 우주의 순위 리스트 
dict = {}

for i in range(m):
    temp = sorted(list(set(arr[i])))  # 각 우주에서 중복을 제거하여 정렬한 리스트 
    for j in range(len(temp)):
        dict[temp[j]] = j   # {1: 0, 2: 1, 3: 2} -> 중복 제거 필요 

    for j in arr[i]:
        new[i].append(dict[j])


new.sort()
cnt, ans = 1, 0
for i in range(1, m):
    if new[i] == new[i-1]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2   ## ?
        cnt = 1

ans += cnt * (cnt - 1) // 2
print(ans)

    
