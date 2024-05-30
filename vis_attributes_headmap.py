from utils.util import *

import os
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main(csv_file: str, output_folder: str, n: int):

    os.makedirs(output_folder, exist_ok=True)
    csv_data = read_csv(csv_file)

    video_count = len(csv_data)
    attributes_count = len(ATTRIBUTES)

    binary_matrix = np.zeros((video_count, attributes_count))

    for i, row in enumerate(csv_data):
        for j, attribute in enumerate(ATTRIBUTES):
            if row[attribute] != "":
                binary_matrix[i][j] = 1

    # Aggregate the data
    num_groups = binary_matrix.shape[0] // n
    aggregated_matrix = np.array(
        [np.sum(binary_matrix[i * n : (i + 1) * n], axis=0) for i in range(num_groups)]
    )

    # Normalize the aggregated data to scale the color intensity
    normalized_matrix = aggregated_matrix / n
    normalized_matrix = normalized_matrix.T

    # Attribute names
    attributes = ATTRIBUTES

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(normalized_matrix, aspect="auto", cmap="Reds")

    # Add labels and title
    plt.title("Heatmap of Aggregated Video Attributes Presence")
    plt.ylabel("Attributes")
    plt.xlabel("Videos")

    # Set the attribute names as x-ticks
    plt.yticks(ticks=np.arange(len(attributes)), labels=attributes)
    plt.xticks([])

    plt.subplots_adjust(left=0.2)

    output_path = os.path.join(output_folder, "attributes_heatmap.png")
    plt.savefig(output_path)


if __name__ == "__main__":
    csv_file = "./data/mvk_caption.csv"
    output_folder = "./figures"
    aggregate_size = 5
    main(csv_file, output_folder, aggregate_size)
