EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int number of layers you want to add
    :return: int how many minutes it takes to make the layers

    Function takes number of layers as an argument and returns how many
    minutes it will take to prepare the layers for lasagna
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elasped time in minutes.
    :param number_of_layers: int number of layers you want to add to calculate
    preparation time.
    :param elapsed_bake_time: int how much time has already elapsed on the bake

    Function takes number of layers and elapsed bake time and
    will call preparation_time_in_minutes to calculate total elapsed time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
