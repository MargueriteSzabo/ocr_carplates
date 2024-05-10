OCR model on car plates.

Dataset found on Kaggle here : https://www.kaggle.com/datasets/xairete/car-plates-ocr/data.

Notebooks are used to try out code and output.

# Done

**image_processing.py** : functions to work on bounding boxes :
- draw rectangles around the plate on the image
- crop the image on the rectangle

**json_extract.py** : extract bounding boxe infos for each image and save them in a csv

# To do

- 1 / Prepare images for yolo
- 2 / Upload the image on a bucket on GCP
- 3 / Create upload and download functions for GCP
- 4 / Create a file to orchestrate functions
- 5 / Train YoloV5 (or 7?) to find the plate on the image
- 6 / Train Pytesseract to extract the information

More infos to come.
