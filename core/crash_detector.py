from core.crash_classifier import save_grouped_crash

crash_count = 0
unique_crashes = set()


def detect_crash(payload, error_message):
    global crash_count

    if error_message is None:
        print("Program ran successfully")
        return False

    crash_signature = payload + error_message

    if crash_signature not in unique_crashes:
        unique_crashes.add(crash_signature)
        crash_count += 1

        print("Unique crash detected!")

        # Group crash by error type
        save_grouped_crash(error_message, payload)

        return True

    else:
        print("Duplicate crash detected")

    return False