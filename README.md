Nonogram Optimization

A Python project exploring and comparing metaheuristic optimization algorithms for solving Nonogram puzzles.

The project implements four optimization approaches and provides tools for comparing their performance, analyzing convergence, and evaluating experimental results.

Overview

A Nonogram is a logic puzzle in which cells in a grid must be filled according to numerical clues describing consecutive groups of filled cells in each row and column.

This project approaches Nonogram solving as an optimization problem. Candidate solutions are represented as binary grids, and an objective function measures the differences between the blocks extracted from a candidate grid and the provided clues.

The goal is to minimize the objective function until a valid solution is found.

Implemented Algorithms

The project includes four metaheuristic algorithms:

Algorithm

Description

Classical Hill Climbing

Iteratively selects the best neighboring solution if it improves the objective value.

Randomized Hill Climbing

Randomly selects a neighboring solution and accepts it if it does not worsen the objective value.

Tabu Search

Uses a tabu list to avoid recently visited solutions and explores alternative search paths.

Simulated Annealing

Uses a temperature-based acceptance probability to occasionally accept worse solutions.

An exhaustive search implementation is also included for small problem instances.

Project Structure

MetaheurystykaNonogram/
├── data/
│   └── examples/
├── experiments/
│   └── benchmark.py
├── results/
│   ├── experiments/
│   │   ├── convergence_runs.csv
│   │   └── convergence_summary.csv
│   └── figures/
│       ├── convergence_iterations.png
│       └── convergence_normalized.png
├── src/
│   └── nonogram/
│       ├── algorithms/
│       │   ├── exhaustive_search.py
│       │   ├── hill_climbing.py
│       │   ├── tabu_search.py
│       │   └── simulated_annealing.py
│       ├── __init__.py
│       ├── comparison.py
│       ├── convergence.py
│       ├── main.py
│       ├── neighborhood.py
│       ├── objective.py
│       └── puzzle.py
├── tests/
├── .gitignore
├── pyproject.toml
└── README.md

Installation

Python 3.10 or newer is required.

Clone the repository:

git clone https://github.com/s29602-pj/MetaheurstykaNonogram.git
cd MetaheurstykaNonogram

Create and activate a virtual environment:

python -m venv .venv

On Windows:

.venv\Scripts\activate

Install the required dependencies:

python -m pip install numpy matplotlib pytest
python -m pip install -e .

Usage

Run the application:

python -m nonogram.main

The application accepts puzzle data interactively.

The input consists of four lines:

Grid width

Grid height

Column clues

Row clues

You can also provide an input file:

python -m nonogram.main --input data/examples/medium.txt

Selecting an Algorithm

Run all algorithms:

python -m nonogram.main --algorithm all

Run a specific algorithm:

python -m nonogram.main --algorithm hill-climbing

Available options:

all
exhaustive
hill-climbing
randomized-hill-climbing
tabu
simulated-annealing
convergence

Additional parameters are available:

python -m nonogram.main --algorithm tabu --max-iterations 1000 --tabu-size 30

For Simulated Annealing:

python -m nonogram.main --algorithm simulated-annealing --initial-temperature 100 --final-temperature 0.1 --cooling-rate 0.95

Note: Exhaustive search is computationally expensive and is intended for small puzzle instances.

Convergence Experiments

The project includes an experimental module for analyzing the convergence behavior of the four metaheuristic algorithms.

Run an experiment with 30 independent starting grids:

python -m nonogram.main --algorithm convergence --number-of-runs 30

Each run generates a new random starting grid. All four algorithms receive the same starting grid within a given run, allowing a more consistent comparison.

Two convergence plots are generated:

results/figures/convergence_iterations.png – objective function value versus the number of iterations.

results/figures/convergence_normalized.png – objective function value versus normalized progress.

Experimental results are exported to CSV:

results/experiments/convergence_runs.csv – individual run results.

results/experiments/convergence_summary.csv – aggregated statistics.

Experimental Results

The following results were obtained from 30 runs using different random starting grids for the same test puzzle.

Algorithm

Success Rate

Average Error

Average Time (s)

Classical Hill Climbing

0.00%

4.70

0.003438

Randomized Hill Climbing

26.67%

1.47

2.050979

Tabu Search

93.33%

0.13

0.048708

Simulated Annealing

0.00%

4.77

0.038610

Results Interpretation

Tabu Search achieved the highest success rate, solving 28 out of 30 runs.

Randomized Hill Climbing solved 8 out of 30 runs, but required substantially more iterations and execution time on average.

Classical Hill Climbing and Simulated Annealing did not find a complete solution in these experiments.

These results are specific to the tested puzzle and experimental configuration. They should not be interpreted as a general ranking of the algorithms across all Nonogram instances.

Testing

The project uses pytest for automated testing.

Run the test suite:

python -m pytest -v

The current test suite contains 41 tests covering the objective function, neighborhood generation, puzzle handling, optimization algorithms, and convergence utilities.

Technologies

Python

NumPy

Matplotlib

pytest

setuptools

Project Goals

The main goals of this project are:

Implementing different metaheuristic optimization algorithms.

Comparing their performance on Nonogram puzzles.

Analyzing convergence behavior.

Collecting and evaluating experimental results.

Practicing software modularity, testing, and documentation.

License

No license has been specified yet.