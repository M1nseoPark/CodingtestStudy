n = int(input())
answer = []
for _ in range(n):
    s = input()

    cnt = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if len(cnt) != 0:
                answer.append(int(cnt))
            cnt = ''
        else:
            cnt += s[i]

    if len(cnt) != 0:
        answer.append(int(cnt))

answer.sort()
for i in answer:
    print(i)
    
