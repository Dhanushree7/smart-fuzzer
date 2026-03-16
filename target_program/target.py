import sys

# Read fuzzed input
data = sys.stdin.read().strip()

# Simulated vulnerabilities for fuzz testing

# 1️⃣ Buffer overflow simulation
if len(data) > 10:
    raise Exception("Buffer Overflow Simulated")

# 2️⃣ Special pattern crash
if "CRASH" in data:
    raise Exception("Crash Pattern Detected")

# 3️⃣ Numeric overflow simulation
if data.isdigit() and int(data) > 100000:
    raise Exception("Integer Overflow Simulated")

# 4️⃣ Format string issue simulation
if "%" in data:
    raise Exception("Format String Vulnerability Simulated")

# 5️⃣ SQL injection pattern simulation
if "'" in data or "--" in data:
    raise Exception("SQL Injection Pattern Detected")

# If none of the conditions trigger
print("Program ran successfully")