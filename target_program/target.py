def run_target(data):

    print("Testing:", data)

    # Simulated vulnerabilities

    if len(data) > 10:
        raise Exception("Buffer Overflow Simulated")

    if "!!!" in data:
        raise Exception("Format String Vulnerability")

    if data.startswith("AAAA"):
        raise Exception("Stack Corruption")

    return "Program ran successfully"