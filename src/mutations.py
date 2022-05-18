from copy import deepcopy
from random import randrange


def bit_flip(chromosome):
    """
    Perform a bit flip mutation. This mutation assumes the chromosome is a sequence of bits. Randomly select an index
    within the chromosome and change the value to not value.

        0 -> 1
        1 -> 0

    :param chromosome: Individual chromosome to be mutated. Assumed to be a sequence of bits.
    :return: Copy of the mutated chromosome
    """
    chromosome = deepcopy(chromosome)
    index = randrange(0, len(chromosome))
    chromosome[index] = type(chromosome[index])(not chromosome[index])
    return chromosome


def swap_index(chromosome):
    """
    Select two indices from the chromosome and swap their contents. This mutation is ideal for chromosomes of
    permutations of unique values.

        For example, if indices 2 and 5 are selected
            [a, b, c, d, e, f, g] -> [a, b, f, d, e, c, g]

    :param chromosome: Individual chromosome to be mutated.
    :return: Copy of the mutated chromosome
    """
    chromosome = deepcopy(chromosome)
    index_one = randrange(len(chromosome))
    index_two = randrange(len(chromosome))
    chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
    return chromosome
