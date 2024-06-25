from PIL import Image
import argparse
import os
from tqdm import tqdm

def is_image(image_file:str):
    try:
        Image.open(image_file)
        return True
    except:
        return False
    
def main(args):
    input_dir = args.input_dir
    assert os.path.exists(input_dir), f"Frame folder {input_dir} does not exist"

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    width = args.width
    height = args.height

    for frame_dirname in tqdm(os.listdir(input_dir), desc="Resize frames"):
        frame_dir = os.path.join(input_dir, frame_dirname)
        if not os.path.isdir(frame_dir):
            continue

        output_frame_dir = os.path.join(output_dir, frame_dirname)
        os.makedirs(output_frame_dir, exist_ok=True)

        # Extract all the image files (verified)
        image_files = os.listdir(frame_dir)
        image_files = [os.path.join(frame_dir, image_file) for image_file in image_files if is_image(os.path.join(frame_dir, image_file))]
        for frame_file in tqdm(image_files, desc=f"Resize frames in {frame_dirname}"):
            filename = os.path.basename(frame_file)
            output_frame_file_path = os.path.join(output_frame_dir, filename)
            with Image.open(frame_file) as img:
                img = img.resize((width, height))
                img.save(output_frame_file_path)

if __name__ == "__main__":
    DEFAULT_WIDTH = 720
    DEFAULT_HEIGHT = 480

    parser = argparse.ArgumentParser(description="Resize frames in a folder")
    parser.add_argument("--input_dir", type=str, help="The folder containing frames")
    parser.add_argument("--output_dir", type=str, help="Output folder to store resized frames")
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH, help=f"Width of the resized frames. Default: {DEFAULT_WIDTH}")
    parser.add_argument("--height", type=int, default=DEFAULT_HEIGHT, help=f"Height of the resized frames. Default: {DEFAULT_HEIGHT}")


    args = parser.parse_args()
    main(args)