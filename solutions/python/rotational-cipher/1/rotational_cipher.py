def map_char(w, key):
    if 'a' <= w <= 'z':
        base = ord('a')
        return chr((ord(w) - base + key) % 26 + base)
    if 'A' <= w <= 'Z':
        base = ord('A')
        return chr((ord(w) - base + key) % 26 + base)
    return w


def rotate(text, key):
    
   


    return "".join(map_char(w, key) for w in text)
        
    