def is_valid(isbn):

    isbn_clear=isbn.replace("-","")
    if len(isbn_clear)!=10:
        return False
    total_sum=0
    for index,nr in enumerate(isbn_clear):
        if nr == "X" and index==9:
            nr=nr.replace("X","10")
        if not nr.isdigit():
            return False
        
        nr=int(nr)
        total_sum+=nr*(10-index)
    return total_sum%11==0
