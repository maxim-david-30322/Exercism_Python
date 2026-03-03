def is_armstrong_number(number):

    digits=list(str(number))
    lenght=len(digits)
    sum=0
    for digit in digits:
        sum+=pow(int(digit),lenght)

    if sum==number:
        return True
    else:
        return False
    
    pass
