import re

def is_isogram(string):

    words=[]
    clean=re.sub(r"[^a-z]", "", string.lower())
    for _,w in enumerate(clean):
        if w not in words:
            words.append(w)
    
    return len(words)==len(clean)


