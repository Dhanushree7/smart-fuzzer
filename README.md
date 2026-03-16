# Smart Fuzzer 🔍

Smart Fuzzer is a Python-based fuzz testing framework designed to automatically generate inputs, mutate them, explore program behavior, detect crashes, and classify vulnerabilities.

This project demonstrates key fuzzing techniques used in modern security testing tools.

---

# 🚀 Features

- Random input generation
- Mutation-based fuzzing
- Coverage-guided fuzzing
- Seed corpus inputs
- Automated target program execution
- Crash detection
- Crash classification
- Crash grouping
- Vulnerability simulation
- Fuzzing summary reports

---

# 📂 Project Structure

```
smart-fuzzer
│
├── core
│   ├── crash_detector.py
│   ├── crash_classifier.py
│
├── corpus
│   └── seeds.txt
│
├── fuzzers
│   ├── mutation_fuzzer.py
│   └── coverage_fuzzer.py
│
├── input_generator
│   └── generator.py
│
├── target_program
│   └── target.py
│
├── crashes
│
└── main.py
```

---

# ⚙️ How Smart Fuzzer Works

1️⃣ The fuzzer generates inputs using random generation or mutation.

2️⃣ Seed inputs are mutated to explore nearby input variations.

3️⃣ The target program is executed with these inputs.

4️⃣ Coverage-guided fuzzing checks if new code paths are discovered.

5️⃣ If the program crashes, the crash is detected.

6️⃣ Crashes are classified and stored in the crashes folder.

---

# ▶️ Running the Fuzzer

Run the Smart Fuzzer with:

```
python main.py
```

Example output:

```
Smart Fuzzer Project Started
Testing: AAAAAAAAA
New code path discovered!
Program ran successfully

Testing: H%LLO
Unique crash detected!
Crash grouped under exception_format_string_vulnerability_simulated.txt
```

---

# 🧪 Simulated Vulnerabilities

The target program simulates different vulnerabilities for testing:

| Vulnerability | Trigger |
|------|------|
Buffer Overflow | Input length > 10 |
Integer Overflow | Large numeric input |
Format String | `%` character |
SQL Injection | `'` or `--` patterns |

---

# 📊 Example Results

```
Total Tests Run: 50
Total Unique Crashes: 11
```

Crash reports are stored in:

```
crashes/
```

Example crash files:

```
exception_buffer_overflow_simulated.txt
exception_integer_overflow_simulated.txt
exception_format_string_vulnerability_simulated.txt
```

---

# 🧠 Advanced Fuzzing Techniques Used

### Mutation-based fuzzing
Inputs are mutated from seed values to explore nearby variations.

Example:

```
HELLO
HELLhO
H%LLO
```

---

### Coverage-guided fuzzing
The fuzzer detects when new code paths are executed and prioritizes those inputs.

Example:

```
New code path discovered!
```

---

# 🛠 Tech Stack

- Python
- Coverage.py
- Git
- GitHub

---

# 🔮 Future Improvements

Planned upgrades:

- Parallel fuzzing
- Corpus evolution
- Crash deduplication
- Web dashboard for fuzzing results

---

# 👨‍💻 Author

Dhanushree
