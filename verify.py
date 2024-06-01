from utils.util import *


def check_video_id_unique(csv_data):
    video_ids = set()
    for data in csv_data:
        video_id = data[VIDEO_ID]
        if video_id in video_ids:
            print(f"Duplicate video id {video_id}")
        else:
            video_ids.add(video_id)


def check_central_obj(csv_data):
    for data in csv_data:
        if is_empty(data[CENTRAL_OBJECT]):
            print(f"Empty central object in video {data[VIDEO_ID]}")


def check_no_newline_character(csv_data):
    for data in csv_data:
        for attribute in ATTRIBUTES:
            if "\n" in data[attribute] or "\r" in data[attribute]:
                print(f"Newline character in {attribute} in video {data[VIDEO_ID]}")


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    print("Checking for unique video ids")
    check_video_id_unique(csv_data)

    print("Checking for empty attributes")
    check_central_obj(csv_data)

    print("Checking for newline character")
    check_no_newline_character(csv_data)


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
