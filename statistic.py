from utils.util import *


def main(csv_file: str):

    csv_data = read_csv(csv_file)

    video_count = len(csv_data)
    print(f"There are {video_count} videos in total.")

    print()
    print("-" * 20)
    for attribute in ATTRIBUTES:
        video_count = 0
        for data in csv_data:
            if data[attribute] != "":
                video_count += 1

        print(f"There are {video_count} videos with {attribute} attribute.")

    print()
    print("-" * 20)
    print(f"There are {len(ATTRIBUTES)} attributes in total.")
    no_of_attributes_asscociated = []
    for data in csv_data:
        count = 0
        for attribute in ATTRIBUTES:
            if data[attribute] != "":
                count += 1
        no_of_attributes_asscociated.append(count)
    print(
        f"Average number of attributes associated with a video: {sum(no_of_attributes_asscociated) / len(no_of_attributes_asscociated)}"
    )

    OBJECTS = [CENTRAL_OBJECT, OBJECT_2, OBJECT_3, OBJECT_4]
    print()
    print("-" * 20)

    # Count the average number of objects that video have
    no_of_objects = []
    for data in csv_data:
        count = 0
        for object in OBJECTS:
            if data[object] != "":
                count += 1
        no_of_objects.append(count)
    print(f"There are {sum(no_of_objects)} objects in total.")
    print(
        f"Average number of objects associated with a video: {sum(no_of_objects) / len(no_of_objects)}"
    )

    print()
    print("-" * 20)
    # Count the number of non empty attributes
    attribute_count = 0
    for data in csv_data:
        count = 0
        for attribute in ATTRIBUTES:
            if data[attribute] != "":
                count += 1
        attribute_count += count
    print(f"Number of non-empty attributes: {attribute_count}")


if __name__ == "__main__":
    csv_file = "./data/final_caption.csv"
    main(csv_file)
