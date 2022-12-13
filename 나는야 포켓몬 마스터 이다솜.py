import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}
for i in range(1, n+1):
    pokemon[str(i)] = sys.stdin.readline().rstrip()

# 처음에 입력 받을 때 이름-번호로 매칭하는 딕셔너리를 하나 더 만들었으면 더 빠를듯 
value = {v:k for k,v in pokemon.items()}
for _ in range(m):
    q = input()
    if q in pokemon:
        print(pokemon.get(q))
    else:
        print(value.get(q))
    
    
    
