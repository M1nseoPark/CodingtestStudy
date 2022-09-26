l, c = map(int, input().split())
word = list(input().split())

answer = []
def makeCode(code):
    if len(code) == l:
        vowel = 0

        # 모음 개수 굳이 미리 세어줄 필요 없이 마지막에 세는게 편함
        for i in range(l):
            if code[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1

        if vowel >= 1 and (l - vowel) >= 2:
            answer.append(code)
                
    else:
        for i in range(c):
            if len(code) == 0:
                code += word[i]
                makeCode(code)
                code = code[:-1]
            # word가 정렬되었더라도 원소를 추가할 때는 조건이 필요함
            elif word[i] not in code and word[i] > code[-1]:
                code += word[i]
                makeCode(code)
                code = code[:-1]


code = ''
makeCode(code)
answer.sort()

for i in answer:
    print(i)

    

    
