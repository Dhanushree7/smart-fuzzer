import random

def mutate(data):

    if not data:
        return data

    mutation_type = random.choice([
        "flip_char",
        "insert_char",
        "delete_char"
    ])

    data = list(data)

    if mutation_type == "flip_char":
        pos = random.randint(0, len(data)-1)
        data[pos] = chr(random.randint(32,126))

    elif mutation_type == "insert_char":
        pos = random.randint(0, len(data))
        data.insert(pos, chr(random.randint(32,126)))

    elif mutation_type == "delete_char":
        if len(data) > 1:
            pos = random.randint(0, len(data)-1)
            data.pop(pos)

    return "".join(data)