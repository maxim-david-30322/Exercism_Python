def is_pangram(sentence):
    alfabet = set('abcdefghijklmnopqrstuvwxyz')
    
    for i,l in enumerate(sentence.lower()):
        if l in alfabet:
            alfabet.remove(l)
            

    if not alfabet:
        return True
    else:
        return False



