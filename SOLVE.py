import re

def solution(word, pages):
    answer = 0
    link = {}
    
    for i in range(len(pages)):
        page = pages[i].split('\n')
        start = False
        content1 = ''
        now = ''
        for j in range(len(page)):
            if len(page[j]) > 33 and page[j][26:33] == 'content':
                p = page[j][43:]
                now = p[:-3]
                if p[:-3] not in link:
                    link[p[:-3]] = [0, []]
            
            if len(page[j]) > 7 and page[j][3:7] == 'href':
                ll = page[j].split('>')
                l = ll[0][17:]; l = l[:-1]
                if l in link:
                    link[l][1].append(now)
                else:
                    link[l] = [0, []]
            
            if page[j] == '<body>':
                start = True
            
            if page[j] == '</body>':
                start = False
            
            if start:
                content1 += page[j]
        
        content2 = ''
        start = True
        for i in content1:
            if i == '<':
                start = False
            if start:
                content2 += i
            if i == '>':
                start = True
        
        content3 = re.split('\W+', content2)
        for i in range(len(content3)):
            if content3[i].lower() == word.lower():
                link[now][0] += 1
                
    print(link)
        
    return answer
    

