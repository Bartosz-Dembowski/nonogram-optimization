def compare_methods(results):
    """Compare optimization methods and print summary conclusions."""

    print("\nOptimization methods comparison\n")

    header = (
        f"{'Method':<30} {'Errors':<10} "
        f"{'Iterations':<10} {'Time [s]':<10}"
    )
    print(header)
    print("-" * len(header))

    for name, error, iterations, elapsed_time in results:
        print(
            f"{name:<30} {error:<10} "
            f"{iterations:<10} {elapsed_time:.4f}"
        )

    print("\nConclusions:")

    min_error = min(results, key=lambda item: item[1])[1]
    best_methods = [
        method for method in results
        if method[1] == min_error
    ]

    best_configuration = min(
        best_methods,
        key=lambda method: method[2] + method[3]
    )
    print(
        f"- Best configuration: {best_configuration[0]} "
        f"(Errors: {best_configuration[1]}, "
        f"Iterations: {best_configuration[2]}, "
        f"Time: {best_configuration[3]:.4f}s)"
    )

    fastest = min(best_methods, key=lambda method: method[3])
    print(
        f"- Fastest method (with {min_error} errors): "
        f"{fastest[0]} ({fastest[3]:.4f}s)"
    )

    least_resources = min(
        best_methods,
        key=lambda method: method[2] + method[3]
    )
    print(
        f"- Lowest resource usage with {min_error} errors: "
        f"{least_resources[0]} "
        f"(iterations + time: "
        f"{least_resources[2]} + {least_resources[3]:.4f})"
    )

    fastest_convergence = min(
        best_methods,
        key=lambda method: method[2]
    )
    print(
        f"- Fastest convergence: "
        f"{fastest_convergence[0]} "
        f"({fastest_convergence[2]} iterations)"
    )