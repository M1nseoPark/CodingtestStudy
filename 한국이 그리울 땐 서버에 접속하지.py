n = int(input())
p = input()
m = len(p)
idx = p.index('*')
np = p[:idx] + p[idx+1:]

for _ in range(n):
    s = input()

    answer = True
    if len(s) < m:
        if np != s:
            answer = False

    else:
        for i in range(idx):
            if p[i] != s[i]:
                answer = False
                break

        for i in range(m-1, idx, -1):
            if p[i] != s[i+len(s)-m]:
                answer = False
                break

    if answer:
        print('DA')
    else:
        print('NE')
            
    
