from PIL import Image
import numpy as np
import json

def _tobinary(message):
    if isinstance(message,np.ndarray):
        message=json.dumps(message.tolist())
        
    if not isinstance(message,str):
         message=str(message)
    binary_message=''.join(format(ord(char),'08b') for char in message)
    return binary_message
        

def encoded_img(img_path ,message,output_path):
    img=Image.open(img_path)
    binary_msg=_tobinary(message)
    pixels=img.getdata()
    new_pixels=[]
    
    msg_index=0
    for pixel in pixels:
        if msg_index < len(binary_msg):
            r,g,b=pixel
            r=(r & ~1) | int(binary_msg[msg_index])
            msg_index +=1
            new_pixels.append((r,g,b))
        else:
            new_pixels.append(pixel)
            
    img.putdata(new_pixels)
    img.save(output_path)


def decode_message(image_path):
    img = Image.open(image_path)
    pixels = img.getdata()
    binary_msg = ''

    for pixel in pixels:
        r, g, b = pixel
        binary_msg += str(r & 1)

    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''
    for char in chars:
        if int(char, 2) == 0:
            break
        message += chr(int(char, 2))

    

# Example usage:
# decode_message("output.png")

    
         

           