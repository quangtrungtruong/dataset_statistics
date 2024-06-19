from utils.util import *


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    for data in csv_data:
        if is_simple(data):
            data[COMPLEXITY] = "simple"
        elif is_medium(data):
            data[COMPLEXITY] = "medium"
        elif is_hard(data):
            data[COMPLEXITY] = "hard"
        else:
            raise ValueError("Unknown complexity")

    output_path = csv_file.replace(".csv", "_complexity.csv")
    print(f"Writing to {output_path}")
    write_csv(output_path, csv_data)

    pass


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
