from nonogram.convergence import (
    calculate_average_curve,
    classical_hill_climbing_curve,
    randomized_hill_climbing_curve,
)


def test_calculate_average_curve():
    curves = [
        [10, 8, 5],
        [12, 9],
        [8, 6, 4, 2],
    ]

    result = calculate_average_curve(curves)

    assert result == [10.0, 23 / 3, 6.0, 16 / 3]


def test_classical_hill_climbing_curve():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    row_clues = [[1], [1]]
    column_clues = [[1], [1]]

    curve = classical_hill_climbing_curve(
        starting_grid,
        row_clues,
        column_clues,
    )

    assert curve[0] == 4
    assert curve[-1] <= curve[0]
    assert all(
        curve[index] > curve[index + 1]
        for index in range(len(curve) - 1)
    )


def test_randomized_hill_climbing_curve():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    row_clues = [[1], [1]]
    column_clues = [[1], [1]]

    curve = randomized_hill_climbing_curve(
        starting_grid,
        row_clues,
        column_clues,
    )

    assert curve[0] == 4
    assert curve[-1] <= curve[0]
    assert all(
        curve[index] >= curve[index + 1]
        for index in range(len(curve) - 1)
    )