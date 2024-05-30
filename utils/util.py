import csv

VIDEO_ID = "Video ID"
CENTRAL_OBJECT = "Central_Object"
TEXTURE = "Texture"
COLOR = "Color"
SIZE_SHAPE = "Size_Shape"
OBJECT_2 = "Object_2"
OBJECT_3 = "Object_3"
OBJECT_4 = "Object_4"
ENVIRONMENT = "Environment"
LIGHTING = "Lighting"
VIDEO_CLARITY = "Video_Clarity"
MOVEMENT_BEHAVIOR = "Movement_Behavior"
CAMERA_POSITION = "Camera_Position"
CAMERA_ANGLE = "Camera_Angle"
CAPTION = "Caption"
FOLDER = "Folder"

ATTRIBUTES = [
    CENTRAL_OBJECT,
    TEXTURE,
    COLOR,
    SIZE_SHAPE,
    OBJECT_2,
    OBJECT_3,
    OBJECT_4,
    ENVIRONMENT,
    LIGHTING,
    VIDEO_CLARITY,
    MOVEMENT_BEHAVIOR,
    CAMERA_POSITION,
    CAMERA_ANGLE,
]


def read_csv(file: str):
    # Return a list of dictionaries
    # The key of the dictionary is the header of the csv file
    # The value is the data of each row
    # Also note that the first line of the csv file is the header
    # Also note that the delimiter is ";"

    with open(file, mode="r") as infile:
        reader = csv.reader(infile, delimiter=";")
        data = [row for row in reader]
    header = data[0]
    data = data[1:]
    return [{header[i]: row[i] for i in range(len(header))} for row in data]
