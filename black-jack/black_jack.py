"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_one_value < card_two_value:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand); numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    if card_one == 'A':
        card_one_value = 11
        card_two_value = value_of_card(card_two)
    elif card_two == 'A':
        card_one_value = value_of_card(card_one)
        card_two_value = 11
    else:
        card_one_value = value_of_card(card_one)
        card_two_value = value_of_card(card_two)

    two_card_sum = card_one_value + card_two_value

    if two_card_sum < 11:
        return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    royal_cards = ['10', 'J', 'Q', 'K']

    hand = (card_one, card_two)

    royal_card_in_hand = False
    ace_card_in_hand = False

    for card in royal_cards:
        if card in hand:
            royal_card_in_hand = True

    if 'A' in hand:
        ace_card_in_hand = True

    return royal_card_in_hand and ace_card_in_hand


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    if card_one == card_two:
        return True
    elif card_one == 'Q' and card_two == 'K':
        return True
    elif card_one == 'K' and card_two == 'Q':
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    two_card_sum = card_one_value + card_two_value

    if two_card_sum in range(8, 12):
        return True
    else:
        return False
