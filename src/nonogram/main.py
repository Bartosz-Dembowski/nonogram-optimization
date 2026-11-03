
import argparse
import sys

from nonogram.puzzle import parse_clues, print_grid
from nonogram.comparison import compare_methods
from nonogram.convergence import generate_convergence_plot
from nonogram.algorithms.exhaustive_search import exhaustive_search
from nonogram.algorithms.hill_climbing import (
    hill_climbing,
    randomized_hill_climbing,
)
from nonogram.algorithms.tabu_search import tabu_search
from nonogram.algorithms.simulated_annealing import simulated_annealing
from nonogram.neighborhood import generate_random_grid


def read_puzzle(input_path=None):
    """Read puzzle data from a file or standard input."""

    if input_path:
        with open(input_path, "r", encoding="utf-8") as file:
            data = file.read().strip().splitlines()
    else:
        print("\nEnter puzzle data:")

        data = [
            input("Width: "),
            input("Height: "),
            input("Column clues: "),
            input("Row clues: "),
        ]

    if len(data) != 4:
        raise ValueError(
            f"Expected exactly 4 lines of input, received {len(data)}."
        )

    width = int(data[0])
    height = int(data[1])
    column_clues = parse_clues(data[2])
    row_clues = parse_clues(data[3])

    return width, height, row_clues, column_clues


def display_result(name, grid, error, iterations, elapsed_time):
    """Display the result of one optimization algorithm."""

    print(f"\n{name}")
    print("-" * len(name))

    print_grid(grid)

    print(f"Errors: {error}")
    print(f"Iterations: {iterations}")
    print(f"Execution time: {elapsed_time:.4f} seconds")


def run_algorithm(
    algorithm,
    starting_grid,
    height,
    width,
    row_clues,
    column_clues,
    args,
):
    """Run one selected optimization algorithm."""

    if algorithm == "exhaustive":
        result = exhaustive_search(
            height, width, row_clues, column_clues
        )

        if result is None:
            print("\nNo solution found.")
            return None

        grid, error, elapsed_time, iterations = result

    elif algorithm == "hill-climbing":
        grid, error, iterations, elapsed_time = hill_climbing(
            starting_grid,
            row_clues,
            column_clues,
            max_iterations=args.max_iterations,
        )

    elif algorithm == "randomized-hill-climbing":
        grid, error, iterations, elapsed_time = randomized_hill_climbing(
            starting_grid,
            row_clues,
            column_clues,
            max_iterations=args.max_iterations,
        )

    elif algorithm == "tabu":
        grid, error, iterations, elapsed_time, history = tabu_search(
            starting_grid,
            row_clues,
            column_clues,
            max_iterations=args.max_iterations,
            tabu_size=args.tabu_size,
        )

        if len(history) > 1:
            print("\nPrevious solution (one step back):")
            print_grid(history[-2])

    elif algorithm == "simulated-annealing":
        grid, error, iterations, elapsed_time = simulated_annealing(
            starting_grid,
            row_clues,
            column_clues,
            initial_temperature=args.initial_temperature,
            final_temperature=args.final_temperature,
            cooling_rate=args.cooling_rate,
        )

    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    display_result(
        algorithm,
        grid,
        error,
        iterations,
        elapsed_time,
    )

    return grid, error, iterations, elapsed_time


def run_all(
    starting_grid,
    height,
    width,
    row_clues,
    column_clues,
    args,
):
    """Run all optimization algorithms and compare their results."""

    algorithms = [
        "exhaustive",
        "hill-climbing",
        "randomized-hill-climbing",
        "tabu",
        "simulated-annealing",
    ]

    results = []

    for algorithm in algorithms:
        print(f"\nRunning {algorithm}...")

        result = run_algorithm(
            algorithm,
            starting_grid,
            height,
            width,
            row_clues,
            column_clues,
            args,
        )

        if result is not None:
            grid, error, iterations, elapsed_time = result
            results.append(
                (algorithm, error, iterations, elapsed_time)
            )

    if results:
        compare_methods(results)
    else:
        print("\nNo algorithm returned a result.")


def create_parser():
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description="Nonogram optimization algorithms."
    )

    parser.add_argument(
        "--input",
        type=str,
        help="Path to the puzzle input file. Reads from stdin if omitted.",
    )

    parser.add_argument(
        "--algorithm",
        choices=[
            "all",
            "exhaustive",
            "hill-climbing",
            "randomized-hill-climbing",
            "tabu",
            "simulated-annealing",
            "convergence",
        ],
        default="all",
        help="Optimization algorithm to run.",
    )

    parser.add_argument(
        "--max-iterations",
        type=int,
        default=1000,
        help="Maximum number of iterations.",
    )

    parser.add_argument(
        "--tabu-size",
        type=int,
        default=30,
        help="Maximum size of the tabu list.",
    )

    parser.add_argument(
        "--initial-temperature",
        type=float,
        default=100.0,
        help="Initial temperature for simulated annealing.",
    )

    parser.add_argument(
        "--final-temperature",
        type=float,
        default=0.1,
        help="Final temperature for simulated annealing.",
    )

    parser.add_argument(
        "--cooling-rate",
        type=float,
        default=0.95,
        help="Cooling rate for simulated annealing.",
    )

    parser.add_argument(
        "--number-of-runs",
        type=int,
        default=10,
        help="Number of runs for convergence experiments.",
    )

    return parser


def main():
    """Run the Nonogram optimization application."""

    parser = create_parser()
    args = parser.parse_args()

    if args.number_of_runs < 1:
        parser.error("--number-of-runs must be at least 1.")

    try:
        width, height, row_clues, column_clues = read_puzzle(args.input)
    except (OSError, ValueError) as error:
        print(f"Input error: {error}")
        return

    starting_grid = generate_random_grid(height, width)

    print("\nStarting grid:")
    print_grid(starting_grid)

    if args.algorithm == "convergence":
        print("\nGenerating convergence curves...")

        generate_convergence_plot(
            starting_grid,
            row_clues,
            column_clues,
            number_of_runs=args.number_of_runs,
        )

        print("\nConvergence plot saved to:")
        print("results/figures/convergence.png")

    elif args.algorithm == "all":
        run_all(
            starting_grid,
            height,
            width,
            row_clues,
            column_clues,
            args,
        )

    else:
        run_algorithm(
            args.algorithm,
            starting_grid,
            height,
            width,
            row_clues,
            column_clues,
            args,
        )


if __name__ == "__main__":
    main()
