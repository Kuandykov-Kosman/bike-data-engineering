import subprocess


def run_step(name, command):
    print(f"\n--- {name} ---")

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"{name} failed!")
        exit(1)

    print(f"{name} completed!")


if __name__ == "__main__":

    run_step(
        "Validation",
        ["python", "src/validate.py"]
    )

    run_step(
        "ETL",
        ["python", "-m", "src.load"]
    )

    run_step(
        "Database",
        ["python", "-m", "src.database"]
    )

    run_step(
        "Visualization",
        ["python", "-m", "src.visualize"]
    )

    print("\nPipeline completed successfully!")
