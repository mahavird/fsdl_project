"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io
from PIL import Image

import torch
from flask import Flask, request
import numpy as np
import cv2

from predict_streamlit import detect


def predict(image):
    # convert string of image data to uint8
    nparr = np.fromstring(image, np.uint8)
    # decode image
    im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    #saving image for debugging. disable it before deployment
    cv2.imwrite("client_image.jpg",im)

    #passing image to predictor


    response = detect("client_image.jpg")
    #print("cat, conf",response)

    return response