import itertools
import time

from nonogram.objective import objective_function


def exhaustive_search(
    height: int,
    width: int,
    row_clues: list[list[int]],
    column_clues: list[list[int]],
):
    """Search all possible grids until a valid solution is found."""

    start_time = time.time()
    counter = 0

    for combination in itertools.product([1, 2], repeat=height * width):
        counter += 1

        grid = [
            list(combination[y * width:(y + 1) * width])
            for y in range(height)
        ]

        errors = objective_function(grid, row_clues, column_clues)

        if errors == 0:
            elapsed_time = time.time() - start_time
            return grid, errors, elapsed_time, counter
