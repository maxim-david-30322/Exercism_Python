
def get_rounds(number):

    number1=number
    number2=number+1
    number3=number+2

    return list((number1,number2,number3,))
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    pass


def concatenate_rounds(rounds_1, rounds_2):

    return rounds_1+rounds_2
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass


def list_contains_round(rounds, number):

    if number in rounds:
        return True
    else:
        return False
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    pass


def card_average(hand):

    return sum(hand)/len(hand)
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    pass


def approx_average_is_average(hand):

    n=len(hand)
    med1=(hand[0]+hand[-1])/2
    med2=hand[n//2]
    med_good=sum(hand)/n

    if med1==med_good or med2==med_good:
        return True
    else:
        return False
     
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    pass


def average_even_is_average_odd(hand):

    odd=hand[::2]
    even=hand[1::2]

    even_med=sum(even)/len(even)
    odd_med=sum(odd)/len(odd)

    if even_med==odd_med:
        return True
    else:
        return False

    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):

    is_11=hand[-1]

    if is_11==11:
        hand[-1]=22
    return hand
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass