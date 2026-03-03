def leap_year(number):
    if number%100 ==0 and number%400==0:
        return True
    elif number%100 ==0 and not number%400==0:
        return  False
    elif number %4 ==0:    
        return  True
    else:
        return  False


    pass
