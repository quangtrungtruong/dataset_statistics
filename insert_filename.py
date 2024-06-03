from utils.util import *


def main(csv_file: str, starting_idx: int):

    csv_data = read_csv(csv_file)

    for idx, data in enumerate(csv_data):
        # Filename should be the idx in 8 digits
        output_idx = starting_idx + idx
        new_filename = f"{output_idx:08}.mp4"

        data["Filename"] = new_filename

    output_file = csv_file.replace(".csv", "_new.csv")
    print(f"Writing to {output_file}")
    write_csv(output_file, csv_data)
    pass


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    starting_idx = 9282
    main(csv_file, starting_idx)
