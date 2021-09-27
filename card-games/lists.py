def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    for num in rounds:
        if num==number:
            return True

    return False


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    hand_sum=0
    for num in hand:
        hand_sum+=num

    return hand_sum/(len(hand))


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    med_index=int(len(hand)/2)
    median=hand[med_index]

    quick_average=(hand[0]+hand[-1])/2

    return median==card_average(hand) or quick_average==card_average(hand)


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_sum=0
    odd_sum=0

    list_length=len(hand)
    num_count=list_length/2
    if list_length%2==0:
        even_count=num_count
        odd_count=num_count
    else:
        even_count=int(num_count)+1
        odd_count=int(num_count)

    even_list=hand[::2]
    odd_list=hand[1::2]

    for num in even_list:
        even_sum+=num

    for num in odd_list:
        odd_sum+=num

    return (even_sum/even_count)==(odd_sum/odd_count)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1]==11:
        hand[-1]=22
    return hand
