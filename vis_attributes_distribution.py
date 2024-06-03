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

    for a, v in zip(attributes, counts):
        print(f"{a}: {v}")

    video_count = len(csv_data)
    percentage = [int(count / video_count * 100) for count in counts]

    # Creating the horizontal bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.barh(attributes, counts, color="skyblue")
    plt.xlabel("Count")
    plt.ylabel("Attribute")
    plt.title("Attribute Counts")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.subplots_adjust(left=0.3)  # Increase the left margin

    # Add text at the tip of each bar
    for bar, add_data in zip(bars, percentage):
        plt.text(
            bar.get_width() + 5,  # x-coordinate: bar's width + some offset
            bar.get_y()
            + bar.get_height()
            / 2,  # y-coordinate: bar's y position + half the bar's height
            f"{add_data}%",  # text to display
            va="center",
        )  # vertical alignment

    output_path = os.path.join(output_folder, "attributes_distribution.png")
    plt.savefig(output_path, bbox_inches="tight")


if __name__ == "__main__":
    csv_file = "./data/mvk_caption.csv"
    output_folder = "./figures"
    main(csv_file, output_folder)
