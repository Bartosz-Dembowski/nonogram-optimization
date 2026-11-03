from nonogram.algorithms.exhaustive_search import exhaustive_search


def test_exhaustive_search_finds_solution():
    row_clues = [[1], []]
    column_clues = [[1], []]

    grid, errors, elapsed_time, counter = exhaustive_search(
        2, 2, row_clues, column_clues
    )

    assert errors == 0
    assert grid == [[2, 1], [1, 1]]
    assert elapsed_time >= 0
    assert counter > 0


def test_exhaustive_search_returns_first_solution():
    row_clues = [[1]]
    column_clues = [[1]]

    grid, errors, elapsed_time, counter = exhaustive_search(
        1, 1, row_clues, column_clues
    )

    assert grid == [[2]]
    assert errors == 0
    assert counter == 2