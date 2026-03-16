import subprocess
import random

from input_generator.generator import generate_input
from fuzzers.mutation_fuzzer import mutate
from fuzzers.coverage_fuzzer import run_with_coverage
from core.crash_detector import detect_crash

TOTAL_TESTS = 50

print("Smart Fuzzer Project Started")

# Load seed inputs
with open("corpus/seeds.txt") as f:
    seeds = [line.strip() for line in f if line.strip()]

crash_inputs = []

for i in range(TOTAL_TESTS):

    # Choose mutation fuzzing or random fuzzing
    if random.random() < 0.6:
        base = random.choice(seeds)
        payload = mutate(base)
    else:
        payload = generate_input()

    print(f"Testing: {payload}")

    try:
        # run coverage-guided execution
        new_path = run_with_coverage(payload)

        if new_path:
            print("New code path discovered!")

        # run target program
        result = subprocess.run(
            ["python", "target_program/target.py"],
            input=payload,
            text=True,
            capture_output=True
        )

        # check crash
        if result.returncode != 0:

            error_message = result.stderr.strip()

            crashed = detect_crash(payload, error_message)

            if crashed:
                crash_inputs.append(payload)

        else:
            print("Program ran successfully")

    except Exception as e:
        print("Execution failed:", e)


print("\n--- Crash Summary Report ---")

print(f"Total Tests Run: {TOTAL_TESTS}")
print(f"Total Unique Crashes: {len(crash_inputs)}")

print("\nInputs that caused crashes:")

for i, crash in enumerate(crash_inputs, 1):
    print(f"{i}. {crash}")

print("\nFuzzing Completed Successfully")