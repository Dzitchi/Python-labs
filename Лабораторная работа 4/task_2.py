import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as inp_f:
        reader = csv.DictReader(inp_f)
        data = list(reader)
    with open(OUTPUT_FILENAME, 'w') as out_f:
        json.dump(data, out_f, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
