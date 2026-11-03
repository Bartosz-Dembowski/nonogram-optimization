
import copy
import csv
import os
import random
import time
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np

from nonogram.neighborhood import (
    generate_neighborhood,
    generate_random_grid,
)
from nonogram.objective import objective_function
from nonogram.algorithms.tabu_search import tabu_search
from nonogram.algorithms.simulated_annealing import simulated_annealing


def classical_hill_climbing_curve(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    max_iterations: int = 500,
) -> list[int]:
    """Collect the convergence curve of classical hill climbing."""

    current_grid = copy.deepcopy(starting_grid)
    current_error = objective_function(
        current_grid, row_clues, column_clues
    )

    curve = [current_error]

    for _ in range(max_iterations):
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

        improved = best_error < current_error

        if improved:
            current_grid = best_neighbor
            current_error = best_error

        curve.append(current_error)

        if current_error == 0 or not improved:
            break

    return curve


def randomized_hill_climbing_curve(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    max_iterations: int = 10000,
) -> list[int]:
    """Collect the convergence curve of randomized hill climbing."""

    current_grid = copy.deepcopy(starting_grid)
    current_error = objective_function(
        current_grid, row_clues, column_clues
    )

    curve = [current_error]

    for _ in range(max_iterations):
        neighbors = generate_neighborhood(current_grid)
        random_neighbor = random.choice(neighbors)

        random_error = objective_function(
            random_neighbor, row_clues, column_clues
        )

        if random_error <= current_error:
            current_grid = random_neighbor
            current_error = random_error

        curve.append(current_error)

        if current_error == 0:
            break

    return curve


def calculate_average_curve(
    curves: list[list[int]],
) -> list[float]:
    """Calculate the average convergence curve."""

    if not curves:
        raise ValueError("At least one convergence curve is required.")

    if any(not curve for curve in curves):
        raise ValueError("Convergence curves cannot be empty.")

    max_length = max(len(curve) for curve in curves)

    padded_curves = [
        curve + [curve[-1]] * (max_length - len(curve))
        for curve in curves
    ]

    return list(np.mean(padded_curves, axis=0))


def normalize_curve(
    curve: list[float],
    number_of_points: int = 101,
) -> list[float]:
    """Resample a convergence curve to normalized progress."""

    if not curve:
        raise ValueError("Convergence curve cannot be empty.")

    if len(curve) == 1:
        return [curve[0]] * number_of_points

    original_positions = np.linspace(0, 1, len(curve))
    normalized_positions = np.linspace(0, 1, number_of_points)

    return list(
        np.interp(
            normalized_positions,
            original_positions,
            curve,
        )
    )


def save_experiment_results(
    run_results: dict[str, list[dict]],
) -> None:
    """Save individual experiment results and summary statistics to CSV."""

    output_directory = "results/experiments"
    os.makedirs(output_directory, exist_ok=True)

    # Save individual run results
    run_file = os.path.join(
        output_directory,
        "convergence_runs.csv",
    )

    run_fields = [
        "algorithm",
        "run",
        "final_error",
        "iterations",
        "execution_time_seconds",
        "success",
    ]

    with open(run_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=run_fields)
        writer.writeheader()

        for algorithm, results in run_results.items():
            for result in results:
                writer.writerow({
                    "algorithm": algorithm,
                    **result,
                })

    # Calculate summary statistics
    summary_file = os.path.join(
        output_directory,
        "convergence_summary.csv",
    )

    summary_fields = [
        "algorithm",
        "number_of_runs",
        "success_rate_percent",
        "average_error",
        "best_error",
        "worst_error",
        "average_iterations",
        "average_execution_time_seconds",
    ]

    with open(summary_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=summary_fields)
        writer.writeheader()

        for algorithm, results in run_results.items():
            errors = [
                result["final_error"] for result in results
            ]

            iterations = [
                result["iterations"] for result in results
            ]

            execution_times = [
                result["execution_time_seconds"]
                for result in results
            ]

            successful_runs = sum(
                result["success"] for result in results
            )

            writer.writerow({
                "algorithm": algorithm,
                "number_of_runs": len(results),
                "success_rate_percent": round(
                    successful_runs / len(results) * 100, 2
                ),
                "average_error": round(mean(errors), 4),
                "best_error": min(errors),
                "worst_error": max(errors),
                "average_iterations": round(mean(iterations), 2),
                "average_execution_time_seconds": round(
                    mean(execution_times), 6
                ),
            })

    print("\nExperiment results saved:")
    print(run_file)
    print(summary_file)



