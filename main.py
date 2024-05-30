import os
import fnmatch
import json
import re
import pandas as pd
import sys
from unidecode import unidecode
import numpy as np


def write_file():
    # Directory to search
    # dir_path = '/media/qttruong/f0816220-235d-45fe-a03e-f17de2c9267b/marine_data/test_marine1'
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

def parse_captioning_csv():
    # Check if any arguments were passed
    if len(sys.argv) > 1:
        print(f'Arguments received: {sys.argv[1:]}')
    else:
        print('No arguments were passed.')

    dir_path = sys.argv[1]

    # Load the CSV file
    df = pd.read_csv(dir_path, delimiter=';')

    print(df.columns)

    for column in df.columns:
        # Kiểm tra nếu cột là kiểu dữ liệu chuỗi
        if df[column].dtype == object:
            # Duyệt qua từng hàng
            for idx in df.index:
                # Chuyển đổi chuỗi có dấu sang không dấu
                if pd.isnull(df.loc[idx, column]):
                    df.loc[idx, column] = unidecode(str(df.loc[idx, column]))

    # In DataFrame
    # non_nan_count_per_row = df.count(axis=1)
    print(df['Video ID'])

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Write the JSON data to a file
    # with open('output.json', 'w') as json_file:
    #     json_file.write(json_data)

if __name__ == '__main__':
    parse_captioning_csv()