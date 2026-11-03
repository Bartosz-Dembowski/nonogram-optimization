def extract_blocks(sequence: list[int]) -> list[int]:
    """Extract consecutive runs of filled cells from a row or column."""
    blocks = []
    current_length = 0

    for cell in sequence:
        if cell == 2:
            current_length += 1
        elif current_length > 0:
            blocks.append(current_length)
            current_length = 0

    if current_length > 0:
        blocks.append(current_length)

    return blocks


def compare_blocks(actual: list[int], expected: list[int]) -> int:
    """Count positional differences between actual and expected blocks."""
    max_length = max(len(actual), len(expected))
    errors = 0

    for index in range(max_length):
        actual_value = actual[index] if index < len(actual) else 0
        expected_value = expected[index] if index < len(expected) else 0

        if actual_value != expected_value:
            errors += 1

    return errors


def objective_function(
    grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
) -> int:
    """Calculate the total number of mismatches in rows and columns."""
    height = len(grid)
    width = len(grid[0])
    errors = 0

    for row_index in range(height):
        actual = extract_blocks(grid[row_index])
        expected = row_clues[row_index]
        errors += compare_blocks(actual, expected)

    for column_index in range(width):
        column = [grid[row][column_index] for row in range(height)]
        actual = extract_blocks(column)
        expected = column_clues[column_index]
        errors += compare_blocks(actual, expected)

    return errors