from utils.util import *

import os
import matplotlib.pyplot as plt


def main(csv_file: str, output_folder: str):

    csv_data = read_csv(csv_file)

    os.makedirs(output_folder, exist_ok=True)

    attributes_count = {}
    for attribute in ATTRIBUTES:
        attributes_count[attribute] = 0

    for data in csv_data:
        for attribute in ATTRIBUTES:
            if data[attribute] != "":
                attributes_count[attribute] += 1

    attributes = list(attributes_count.keys())
    counts = list(attributes_count.values())

    # Creating the horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(attributes, counts, color="skyblue")
    plt.xlabel("Count")
    plt.ylabel("Attribute")
    plt.title("Horizontal Bar Chart of Attribute Counts")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    output_path = os.path.join(output_folder, "attributes_distribution.png")
    plt.savefig(output_path)


if __name__ == "__main__":
    csv_file = "./data/mvk_caption.csv"
    output_folder = "./figures"
    main(csv_file, output_folder)
