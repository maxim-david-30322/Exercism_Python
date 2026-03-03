import math
def score(x:float, y:float)->int:

    '''
    this function takes one point (X,Y) and returns the 
    score that it striked
    '''
    score_d=math.hypot(x, y)
    outer_d=10
    middle_d=5
    inner_d=1
    if score_d>outer_d:
        return 0
    elif score_d>middle_d:
        return 1
    elif score_d>inner_d:
        return 5
    else:
        return 10
    pass
