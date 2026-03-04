def to_rna(dna_strand):
    dic={"G":"C","C":"G","T":"A","A":"U"}
    d=[]
    for w in dna_strand:
        if w not in dic:
            return False
        d.append(dic[w])
    
    return ''.join(d)
    