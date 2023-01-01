meg = input()
key = input()

# 주어진 키 5x5크기의 표로 변환
visited = {}
arr = [['0'] * 5 for _ in range(5)]
y, x = 0, 0
for i in range(len(key)):
    if key[i] not in visited:
        visited[key[i]] = 1
        arr[y][x] = key[i]

        if x + 1 > 4:
            y += 1
            x = 0
        else:
            x += 1

sub = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if len(visited) != 25:
    for i in range(25):
        if sub[i] not in visited:
            visited[sub[i]] = 1
            arr[y][x] = sub[i]

            if x + 1 > 4:
                y += 1
                x = 0
            else:
                x += 1

result = {}
for i in range(5):
    for j in range(5):
        result[arr[i][j]] = [i, j]


# 메시지 두 글자씩 나누기
divide = []
m = len(meg)
i = 0
while True:
    if i == m - 1:
        divide.append(meg[i] + 'X')
        break
    elif i == m:
        break

    if meg[i] != meg[i+1]:
        divide.append(meg[i:i+2])
        i += 2
    else:
        if meg[i] == 'X':
            divide.append('XQ')
        else:
            divide.append(meg[i]+'X')
        i += 1


# 암호화하기
answer = ''
for i in range(len(divide)):
    a, b = divide[i][0], divide[i][1]

    ar = result[a]
    br = result[b]

    # 두 글자가 같은 행에 존재하면 
    if ar[0] == br[0]:
        answer += (arr[ar[0]][(ar[1]+1)%5] + arr[br[0]][(br[1]+1)%5])
    
    # 두 글자가 같은 열에 존재하면 
    elif ar[1] == br[1]:
        answer += (arr[(ar[0]+1)%5][ar[1]] + arr[(br[0]+1)%5][br[1]])
    
    # 두 글자가 표에서 서로 다른 행, 열에 존재하면 
    else:
        answer += (arr[ar[0]][br[1]] + arr[br[0]][ar[1]])

print(answer)

