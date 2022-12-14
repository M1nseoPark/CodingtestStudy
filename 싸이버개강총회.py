import sys

s, e, q = sys.stdin.readline().split()
sh, sm = map(int, s.split(':'))
eh, em = map(int, e.split(':'))
qh, qm = map(int, q.split(':'))

s = sh * 60 + sm
e = eh * 60 + em
q = qh * 60 + qm

cin = {}
cout = {}

# 입력받는 것 때매 약간 헤맴 
while True:
    try:
        temp = list(sys.stdin.readline().split())

        th, tm = map(int, temp[0].split(':'))
        time = th * 60 + tm

        if (time <= s) and (temp[1] not in cin):
            cin[temp[1]] = time

        elif (e <= time <= q) and (temp[1] in cin) and (temp[1] not in cout):
            cout[temp[1]] = time
            
    except:
        break
        

print(len(cout))
        
        
