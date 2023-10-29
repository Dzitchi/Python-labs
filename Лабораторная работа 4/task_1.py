import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    sum_ = sum([n["score"] * n["weight"] for n in data])
    return round(sum_, 3)


print(task())
