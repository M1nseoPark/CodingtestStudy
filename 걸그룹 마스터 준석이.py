n, m = map(int, input().split())
group = {}
member = {}
for _ in range(n):
    name = input()
    group[name] = []
    k = int(input())
    
    for i in range(k):
        girl = input()
        group[name].append(girl)
        member[girl] = name
        

for _ in range(m):
    q = input()
    t = int(input())

    if t == 0:
        answer = group.get(q)
        answer.sort()
        for i in range(len(answer)):
            print(answer[i])
    else:
        print(member.get(q))
    
    
        
        
