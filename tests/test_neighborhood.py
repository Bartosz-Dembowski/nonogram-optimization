from nonogram.neighborhood import (
    generate_neighborhood,
    generate_random_grid,
)


def test_generate_neighborhood_size():
    grid = [
        [1, 2],
        [2, 1],
    ]

    neighbors = generate_neighborhood(grid)

    assert len(neighbors) == 4


def test_generate_neighborhood_flips_one_cell():
    grid = [
        [1, 2],
        [2, 1],
    ]

    neighbors = generate_neighborhood(grid)

    for neighbor in neighbors:
        differences = sum(
            grid[y][x] != neighbor[y][x]
            for y in range(2)
            for x in range(2)
        )

        assert differences == 1


def test_generate_neighborhood_does_not_modify_original():
    grid = [
        [1, 2],
        [2, 1],
    ]

    original = copy_grid = [row.copy() for row in grid]

    generate_neighborhood(grid)

    assert grid == original


def test_generate_random_grid_dimensions():
    grid = generate_random_grid(3, 4)

    assert len(grid) == 3
    assert all(len(row) == 4 for row in grid)


def test_generate_random_grid_values():
    grid = generate_random_grid(5, 5)

    assert all(
        cell in [1, 2]
        for row in grid
        for cell in row
    )