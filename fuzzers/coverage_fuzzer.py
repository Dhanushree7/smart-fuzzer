import subprocess
import json
import os

# stores all previously seen executed lines
coverage_seen = set()


def run_with_coverage(payload):

    # run target program with coverage tracking
    result = subprocess.run(
        ["coverage", "run", "--parallel-mode", "target_program/target.py"],
        input=payload,
        text=True,
        capture_output=True
    )

    # generate coverage report in JSON format
    subprocess.run(["coverage", "json", "-o", "coverage.json"], capture_output=True)

    if not os.path.exists("coverage.json"):
        return False

    with open("coverage.json") as f:
        data = json.load(f)

    files = data.get("files", {})

    new_path = False

    for file in files:
        executed_lines = files[file]["executed_lines"]

        for line in executed_lines:
            if line not in coverage_seen:
                coverage_seen.add(line)
                new_path = True

    return new_path