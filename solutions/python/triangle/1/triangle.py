
def equilateral(sides):
    if all(set(sides))==0:
        return False
    sorted_sides=sorted(sides)
    if sum(sorted_sides[:-1]) < sorted_sides[-1]:
        return False
        
    return len(sides)>0 and len(set(sides))==1
pass


def isosceles(sides):
    if all(set(sides))==0:
        return False
    sorted_sides=sorted(sides)
    if sum(sorted_sides[:-1]) < sorted_sides[-1]:
        return False
        
    sets=set(sides)
    return len(sides)>0 and len(set(sides))<=2

    pass


def scalene(sides):
    if equilateral(sides):
        return False
    if isosceles(sides):
        return False
    
    if all(set(sides))==0:
        return False
    
    sorted_sides=sorted(sides)

    if len(sides)>0 and len(set(sides))==3 and not sum(sorted_sides[:-1]) < sorted_sides[-1]:
        return True

    return False


