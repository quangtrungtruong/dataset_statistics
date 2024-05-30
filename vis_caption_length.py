from utils.util import *

import os
import matplotlib.pyplot as plt


def main(csv_file: str, output_folder: str):

    os.makedirs(output_folder, exist_ok=True)

    csv_data = read_csv(csv_file)

    caption_lengths = []
    for data in csv_data:
        caption = data[CAPTION]
        caption_lengths.append(len(caption.split()))

    plt.boxplot(caption_lengths, vert=False)
    plt.xlabel("Caption Length")
    plt.yticks([])
    plt.grid(axis="x", linestyle="--", linewidth=0.7)
    # Remove the outer border lines
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.3, bottom=0.1)

    vis_path = os.path.join(output_folder, "caption_length_distribution.png")
    plt.savefig(vis_path, bbox_inches="tight")


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    output_folder = "./figures"
    main(csv_file, output_folder)
