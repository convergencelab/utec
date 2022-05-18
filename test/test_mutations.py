from unittest import mock

import pytest

from src.mutations import bit_flip, inversion, swap_index


def test_bit_flip_empty_chromosome_raises_value_error():
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


def test_inversion_empty_chromosome_raises_value_error():
    with pytest.raises(ValueError):
        inversion([])


def test_inversion_size_one_chromosome_returns_equal_chromosome():
    assert [99] == inversion([99])


@mock.patch("src.mutations.randrange")
def test_inversion_same_random_indices_returns_equal_chromosome(randrange):
    randrange.side_effect = [2, 2]
    chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert expected == inversion(chromosome)


@mock.patch("src.mutations.randrange")
def test_inversion_adjacent_random_indices_returns_equal_chromosome(randrange):
    randrange.side_effect = [2, 3]
    chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert expected == inversion(chromosome)


@mock.patch("src.mutations.randrange")
def test_inversion_indices_for_full_chromosome_returns_reversed_chromosome(randrange):
    randrange.side_effect = [0, 10]
    chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert expected == inversion(chromosome)


@mock.patch("src.mutations.randrange")
def test_inversion_arbitrary_chromosome_returns_correctly_mutated_chromosome(randrange):
    randrange.side_effect = [1, 5]
    chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
    assert expected == inversion(chromosome)


def test_swap_index_empty_chromosome_raises_value_error():
    with pytest.raises(ValueError):
        swap_index([])


def test_swap_index_size_one_chromosome_returns_equal_chromosome():
    assert [99] == swap_index([99])


@mock.patch("src.mutations.randrange")
def test_swap_index_arbitrary_chromosome_returns_correctly_mutated_chromosome(randrange):
    randrange.side_effect = [2, 6]
    chromosome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 1, 6, 3, 4, 5, 2, 7, 8, 9]
    assert expected == swap_index(chromosome)
