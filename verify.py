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


def check_camear_angle(csv_data):
    for data in csv_data:
        if is_empty(data[CAMERA_ANGLE]):
            print(
                f"Invalid camera angle {data[CAMERA_ANGLE]} in video {data[VIDEO_ID]}"
            )


def check_camera_position(csv_data):
    for data in csv_data:
        if is_empty(data[CAMERA_POSITION]):
            print(
                f"Invalid camera position {data[CAMERA_POSITION]} in video {data[VIDEO_ID]}"
            )


def check_environment(csv_data):
    for data in csv_data:
        if is_empty(data[ENVIRONMENT]):
            print(f"Invalid environment {data[ENVIRONMENT]} in video {data[VIDEO_ID]}")


def check_video_clarity(csv_data):
    for data in csv_data:
        if is_empty(data[VIDEO_CLARITY]):
            print(
                f"Invalid video clarity {data[VIDEO_CLARITY]} in video {data[VIDEO_ID]}"
            )


def check_complexity(csv_data):
    for data in csv_data:
        object_count = count_object(data)
        complexity = data[COMPLEXITY]
        if object_count == 1:
            if complexity != "simple":
                print(f"Complexity should be simple for video {data[VIDEO_ID]}")
        elif object_count == 2:
            if complexity != "medium":
                print(f"Complexity should be medium for video {data[VIDEO_ID]}")
        elif object_count >= 3:
            if complexity != "hard":
                print(f"Complexity should be hard for video {data[VIDEO_ID]}")
        else:
            print("Error: Unknown complexity")


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    print("Checking for unique video ids")
    check_video_id_unique(csv_data)

    print("Checking for empty attributes")
    check_central_obj(csv_data)

    print("Checking for newline character")
    check_no_newline_character(csv_data)

    # print("Checking for camera angle")
    # check_camear_angle(csv_data)

    # print("Checking for camera position")
    # check_camera_position(csv_data)

    # print("Checking for environment")
    # check_environment(csv_data)

    # print("Checking for video clarity")
    # check_video_clarity(csv_data)
    print("Checking for complexity")
    check_complexity(csv_data)

    print("Done")


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
