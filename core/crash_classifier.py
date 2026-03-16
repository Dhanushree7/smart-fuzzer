import os

def save_grouped_crash(error_message, input_data):

    # Extract only the last line of the error
    error_type = error_message.strip().split("\n")[-1]

    # Clean filename
    filename = error_type.lower().replace(" ", "_").replace(":", "") + ".txt"

    filepath = os.path.join("crashes", filename)

    os.makedirs("crashes", exist_ok=True)

    with open(filepath, "a") as f:
        f.write(input_data + "\n")

    print(f"Crash grouped under {filename}")