import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

import numpy as np

from wordcloud import WordCloud
from utils.util import *

# nltk.download("stopwords")
# nltk.download("punkt")


def main(csv_file: str, output_folder: str):

    os.makedirs(output_folder, exist_ok=True)

    csv_data = read_csv(csv_file)

    captions = []
    for data in csv_data:
        captions.append(data[CAPTION])

    # Load the set of English stopwords
    stop_words = set(stopwords.words("english"))

    # Tokenize each sentence into words and flatten the list
    words = [word for caption in captions for word in word_tokenize(caption.lower())]

    # Filter out stopwords and non-alphabetic words
    filtered_words = [
        word for word in words if word.isalpha() and word not in stop_words
    ]

    word_count = {}
    for word in filtered_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Create the word cloud
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(word_count)
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    output_path = os.path.join(output_folder, f"caption_wordcloud.png")
    plt.savefig(output_path)
    plt.clf()


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    output_folder = "./figures"
    main(csv_file, output_folder)
