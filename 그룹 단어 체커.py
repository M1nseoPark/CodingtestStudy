n = int(input())
answer = 0
for _ in range(n):
    word = input()

    result = True
    book = []
    for i in range(len(word)):
        if len(book) == 0 or word[i] not in book:
            book.append(word[i])
            
        elif word[i] != book[-1]:
            result = False
            break

    if result:
        answer += 1

print(answer)
        

