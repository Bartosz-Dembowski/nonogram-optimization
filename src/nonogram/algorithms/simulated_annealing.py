import copy
import math
import random
import time

from nonogram.neighborhood import generate_neighborhood
from nonogram.objective import objective_function


def simulated_annealing(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    initial_temperature: float = 100.0,
    final_temperature: float = 0.1,
    cooling_rate: float = 0.95,
    convergence_history: list[int] | None = None,
):
    """Run simulated annealing optimization."""

    start_time = time.time()

    current_grid = copy.deepcopy(starting_grid)
    current_error = objective_function(
        current_grid, row_clues, column_clues
    )

    best_grid = copy.deepcopy(current_grid)
    best_error = current_error

    if convergence_history is not None:
        convergence_history.append(best_error)

    temperature = initial_temperature
    iteration = 0

    while temperature > final_temperature:
        iteration += 1

        neighbors = generate_neighborhood(current_grid)
        candidate = random.choice(neighbors)

        candidate_error = objective_function(
            candidate, row_clues, column_clues
        )

        delta = candidate_error - current_error

        if delta < 0:
            current_grid = candidate
            current_error = candidate_error
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current_grid = candidate
                current_error = candidate_error

        if current_error < best_error:
            best_grid = copy.deepcopy(current_grid)
            best_error = current_error

        if convergence_history is not None:
            convergence_history.append(best_error)

        if best_error == 0:
            break

        temperature *= cooling_rate

    elapsed_time = time.time() - start_time

    return best_grid, best_error, iteration, elapsed_time