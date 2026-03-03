def classify(number):
    divizors=[]

    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    pass


    for d in range(1,number):
        if number%d==0:
            divizors.append(d)
    
    #divizors.pop(divizors.index(number))

    sumd=sum(divizors)

    if sumd<number:
        return ("deficient")
    elif sumd==number:
        return("perfect")
    return ("abundant")
