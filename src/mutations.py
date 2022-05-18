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
