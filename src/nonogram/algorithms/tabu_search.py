import copy
import time

from nonogram.neighborhood import generate_neighborhood
from nonogram.objective import objective_function


def tabu_search(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    max_iterations: int | None = None,
    tabu_size: int = 50,
    convergence_history: list[int] | None = None,
):
    """Run tabu search with a tabu list and history-based backtracking."""

    start_time = time.time()

    current_grid = copy.deepcopy(starting_grid)
    best_grid = copy.deepcopy(current_grid)

    best_error = objective_function(
        best_grid, row_clues, column_clues
    )

    if convergence_history is not None:
        convergence_history.append(best_error)

    tabu_list = [copy.deepcopy(current_grid)]
    history = [copy.deepcopy(current_grid)]

    iteration = 0

    while True:
        iteration += 1

        neighbors = generate_neighborhood(current_grid)

        admissible_neighbors = [
            neighbor for neighbor in neighbors
            if neighbor not in tabu_list
        ]

        if not admissible_neighbors:
            if len(history) > 1:
                current_grid = copy.deepcopy(history[-2])
                history = history[:-1]

                if convergence_history is not None:
                    convergence_history.append(best_error)

                continue
            else:
                break

        best_candidate = min(
            admissible_neighbors,
            key=lambda grid: objective_function(
                grid, row_clues, column_clues
            ),
        )

        candidate_error = objective_function(
            best_candidate, row_clues, column_clues
        )

        current_grid = best_candidate
        history.append(copy.deepcopy(current_grid))
        tabu_list.append(copy.deepcopy(current_grid))

        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        if candidate_error < best_error:
            best_grid = copy.deepcopy(best_candidate)
            best_error = candidate_error

        if convergence_history is not None:
            convergence_history.append(best_error)

        if best_error == 0:
            break

        if max_iterations is not None and iteration >= max_iterations:
            print("Algorithm stopped after reaching the iteration limit.")
            break

    elapsed_time = time.time() - start_time

    return best_grid, best_error, iteration, elapsed_time, history