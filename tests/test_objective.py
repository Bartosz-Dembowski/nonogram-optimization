from nonogram.objective import (
    extract_blocks,
    compare_blocks,
    objective_function,
)


def test_extract_blocks():
    assert extract_blocks([2, 2, 1, 2, 2, 2]) == [2, 3]
    assert extract_blocks([1, 1, 1]) == []
    assert extract_blocks([2, 2, 2]) == [3]
    assert extract_blocks([]) == []


def test_compare_blocks():
    assert compare_blocks([3, 2], [3, 2]) == 0
    assert compare_blocks([3, 1], [3, 2]) == 1
    assert compare_blocks([1, 3], [3, 2]) == 2
    assert compare_blocks([3], [3, 2]) == 1


def test_objective_function():
    grid = [
        [2, 1],
        [1, 1],
        [1, 2],
    ]

    row_clues = [[1], [], [1]]
    column_clues = [[1], [1]]

    assert objective_function(grid, row_clues, column_clues) == 0
import pytest


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([2, 1, 2], [1, 1]),
        ([1, 2, 2, 1], [2]),
        ([1, 1, 1], []),
        ([2, 2, 2], [3]),
        ([], []),
        ([2, 1, 1, 2], [1, 1]),
    ],
)
def test_extract_blocks_edge_cases(sequence, expected):
    assert extract_blocks(sequence) == expected


@pytest.mark.parametrize(
    "actual, expected, errors",
    [
        ([], [], 0),
        ([2], [2], 0),
        ([2], [], 1),
        ([], [2], 1),
        ([3, 2], [2, 3], 2),
        ([1, 2], [1, 2], 0),
    ],
)
def test_compare_blocks_edge_cases(actual, expected, errors):
    assert compare_blocks(actual, expected) == errors