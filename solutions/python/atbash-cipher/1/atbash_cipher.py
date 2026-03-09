def encode(plain_text):

    plain_to_cipher = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 
    'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 
    'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 
    'y': 'b', 'z': 'a'
}
    encod=[]
    for char in ",-.":
        plain_text=plain_text.replace(char,"")

    for count,l in enumerate((plain_text.lower()).replace(" ","")):
        if l in plain_to_cipher:
            encod.append(plain_to_cipher[l])
        if l.isdigit():
            encod.append(l)
        if (count+1)%5==0 and count != 0:
            encod.append(" ")
        

    if encod[-1]==" ":
        encod[-1]=""
        
    return "".join(encod) 


    pass

def decode(ciphered_text):


    cipher_to_plain = {
    'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd', 'v': 'e', 'u': 'f', 't': 'g', 's': 'h', 
    'r': 'i', 'q': 'j', 'p': 'k', 'o': 'l', 'n': 'm', 'm': 'n', 'l': 'o', 'k': 'p', 
    'j': 'q', 'i': 'r', 'h': 's', 'g': 't', 'f': 'u', 'e': 'v', 'd': 'w', 'c': 'x', 
    'b': 'y', 'a': 'z'
    }
    
    decod=[]
    
    cipher_text=ciphered_text.replace(" ","")
    for i,ch in enumerate(cipher_text):
        if not ch.isdigit():
            decod.append(cipher_to_plain[ch])
        else:
            decod.append(ch)


    return "".join(decod)

    


    

