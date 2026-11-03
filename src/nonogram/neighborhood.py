import copy
import random


def generate_neighborhood(grid: list[list[int]]) -> list[list[list[int]]]:
    """Generate all neighbors by flipping one cell at a time."""
    height = len(grid)
    width = len(grid[0])
    neighbors = []

    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1 or grid[y][x] == 2:
                new_grid = copy.deepcopy(grid)

                if new_grid[y][x] == 1:
                    new_grid[y][x] = 2
                elif new_grid[y][x] == 2:
                    new_grid[y][x] = 1

                neighbors.append(new_grid)

    return neighbors


def generate_random_grid(height: int, width: int) -> list[list[int]]:
    """Generate a random grid with the specified dimensions."""
    return [
        [random.choice([1, 2]) for _ in range(width)]
        for _ in range(height)
    ]