from unittest import mock

import pytest

from src.crossovers import one_point


def test_one_point_does_not_return_same_objects():
    chromosome_one = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    chromosome_two = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    result = one_point(chromosome_one, chromosome_two)
    assert result[0] is not chromosome_one and result[1] is not chromosome_two


def test_one_point_unequal_chromosome_lengths_raises_value_error():
    with pytest.raises(ValueError):
        one_point([0], [1, 2])


def test_one_point_empty_chromosomes_raises_value_error():
    with pytest.raises(ValueError):
        one_point([], [])


def test_one_point_size_one_chromosomes_returns_swapped_chromosomes():
    assert ([1], [0]) == one_point([0], [1])


@mock.patch("src.crossovers.randrange")
def test_one_point_index_zero_returns_swapped_chromosomes(randrange):
    randrange.return_value = 0
    chromosome_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    chromosome_two = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert (chromosome_two, chromosome_one) == one_point(chromosome_one, chromosome_two)


@mock.patch("src.crossovers.randrange")
def test_one_point_last_index_returns_chromosomes_with_only_last_element_swapped(randrange):
    randrange.return_value = 9
    chromosome_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]
    chromosome_two = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected_two = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9]
    assert (expected_one, expected_two) == one_point(chromosome_one, chromosome_two)


@mock.patch("src.crossovers.randrange")
def test_one_point_arbitrary_index_returns_crossed_over_chromosomes(randrange):
    randrange.return_value = 5
    chromosome_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_one = [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
    chromosome_two = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected_two = [9, 8, 7, 6, 5, 5, 6, 7, 8, 9]
    assert (expected_one, expected_two) == one_point(chromosome_one, chromosome_two)
