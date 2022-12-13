n = int(input())
note = {}
for _ in range(n):
    a, b = input().split()

    if (len(note) == 0) or (a not in note):
        if b == 'enter':
            note[a] = b
    elif a in note:
        if b == 'leave':
            del note[a]

answer = []
for i in note:
    answer.append(i)

answer.sort(reverse=True)
for i in answer:
    print(i)
        
    

