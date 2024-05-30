from utils.util import *

import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def main(csv_file: str, output_folder: str):
    csv_data = read_csv(csv_file)

    os.makedirs(output_folder, exist_ok=True)
    for attribute in ATTRIBUTES:
        print("Creating word cloud for", attribute)
        word_count = {}

        for data in csv_data:
            word = data[attribute]
            if word != "":
                if len(word.split()) > 1:
                    continue

                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        if len(word_count) == 0:
            continue

        # Create the word cloud
        wordcloud = WordCloud(
            width=800, height=400, background_color="white"
        ).generate_from_frequencies(word_count)
        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        output_path = os.path.join(output_folder, f"{attribute}_wordcloud.png")
        plt.savefig(output_path)
        plt.clf()


if __name__ == "__main__":
    csv_file = "./data/mvk_caption.csv"
    output_folder = "./figures/wordcloud"
    main(csv_file, output_folder)
