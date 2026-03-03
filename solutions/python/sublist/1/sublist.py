"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = ("A is sublist of B") 
SUPERLIST = ("A is a superlist of B")
EQUAL = ("A and B are equal")
UNEQUAL = ("A and B are unequal")


# def sublist2(list_one, list_two):
#     if list_one==list_two:
#         return ("A and B are equal")
#     elif list_one in list_two:
#         return ("A is sublist of B") 
#     elif list_two in list_one:
#         return("A is a superlist of B")
#     pass


def sublist(list_one,list_two):

    A=".".join(map(str,list_one))+"."
    B=".".join(map(str,list_two))+"."

    if A==B:
        return EQUAL
    elif A in B:
        return SUBLIST
    elif B in A:
        return SUPERLIST
    return UNEQUAL
    pass
