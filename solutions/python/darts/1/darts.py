import math
def score(x, y):


    score_d=math.sqrt(x**2+y**2)
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
