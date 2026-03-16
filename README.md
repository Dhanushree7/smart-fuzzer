# Smart Fuzzer 🔍

Smart Fuzzer is a Python-based fuzz testing framework designed to automatically generate inputs, test target programs, detect crashes, and classify vulnerabilities.

Fuzzing is a widely used technique in security testing used by tools like AFL, libFuzzer, and OSS-Fuzz.

---

## 🚀 Features

- Random input generation
- Automated fuzz testing
- Target program execution
- Crash detection
- Crash classification
- Crash grouping
- Vulnerability simulation
- Fuzzing summary report

---

## 📂 Project Structure

smart-fuzzer-project

core  
  crash_detector.py  
  crash_classifier.py  

input_generator  
  generator.py  

target_program  
  target.py  

crashes  
  crash reports  

payloads  

fuzzers  

corpus  

coverage_report  

main.py

---

## ⚙️ How It Works

1. The fuzzer generates random inputs.
2. Inputs are passed to the target program.
3. The target program processes the input.
4. If the program crashes, the fuzzer detects it.
5. The crash is classified and saved in the crashes folder.

---

## ▶️ Running the Fuzzer

Run the program using:

python main.py

Example output:

Smart Fuzzer Project Started  
Testing: PnscazLTsoT  
Unique crash detected!  
Crash grouped under buffer_overflow_simulated.txt

---

## 🧪 Simulated Vulnerabilities

The target program simulates several vulnerabilities:

- Buffer Overflow
- Crash Pattern Detection
- Integer Overflow
- Format String Vulnerability
- SQL Injection Pattern

---

## 📊 Example Results

Total Tests Run: 50  
Total Unique Crashes: 15  

Detected crashes are stored in:

crashes/
buffer_overflow_simulated.txt

---

## 🔮 Future Improvements

Planned upgrades:

- Mutation-based fuzzing
- Coverage-guided fuzzing
- API fuzzing
- AI-assisted input generation
- Web dashboard for results

---

## 🛠 Tech Stack

Python  
Git  
GitHub  

---

## 👨‍💻 Author

Dhanushree

