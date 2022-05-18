from collections.abc import Sequence
from copy import deepcopy
from random import randrange


def bit_flip(chromosome: Sequence) -> Sequence:
    """
    Perform a bit flip mutation. This mutation assumes the chromosome is a sequence of bits. Randomly select an index
    within the chromosome and change the value to not value.

        0 -> 1
        1 -> 0

    :param chromosome: Individual chromosome to be mutated. Assumed to be a sequence of bits.
    :type chromosome: Sequence
    :return: Copy of the mutated chromosome
    :rtype: Sequence
    """
    chromosome = deepcopy(chromosome)
    index = randrange(len(chromosome))
    chromosome[index] = type(chromosome[index])(not chromosome[index])
    return chromosome


def swap_index(chromosome: Sequence) -> Sequence:
    """
    Select two indices from the chromosome and swap their contents. This mutation is ideal for chromosomes of
    permutations of unique values. It is possible that the same index is selected twice. This situation is ignored and
    will result in an unchanged chromosome.

        For example, if indices 2 and 5 are selected
            [a, b, c, d, e, f, g] -> [a, b, f, d, e, c, g]

    :param chromosome: Individual chromosome to be mutated.
    :type chromosome: Sequence
    :return: Copy of the mutated chromosome
    :rtype: Sequence
    """
    chromosome = deepcopy(chromosome)
    index_one = randrange(len(chromosome))
    index_two = randrange(len(chromosome))
    chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
    return chromosome
