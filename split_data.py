from utils.util import *
import random
import os


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    simple_extract_count = 100
    medium_extract_count = 300
    hard_extract_count = 500

    simple_datas = [data for data in csv_data if is_simple(data)]
    medium_datas = [data for data in csv_data if is_medium(data)]
    hard_datas = [data for data in csv_data if is_hard(data)]

    assert len(csv_data) == len(simple_datas) + len(medium_datas) + len(
        hard_datas
    ), f"There are data that are not classified as simple, medium, or hard"

    random.shuffle(simple_datas)
    random.shuffle(medium_datas)
    random.shuffle(hard_datas)

    simple_extract = simple_datas[:simple_extract_count]
    simple_remain = simple_datas[simple_extract_count:]

    medium_extract = medium_datas[:medium_extract_count]
    medium_remain = medium_datas[medium_extract_count:]

    hard_extract = hard_datas[:hard_extract_count]
    hard_remain = hard_datas[hard_extract_count:]

    # Train set are the data that is not extracted
    train_data = simple_remain + medium_remain + hard_remain

    # Test set are the data that is extracted
    test_data = simple_extract + medium_extract + hard_extract

    assert len(train_data) == 1100, f"Train data should have 1100 data"
    assert len(test_data) == 900, f"Test data should have 900 data"

    output_folder = os.path.dirname(csv_file)
    train_output_path = os.path.join(output_folder, "train.csv")
    test_output_path = os.path.join(output_folder, "test.csv")

    write_csv(train_output_path, train_data)
    write_csv(test_output_path, test_data)


if __name__ == "__main__":
    csv_file = "data/mvk_caption.csv"
    main(csv_file)
