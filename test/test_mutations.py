from unittest import mock

import pytest

from src.mutations import bit_flip


def test_bit_flip_empty_chromosome_returns_empty_chromosome():
    with pytest.raises(ValueError):
        bit_flip([])


def test_bit_flip_list_of_zero_chromosome_returns_list_of_one():
    assert [1] == bit_flip([0])


def test_bit_flip_list_of_one_chromosome_returns_list_of_zero():
    assert [0] == bit_flip([1])


@mock.patch("src.mutations.randrange")
def test_bit_flip_arbitrary_chromosome_returns_correctly_mutated_chromosome(randrange):
    randrange.return_value = 5
    chromosome = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    expected = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
    assert expected == bit_flip(chromosome)