def generate_convergence_plot(
    starting_grid: list[list[int]],
    row_clues: list[list[int]],
    column_clues: list[list[int]],
    number_of_runs: int = 10,
) -> None:
    """Generate convergence plots and experiment statistics."""

    if number_of_runs < 1:
        raise ValueError("Number of runs must be at least 1.")

    convergence_curves = {
        "Classical Hill Climbing": [],
        "Randomized Hill Climbing": [],
        "Tabu Search": [],
        "Simulated Annealing": [],
    }

    run_results = {
        name: []
        for name in convergence_curves
    }

    height = len(starting_grid)
    width = len(starting_grid[0])

    for run in range(number_of_runs):
        print(f"\nConvergence experiment: {run + 1}/{number_of_runs}")

        # Generate one new starting grid for this experiment.
        # All four algorithms use the same grid in this run.
        run_starting_grid = generate_random_grid(height, width)

        # Classical Hill Climbing
        start_time = time.perf_counter()

        classical_curve = classical_hill_climbing_curve(
            run_starting_grid,
            row_clues,
            column_clues,
        )

        elapsed_time = time.perf_counter() - start_time

        convergence_curves["Classical Hill Climbing"].append(
            classical_curve
        )

        run_results["Classical Hill Climbing"].append({
            "run": run + 1,
            "final_error": classical_curve[-1],
            "iterations": len(classical_curve) - 1,
            "execution_time_seconds": round(elapsed_time, 6),
            "success": classical_curve[-1] == 0,
        })

        # Randomized Hill Climbing
        start_time = time.perf_counter()

        randomized_curve = randomized_hill_climbing_curve(
            run_starting_grid,
            row_clues,
            column_clues,
        )

        elapsed_time = time.perf_counter() - start_time

        convergence_curves["Randomized Hill Climbing"].append(
            randomized_curve
        )

        run_results["Randomized Hill Climbing"].append({
            "run": run + 1,
            "final_error": randomized_curve[-1],
            "iterations": len(randomized_curve) - 1,
            "execution_time_seconds": round(elapsed_time, 6),
            "success": randomized_curve[-1] == 0,
        })

        # Tabu Search
        tabu_curve = []

        start_time = time.perf_counter()

        _, tabu_error, tabu_iterations, _, _ = tabu_search(
            run_starting_grid,
            row_clues,
            column_clues,
            max_iterations=1000,
            tabu_size=50,
            convergence_history=tabu_curve,
        )

        elapsed_time = time.perf_counter() - start_time

        convergence_curves["Tabu Search"].append(tabu_curve)

        run_results["Tabu Search"].append({
            "run": run + 1,
            "final_error": tabu_error,
            "iterations": tabu_iterations,
            "execution_time_seconds": round(elapsed_time, 6),
            "success": tabu_error == 0,
        })

        # Simulated Annealing
        annealing_curve = []

        start_time = time.perf_counter()

        _, annealing_error, annealing_iterations, _ = (
            simulated_annealing(
                run_starting_grid,
                row_clues,
                column_clues,
                convergence_history=annealing_curve,
            )
        )

        elapsed_time = time.perf_counter() - start_time

        convergence_curves["Simulated Annealing"].append(
            annealing_curve
        )

        run_results["Simulated Annealing"].append({
            "run": run + 1,
            "final_error": annealing_error,
            "iterations": annealing_iterations,
            "execution_time_seconds": round(elapsed_time, 6),
            "success": annealing_error == 0,
        })

    # Save experiment results
    save_experiment_results(run_results)

    # Calculate average convergence curves
    average_curves = {
        name: calculate_average_curve(curves)
        for name, curves in convergence_curves.items()
    }

    os.makedirs("results/figures", exist_ok=True)

    # Plot 1: Convergence versus actual iterations
    plt.figure(figsize=(12, 7))

    for name, curve in average_curves.items():
        plt.plot(curve, label=name)

    plt.xscale("symlog", linthresh=10)
    plt.xlabel("Iteration")
    plt.ylabel("Best objective function value (number of errors)")
    plt.title(
        f"Average convergence versus iterations ({number_of_runs} runs)"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("results/figures/convergence_iterations.png")
    plt.show()
    plt.close()

    # Plot 2: Convergence versus normalized progress
    normalized_average_curves = {
        name: calculate_average_curve(
            [
                normalize_curve(curve)
                for curve in curves
            ]
        )
        for name, curves in convergence_curves.items()
    }

    plt.figure(figsize=(12, 7))

    for name, curve in normalized_average_curves.items():
        plt.plot(
            np.linspace(0, 100, len(curve)),
            curve,
            label=name,
        )

    plt.xlabel("Normalized progress (%)")
    plt.ylabel("Best objective function value (number of errors)")
    plt.title(
        f"Average normalized convergence ({number_of_runs} runs)"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("results/figures/convergence_normalized.png")
    plt.show()
    plt.close()

