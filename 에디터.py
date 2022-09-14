import sys

signal1 = list(sys.stdin.readline().rstrip())   # 커서의 앞
signal2 = []   # 커서의 뒤

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip()
    if command[0] == 'P':
        signal1.append(command[2])
        
    elif command[0] == 'L':
        if signal1:
            signal2.append(signal1.pop())
            
    elif command[0] == 'D':
        if signal2:
            signal1.append(signal2.pop())
            
    else:
        if signal1:
            signal1.pop()


signal1.extend(reversed(signal2))   # extend는 append와 달리 리스트 원소만 넣음
print(''.join(signal1))   # 리스트 문자열로 출력하기      
        
