import subprocess
from input_generator.generator import generate_input
from core.crash_detector import detect_crash

TOTAL_TESTS = 50

print("Smart Fuzzer Project Started")

crash_inputs = []

for i in range(TOTAL_TESTS):

    payload = generate_input()

    print(f"Testing: {payload}")

    try:
        result = subprocess.run(
            ["python", "target_program/target.py"],
            input=payload,
            text=True,
            capture_output=True
        )

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