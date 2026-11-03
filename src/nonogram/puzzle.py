def parse_clues(text: str) -> list[list[int]]:
    """Parse clues from their string representation."""
    return [
        list(map(int, section.split(',')))
        for section in text[1:-1].split('","')
    ]


def print_grid(grid: list[list[int]]) -> None:
    """Print the grid in a readable format."""
    for row in grid:
        print("".join("- *"[cell] for cell in row))