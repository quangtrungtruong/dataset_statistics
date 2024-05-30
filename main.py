import os
import fnmatch
import json
import re
import pandas as pd
import sys
from unidecode import unidecode
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def write_file():
    # Directory to search
    dir_path = '/media/qttruong/f0816220-235d-45fe-a03e-f17de2c9267b/marine_data/vimeo/underwater'

    # List of file extensions to search for
    extensions = ['*.AVI', '*.mov', '*.MOV', '*.mp4', '*.MP4', '*.wmv']
    c = 0
    num_digits = 8
    # Create a dictionary to hold the data
    data = {}
    # Open a file in write mode
    with open('data.json', 'w') as f:
        # Find and print names of .avi, .mov, .mp4, and .wmv files
        for root, dir, files in os.walk(dir_path):
            for extension in extensions:
                for file in fnmatch.filter(files, extension):
                    c += 1

                    str_num = str(c).zfill(num_digits) + '.mp4'

                    data[str_num] = file

                    file = os.path.join(dir_path, file)
                    new_file = os.path.join(dir_path, str_num)
                    print(new_file, file)

                    os.rename(file, new_file)

        json.dump(data, f)

def task3(df):
    print('Total object: ', df['Central_Object'].count() + df['Object_2'].count() + df['Object_3'].count() + df['Object_4'].count())
    data = df['Object_2']
    # print(data)
    sns.histplot(data, bins=10, kde=True)
    # Show the plot
    plt.show()

def parse_captioning_csv():
    # Check if any arguments were passed
    if len(sys.argv) > 1:
        print(f'Arguments received: {sys.argv[1:]}')
        dir_path = sys.argv[1]
    else:
        print('No arguments were passed.')
        dir_path = './data/mvk_caption.csv'


    # Load the CSV file
    df = pd.read_csv(dir_path, delimiter=';')
    return df

if __name__ == '__main__':
    df = parse_captioning_csv()

    # do task
    task3(df)