
from nonogram.algorithms.simulated_annealing import simulated_annealing


def test_simulated_annealing_finds_solution():
    starting_grid = [[1]]

    row_clues = [[1]]
    column_clues = [[1]]

    grid, errors, iterations, elapsed_time = simulated_annealing(
        starting_grid,
        row_clues,
        column_clues,
    )

    assert grid == [[2]]
    assert errors == 0
    assert iterations == 1
    assert elapsed_time >= 0


def test_simulated_annealing_preserves_starting_grid():
    starting_grid = [
        [1, 1],
        [1, 1],
    ]

    original = [row.copy() for row in starting_grid]

    simulated_annealing(
        starting_grid,
        [[1], []],
        [[1], []],
    )

    assert starting_grid == original


def test_simulated_annealing_respects_temperature_limit():
    starting_grid = [[1]]

    _, _, iterations, _ = simulated_annealing(
        starting_grid,
        [[2]],
        [[2]],
        initial_temperature=1.0,
        final_temperature=0.5,
        cooling_rate=0.5,
    )

    assert iterations == 1


def test_simulated_annealing_returns_best_solution():
    starting_grid = [[2]]

    grid, errors, iterations, elapsed_time = simulated_annealing(
        starting_grid,
        [[1]],
        [[1]],
    )

    assert grid == [[2]]
    assert errors == 0
    assert iterations == 1


def test_simulated_annealing_records_convergence_history():
    starting_grid = [[1]]
    convergence = []

    grid, errors, iterations, elapsed_time = simulated_annealing(
        starting_grid,
        [[1]],
        [[1]],
        convergence_history=convergence,
    )

    assert convergence == [2, 0]
    assert convergence[0] >= convergence[-1]
    assert convergence[-1] == errors
