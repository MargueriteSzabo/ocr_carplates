import pandas as pd
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import cv2


def draw_boundingbox(image_num, x_0=None, x_1=None, y_0=None, y_1=None):
    """Draw a rectangle on an image based on coordinates.
    Coordinates are either found or given."""
    image = cv2.imread(f"../data/train/{image_num}.jpg")

    #get the bounding box coordinates if they are not given
    if x_0 is None :
        data = pd.read_csv('../data/submission.csv')
        coordinates = data[data['file']==f"{image_num}.jpg"]
        x_0 = coordinates[x_0]
        x_1 = coordinates[x_1]
        y_0 =coordinates[y_0]
        y_1 = coordinates[y_1]

    #shows the image
    # Start coordinate represents the top left corner of rectangle
    start_point = (x_0, y_0)

    # Ending coordinate represents the bottom right corner of rectangle
    end_point = (x_1, y_1)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 10 px
    thickness = 10

    # Draw a rectangle with blue line borders of thickness of 10 px
    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Displaying the image
    PIL_image = Image.fromarray(np.uint8(image)).convert('RGB')
    PIL_image.show()

    return PIL_image


def cropping_images(image_path, x_0, x_1, y_0, y_1):
    """Fuction used to crop all the images available"""
    image = cv2.imread(f"../data/train/{image_path}")
    try:
        cropped = image[y_0:y_1, x_0:x_1]
        PIL_cropped = Image.fromarray(np.uint8(cropped)).convert('RGB')
        return PIL_cropped
    except:
        return None



def cropping_all_images():
    data = pd.read_csv('../data/plate_infos.csv')
    print(data.shape)

    for index, row in data.iterrows():
        print(row['file'])
        image_num = row['file'].split('/')[1]
        cropped = cropping_images(image_num, row['x_0'], row['x_1'], row['y_0'], row['y_1'])
        if cropped:
            cropped.save(f"../data/train/cropped/cropped_{image_num}.jpg")
    # function to be corrected when coordinates are outside of the image.




if __name__ == "__main__":
    cropping_all_images()
