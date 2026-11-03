
from nonogram.algorithms.tabu_search import tabu_search


def test_tabu_search_finds_solution():
    starting_grid = [[1]]

    row_clues = [[1]]
    column_clues = [[1]]

    grid, errors, iterations, elapsed_time, history = tabu_search(
        starting_grid,
        row_clues,
        column_clues,
    )

    assert grid == [[2]]
    assert errors == 0
    assert iterations == 1
    assert elapsed_time >= 0
    assert len(history) == 2


def test_tabu_search_respects_iteration_limit():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    row_clues = [[1], []]
    column_clues = [[1], []]

    _, _, iterations, _, _ = tabu_search(
        starting_grid,
        row_clues,
        column_clues,
        max_iterations=1,
    )

    assert iterations == 1


def test_tabu_search_does_not_modify_starting_grid():
    starting_grid = [[1]]
    original = [row.copy() for row in starting_grid]

    tabu_search(
        starting_grid,
        [[1]],
        [[1]],
    )

    assert starting_grid == original


def test_tabu_search_records_convergence_history():
    starting_grid = [[1]]
    convergence = []

    grid, errors, iterations, elapsed_time, history = tabu_search(
        starting_grid,
        [[1]],
        [[1]],
        convergence_history=convergence,
    )

    assert convergence == [2, 0]
    assert convergence[0] >= convergence[-1]
    assert convergence[-1] == errors
