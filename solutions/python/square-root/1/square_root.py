def square_root(number):
    if number==1:
        return 1
    
    square=1
    while pow(square,2)<number:
        square+=1
    
    return square