import json
import time
from utils.util import *


def write_json(file: str, json_data):
    with open(file, "w") as f:
        json.dump(json_data, f)


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    json_datas = []

    for data in csv_data:

        # Get current time in this format: 2024:05:26 23:26:44
        current_time = time.strftime("%Y:%m:%d %H:%M:%S")

        duration = -1
        fps = -1
        width = -1
        height = -1
        source = ""
        original_name = data[VIDEO_ID]
        filename = data[FILENAME]
        caption = data[CAPTION]
        caption_attributes = []
        create_time = current_time
        ext = "mp4"
        path = ""

        json_data = {
            "duration": duration,
            "fps": fps,
            "width": width,
            "height": height,
            "source": source,
            "original_name": original_name,
            "filename": filename,
            "caption": caption,
            "caption_attributes": caption_attributes,
            "create_time": create_time,
            "ext": ext,
            "path": path,
        }

        json_datas.append(json_data)

    output_path = csv_file.replace(".csv", ".json")
    write_json(output_path, json_datas)

    pass


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
