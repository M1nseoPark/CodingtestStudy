# 뒷부분에 공백을 더해주면 오답임 
n = int(input())
for i in range(1, n+1):
    print((' ' * (n - i)) + ('*' * (2 * i - 1)))
    
