import json


def task() -> float:
    total = 0
    with open("input.json", "r") as file:
        data = json.load(file)
    for dict_ in data:
        total += dict_["score"] * dict_["weight"]
    return total


print(f"{task():.3f}")
