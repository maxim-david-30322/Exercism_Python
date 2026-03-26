
def rows(letter):
    letter = letter.lower()
    alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    #print (int(alphabet.index("a")))
    
    index=0
    left=0
    right=0

    rows_list = []
    while index <= int(alphabet.index(letter)):

        row=list()
        left=int(alphabet.index(letter))-index
        right=index
        if left!=0:
 
            while left>0:
                row.append(" ")
                left-=1

        row.append(alphabet[index].capitalize())

        if right!=0:
            while right>0:
                row.append(" ")
                right-=1
        minus1=row[:-1]
        row=row+(row[::-1][1:])
        rows_list.append(row)
        index+=1
        #print (row)
    # Inverse the order
    rows_list = rows_list + rows_list[-2::-1]
    
    return ["".join(row) for row in rows_list]




