import random
import string
import os

CRASH_FOLDER = "../crashes"  # relative to input_generator

def load_crash_inputs():
    """Load past crash inputs"""
    inputs = []
    if os.path.exists(CRASH_FOLDER):
        for filename in os.listdir(CRASH_FOLDER):
            filepath = os.path.join(CRASH_FOLDER, filename)
            with open(filepath, "r") as f:
                line = f.readline()
                if line.startswith("Input:"):
                    inputs.append(line.strip().split("Input: ")[1])
    return inputs

def generate_input():
    """Generate new input intelligently"""
    past_crashes = load_crash_inputs()
    
    if past_crashes and random.random() < 0.7:
        # 70% chance to mutate a past crash input
        base = random.choice(past_crashes)
        return mutate_input(base)
    else:
        # 30% chance to generate fully random input
        length = random.randint(3,12)
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def mutate_input(base):
    """Slightly change a past crash input"""
    chars = list(base)
    for _ in range(random.randint(1, 3)):
        idx = random.randint(0, len(chars)-1)
        chars[idx] = random.choice(string.ascii_letters)
    return ''.join(chars)

if __name__ == "__main__":
    print(generate_input())