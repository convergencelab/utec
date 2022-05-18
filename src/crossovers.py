from collections.abc import Sequence
from copy import deepcopy
from random import randrange


def one_point(chromosome_one: Sequence, chromosome_two: Sequence) -> Sequence:
    """
    Perform one point crossover. Randomly select an index and swap all elements after the index between the two
    chromosomes. Assume chromosomes are of equal length.

        For example, if index 3 is selected
            [a, b, c, d, e, f, g] -> [a, b, c, w, x, y, z]
            [t, u, v, w, x, y, z] -> [t, u, v, d, e, f, g]

    :param chromosome_one: One of the two chromosome to perform crossover on.
    :type chromosome_one: Sequence
    :param chromosome_two: The other chromosome to perform crossover on.
    :type chromosome_two: Sequence
    :return: The two offspring resulting from the crossover.
    :rtype: Tuple of Sequences (Sequence, Sequence)
    """
    if len(chromosome_one) != len(chromosome_two):
        raise ValueError("chromosomes must be of equal length")
    chromosome_one = deepcopy(chromosome_one)
    chromosome_two = deepcopy(chromosome_two)
    index = randrange(len(chromosome_one))
    chromosome_one[index:], chromosome_two[index:] = chromosome_two[index:], chromosome_one[index:]
    return chromosome_one, chromosome_two
