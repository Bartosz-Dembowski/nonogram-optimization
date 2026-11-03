# Nonogram Optimization

A Python-based project exploring metaheuristic optimization algorithms for solving Nonogram puzzles.

The project implements and compares several optimization approaches, evaluating their performance in terms of solution quality, execution time, and convergence behavior.

## Overview

Nonograms are logic puzzles in which cells in a grid must be filled according to numerical clues provided for each row and column.

This project approaches Nonogram solving as an optimization problem. Candidate solutions are represented as grids, and an objective function measures the difference between the blocks in a candidate grid and the required clues.

The main goal is to investigate how different optimization algorithms perform when searching for valid Nonogram solutions.

## Implemented Algorithms

The project includes the following algorithms:

- **Exhaustive Search** – explores all possible grid configurations to find a valid solution.
- **Hill Climbing** – iteratively selects the best neighboring solution.
- **Randomized Hill Climbing** – explores randomly selected neighboring solutions.
- **Tabu Search** – uses a tabu list to avoid revisiting previously explored solutions.
- **Simulated Annealing** – uses a probabilistic acceptance mechanism to escape local optima.

## Project Structure

```text
nonogram-optimization/
│
├── data/
│   └── examples/
│       ├── small.txt
│       └── medium.txt
│
├── experiments/
│   └── benchmark.py
│
├── results/
│   ├── experiments/
│   │   ├── convergence_runs.csv
│   │   └── convergence_summary.csv
│   │
│   └── figures/
│       ├── convergence_iterations.png
│       ├── convergence_normalized.png
│       └── ...
│
├── src/
│   └── nonogram/
│       ├── algorithms/
│       │   ├── exhaustive_search.py
│       │   ├── hill_climbing.py
│       │   ├── tabu_search.py
│       │   └── simulated_annealing.py
│       │
│       ├── __init__.py
│       ├── main.py
│       ├── puzzle.py
│       ├── objective.py
│       ├── neighborhood.py
│       ├── comparison.py
│       └── convergence.py
│
├── tests/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Technologies

- Python 3.13
- NumPy
- Matplotlib
- pytest
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/Bartosz-Dembowski/nonogram-optimization.git
cd nonogram-optimization
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Running the Project

The application can be launched through the main module:

```bash
python -m nonogram.main
```

To use a predefined puzzle, provide an input file:

```bash
python -m nonogram.main --input data/examples/small.txt
```

The application supports the following algorithm selection options:

- `all`
- `exhaustive`
- `hill-climbing`
- `randomized-hill-climbing`
- `tabu`
- `simulated-annealing`
- `convergence`

For convergence experiments, the number of runs can be specified using:

```bash
python -m nonogram.main --algorithm convergence --number-of-runs 30
```

## Experiments and Results

The project includes experiments comparing the convergence behavior and performance of the implemented algorithms.

The benchmark evaluated all four metaheuristic algorithms using 30 independent runs. Each run used a different randomly generated starting grid, shared by all algorithms within that run.

### Benchmark Results

| Algorithm | Success Rate | Average Error | Average Iterations | Average Execution Time |
|---|---:|---:|---:|---:|
| Classical Hill Climbing | 0.00% | 4.70 | 6.73 | 0.0034 s |
| Randomized Hill Climbing | 26.67% | 1.47 | 7,417.27 | 2.0510 s |
| Tabu Search | **93.33%** | **0.13** | 92.10 | 0.0487 s |
| Simulated Annealing | 0.00% | 4.77 | 135.00 | 0.0386 s |

### Key Findings

- Tabu Search achieved the highest success rate, solving 28 out of 30 runs.
- Randomized Hill Climbing solved 8 out of 30 runs but required significantly more iterations and execution time.
- Classical Hill Climbing frequently became trapped in local optima.
- Simulated Annealing did not find a valid solution in the tested configuration.

**Conclusion:** Tabu Search achieved the best overall performance in the tested experimental configuration.

These results are specific to one puzzle instance and the selected algorithm parameters. They should not be interpreted as a general ranking across all Nonogram puzzles.

### Convergence Visualization

The project generates convergence plots to compare how the algorithms improve their solutions over time.

Generated figures are stored in `results/figures/`.

## Running Tests

Run the test suite using:

```bash
python -m pytest -v
```

The project includes unit tests covering the objective function, puzzle handling, neighborhood generation, optimization algorithms, and convergence functionality.

## Project Background

This project was originally developed as part of a university coursework assignment.

After completing the academic project, I continued working on it independently, focusing on code refactoring, improving project structure, introducing modular architecture, expanding automated tests, and preparing the codebase for further development.

The current repository represents a reorganized and improved version of the original academic project.

## License

No license has been specified for this project yet.
