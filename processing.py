from utils.util import *


def redefined_video_id(csv_data):
    for data in csv_data:
        video_id = data[VIDEO_ID]
        folder = data[FOLDER]
        new_video_id = f"{folder}/{video_id}"
        data[VIDEO_ID] = new_video_id
    return csv_data


def remove_newline_character(csv_data):
    for data in csv_data:
        for attribute in ATTRIBUTES:
            data[attribute] = data[attribute].replace("\n", " ").replace("\r", " ")
    return csv_data


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    print("Refined video id")
    csv_data = redefined_video_id(csv_data)

    print("Remove new line character")
    csv_data = remove_newline_character(csv_data)

    print("Write to new csv file")
    write_csv("data/mvk_caption_refined.csv", csv_data)


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
