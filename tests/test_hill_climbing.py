from nonogram.algorithms.hill_climbing import (
    hill_climbing,
    randomized_hill_climbing,
)


def test_hill_climbing_finds_solution():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    row_clues = [[1], []]
    column_clues = [[1], []]

    grid, errors, iterations, elapsed_time = hill_climbing(
        starting_grid, row_clues, column_clues
    )

    assert errors == 0
    assert grid == [[2, 1], [1, 1]]
    assert iterations > 0
    assert elapsed_time >= 0


def test_hill_climbing_does_not_modify_starting_grid():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    original = [row.copy() for row in starting_grid]

    hill_climbing(
        starting_grid,
        [[1], []],
        [[1], []],
    )

    assert starting_grid == original


def test_randomized_hill_climbing_finds_solution():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    row_clues = [[1], []]
    column_clues = [[1], []]

    grid, errors, iterations, elapsed_time = randomized_hill_climbing(
        starting_grid, row_clues, column_clues
    )

    assert errors == 0
    assert grid == [[2, 1], [1, 1]]
    assert iterations > 0
    assert elapsed_time >= 0


def test_randomized_hill_climbing_respects_iteration_limit():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    _, _, iterations, _ = randomized_hill_climbing(
        starting_grid,
        [[1], []],
        [[1], []],
        max_iterations=1,
    )

    assert iterations <= 1
