import re

def solution(word, pages):
    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        score = 0
        for f in re.findall(
        
        
    

        
    
    
