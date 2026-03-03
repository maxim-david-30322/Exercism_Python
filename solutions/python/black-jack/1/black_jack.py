"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
    
    if card in cards:
        return cards[card]
    else:
        return int(card)
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    pass


def higher_card(card_one, card_two):
    cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

    if card_one in cards:
        c1=cards[card_one]
    else:
        c1=int(card_one)

    if card_two in cards:
        c2=cards[card_two]
    else:
        c2=int(card_two)
    
    if c1<c2:
        return card_two
    elif c1>c2:
        return card_one
    else:
        return card_one,card_two
        
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    pass


def value_of_ace(card_one, card_two):
    cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

    if card_one in cards:
        c1=cards[card_one]
    else:
        c1=int(card_one)

    if card_two in cards:
        c2=cards[card_two]
    else:
        c2=int(card_two)


    sum = c1+c2

    if c1 == 1 or c2 == 1:
        return 1
    elif c1+c2<=10:
        return 11
    elif c1+c2>10:
        return 1
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def is_blackjack(card_one, card_two):
    cards = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}

    if card_one in cards:
        c1=cards[card_one]
    else:
        c1=int(card_one)

    if card_two in cards:
        c2=cards[card_two]
    else:
        c2=int(card_two)

    sum=c1+c2
    if sum ==21:
        return True
    else:
        return False
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one, card_two):
    cards = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}

    if card_one in cards:
        c1=cards[card_one]
    else:
        c1=int(card_one)

    if card_two in cards:
        c2=cards[card_two]
    else:
        c2=int(card_two)

    if c1==c2:
        return True
    else:
        return False
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

    if card_one in cards:
        c1=cards[card_one]
    else:
        c1=int(card_one)

    if card_two in cards:
        c2=cards[card_two]
    else:
        c2=int(card_two)

    sum=c1+c2
    if sum in [9,10,11]:
        return True
    else:
        return False
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
