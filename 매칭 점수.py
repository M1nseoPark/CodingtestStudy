import re

def solution(word, pages):
    dic = {}
    kind = []
    name = []
    
    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        score = 0
        for f in re.findall('[a-zA-Z]+', page.lower()):
            if f == word.lower():
                score += 1

        link = re.findall('<a href="(https://[\S]*)"', page)

        for i in link:
            if i not in dic:
                dic[i] = [url]
            else:
                dic[i].append(url)

        name.append(url)
        kind.append([url, score, len(link)])


    result, answer = 0, 0
    for i in range(len(kind)):
        url = kind[i][0]
        score = kind[i][1]

        if url in dic:
            for i in dic[url]:
                a, b, c = kind[name.index(i)]
                score += (b / c)

        if result < score:
            result = score
            answer = i

    return answer
            
                

        
        
            
