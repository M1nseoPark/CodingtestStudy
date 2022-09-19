# 처음에 나올 수 있는 모든 경우를 리스트에 저장해주었다가 메모리 초과

s = input()
t = input()

while len(t) != len(s):
    if t[-1] == 'A':
        t = t[:-1]

    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)
        
    
    
