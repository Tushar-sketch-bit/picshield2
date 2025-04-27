import os
import numpy as np
import steganography as stg
import cv2
import os
import numpy as np
from numpy import random



folder_path="D:/Hackathon/PicShield/uploads"
output_path="D:/Hackathon/PicShield/outputs"


def random_code_generator():
    return np.random.rand(3,3)

os.makedirs(output_path,exist_ok=True)

def iterate_over_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path=os.path.join(folder_path,filename)
            
            random_code=random_code_generator()
            output_image_path = os.path.join(output_path, "encoded_" + filename)
            stg.encoded_img(image_path,random_code,output_image_path)
            
    
iterate_over_images(folder_path)



