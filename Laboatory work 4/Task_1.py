import json


def task() -> float:
    total = 0
    with open("input.json", "r") as file:
        data = json.load(file)
    for dict_ in data:
        p = dict_["score"] * dict_["weight"]
        total += p
    return total


print(f"{task():.3f}")
