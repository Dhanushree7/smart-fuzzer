import os
import random
from collections import defaultdict
import matplotlib.pyplot as plt

from input_generator.generator import generate_input
from target_program.target import run_target

print("Smart Fuzzer Project Started")

# Create crashes folder
if not os.path.exists("crashes"):
    os.mkdir("crashes")

NUM_TESTS = 50

crash_count = 0
crash_inputs = []
crash_freq = defaultdict(int)
unique_crashes = set()

for i in range(NUM_TESTS):

    # Smart mutation strategy
    if crash_inputs and random.random() < 0.6:

        base = random.choice(crash_inputs)
        pos = random.randint(0, len(base) - 1)
        new_char = chr(random.randint(65, 90))

        data = base[:pos] + new_char + base[pos+1:]

    else:
        data = generate_input()

    try:
        result = run_target(data)
        print(result)

    except Exception as e:

        if data not in unique_crashes:

            unique_crashes.add(data)

            crash_count += 1
            crash_inputs.append(data)
            crash_freq[data] += 1

            filename = f"crashes/crash_{crash_count}.txt"

            with open(filename, "w") as f:
                f.write(f"Input: {data}\n")
                f.write(f"Error: {str(e)}\n")

            print(f"Unique crash detected! Saved to {filename}")

# Crash Summary
print("\n--- Crash Summary Report ---")
print("Total Tests Run:", NUM_TESTS)
print("Total Unique Crashes:", crash_count)

print("\nInputs that caused crashes:")
for i, inp in enumerate(crash_inputs, start=1):
    print(f"{i}. {inp}")

print("\nMost Frequent Crashes:")
for inp, freq in crash_freq.items():
    print(f"{inp} → {freq} time(s)")

# Visualization
if crash_freq:

    inputs = list(crash_freq.keys())
    counts = list(crash_freq.values())

    plt.figure(figsize=(10,5))
    plt.bar(inputs, counts)

    plt.xlabel("Crash Inputs")
    plt.ylabel("Frequency")
    plt.title("Smart Fuzzer Crash Analysis")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("crash_analysis.png")
    plt.close()

    print("\nCrash chart saved as crash_analysis.png")

print("\nFuzzing Completed Successfully")