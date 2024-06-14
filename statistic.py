from utils.util import *

import nltk


def count_video(csv_data):
    return len(csv_data)


def count_attribute(csv_data):
    count = 0
    for data in csv_data:
        for attribute in ATTRIBUTES:
            if not is_empty(data[attribute]):
                count += 1
    return count


def measure_avg_attributes_per_video(csv_data):
    no_of_attributes_asscociated = []
    for data in csv_data:
        count = 0
        for attribute in ATTRIBUTES:
            if not is_empty(data[attribute]):
                count += 1
        no_of_attributes_asscociated.append(count)
    return sum(no_of_attributes_asscociated) / len(no_of_attributes_asscociated)


def count_objects(csv_data):
    count = 0
    for data in csv_data:
        for object in OBJECTS:
            if not is_empty(data[object]):
                count += 1
    return count


def measure_avg_objects_per_video(csv_data):
    no_of_objects_asscociated = []
    for data in csv_data:
        count = 0
        for object in OBJECTS:
            if not is_empty(data[object]):
                count += 1
        no_of_objects_asscociated.append(count)
    return sum(no_of_objects_asscociated) / len(no_of_objects_asscociated)


def count_easy_data(csv_data):
    count = 0
    for data in csv_data:
        if is_simple(data):
            count += 1
    return count


def count_medium_data(csv_data):
    count = 0
    for data in csv_data:
        if is_medium(data):
            count += 1
    return count


def count_hard_data(csv_data):
    count = 0
    for data in csv_data:
        if is_hard(data):
            count += 1
    return count


def measure_avg_sentences(csv_data):
    no_of_sentences = []

    for data in csv_data:
        caption = data[CAPTION]
        sentences = nltk.sent_tokenize(caption)
        no_of_sentences.append(len(sentences))

    return sum(no_of_sentences) / len(no_of_sentences)


def main(csv_file: str, train_file: str, test_file: str):

    csv_data = read_csv(csv_file)

    print(" ---- Total Dataset ---- ")
    video_count = count_video(csv_data)
    print(f"There are {video_count} videos in total.")

    attribute_count = count_attribute(csv_data)
    print(f"There are {attribute_count} attributes in total.")

    avg_attributes_per_video = measure_avg_attributes_per_video(csv_data)
    print(
        f"Average number of attributes associated with a video: {avg_attributes_per_video}"
    )

    object_count = count_objects(csv_data)
    print(f"There are {object_count} objects in total.")

    avg_objects_per_video = measure_avg_objects_per_video(csv_data)
    print(f"Average number of objects associated with a video: {avg_objects_per_video}")

    simple_data_count = count_easy_data(csv_data)
    print(f"There are {simple_data_count} simple data in total.")

    medium_data_count = count_medium_data(csv_data)
    print(f"There are {medium_data_count} medium data in total.")

    hard_data_count = count_hard_data(csv_data)
    print(f"There are {hard_data_count} hard data in total.")

    assert (
        video_count == simple_data_count + medium_data_count + hard_data_count
    ), f"Video count is not equal to the sum of simple, medium and hard data count"

    print(
        f"Average number of sentences in a caption: {measure_avg_sentences(csv_data)}"
    )

    print(" ---- Train Dataset ---- ")
    train_data = read_csv(train_file)

    train_data_count = count_video(train_data)
    print(f"There are {train_data_count} videos in train dataset.")

    train_attribute_count = count_attribute(train_data)
    print(f"There are {train_attribute_count} attributes in train dataset.")

    train_avg_attributes_per_video = measure_avg_attributes_per_video(train_data)
    print(
        f"Average number of attributes associated with a video in train dataset: {train_avg_attributes_per_video}"
    )

    train_object_count = count_objects(train_data)
    print(f"There are {train_object_count} objects in train dataset.")

    train_avg_objects_per_video = measure_avg_objects_per_video(train_data)
    print(
        f"Average number of objects associated with a video in train dataset: {train_avg_objects_per_video}"
    )

    train_simple_data_count = count_easy_data(train_data)
    print(f"There are {train_simple_data_count} simple data in train dataset.")

    train_medium_data_count = count_medium_data(train_data)
    print(f"There are {train_medium_data_count} medium data in train dataset.")

    train_hard_data_count = count_hard_data(train_data)
    print(f"There are {train_hard_data_count} hard data in train dataset.")

    assert (
        train_data_count
        == train_simple_data_count + train_medium_data_count + train_hard_data_count
    ), f"Train video count is not equal to the sum of simple, medium and hard data count"

    print(" ---- Test Dataset ---- ")
    test_data = read_csv(test_file)

    for data in test_data:
        if data[VIDEO_ID] == "GreenIsland_SteelReef_Apr10_2023/0017.mp4":
            print(data)

    test_data_count = count_video(test_data)
    print(f"There are {test_data_count} videos in test dataset.")

    test_attribute_count = count_attribute(test_data)
    print(f"There are {test_attribute_count} attributes in test dataset.")

    test_avg_attributes_per_video = measure_avg_attributes_per_video(test_data)
    print(
        f"Average number of attributes associated with a video in test dataset: {test_avg_attributes_per_video}"
    )

    test_object_count = count_objects(test_data)
    print(f"There are {test_object_count} objects in test dataset.")

    test_avg_objects_per_video = measure_avg_objects_per_video(test_data)
    print(
        f"Average number of objects associated with a video in test dataset: {test_avg_objects_per_video}"
    )

    test_simple_data_count = count_easy_data(test_data)
    print(f"There are {test_simple_data_count} simple data in test dataset.")

    test_medium_data_count = count_medium_data(test_data)
    print(f"There are {test_medium_data_count} medium data in test dataset.")

    test_hard_data_count = count_hard_data(test_data)
    print(f"There are {test_hard_data_count} hard data in test dataset.")

    assert (
        test_data_count
        == test_simple_data_count + test_medium_data_count + test_hard_data_count
    ), f"Test video count is not equal to the sum of simple, medium and hard data count"


if __name__ == "__main__":
    csv_file = "./data/mvk_caption.csv"
    train_file = "data/train.csv"
    test_file = "data/test.csv"
    main(csv_file, train_file, test_file)
