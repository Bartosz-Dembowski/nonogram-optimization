import copy
import random
import time

from nonogram.neighborhood import generate_neighborhood
from nonogram.objective import objective_function


def hill_climbing(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    max_iterations: int = 10000,
):
    """Run classical hill climbing optimization."""

    start_time = time.time()
    current_grid = copy.deepcopy(starting_grid)
    current_error = objective_function(
        current_grid, row_clues, column_clues
    )
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        neighbors = generate_neighborhood(current_grid)
        best_neighbor = min(
            neighbors,
            key=lambda grid: objective_function(
                grid, row_clues, column_clues
            ),
        )

        best_error = objective_function(
            best_neighbor, row_clues, column_clues
        )

        if best_error < current_error:
            current_grid = best_neighbor
            current_error = best_error
        else:
            break

        if current_error == 0:
            break

    elapsed_time = time.time() - start_time

    return current_grid, current_error, iteration, elapsed_time


def randomized_hill_climbing(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    max_iterations: int = 100000,
):
    """Run randomized hill climbing optimization."""

    start_time = time.time()
    current_grid = copy.deepcopy(starting_grid)
    current_error = objective_function(
        current_grid, row_clues, column_clues
    )
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        neighbors = generate_neighborhood(current_grid)
        random_neighbor = random.choice(neighbors)

        random_error = objective_function(
            random_neighbor, row_clues, column_clues
        )

        if random_error <= current_error:
            current_grid = random_neighbor
            current_error = random_error

        if current_error == 0:
            break

    elapsed_time = time.time() - start_time

    return current_grid, current_error, iteration, elapsed_time