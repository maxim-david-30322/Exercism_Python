def square(number):

    i=1
    nr=1
    if number <1  or number >64:
        raise ValueError("square must be between 1 and 64")
    
    while i< number:
        nr=nr*2
        i+=1
    return nr
    
    pass


def total():

    i=1
    nr=1
    sum=1
    
    while i< 64:
        nr=nr*2
        i+=1
        sum=sum+nr
    return sum
    
    pass
