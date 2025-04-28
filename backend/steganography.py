from PIL import Image
import numpy as np
import json

def encoded_img(img_path, message, output_path):
    """Embed message in image and save to output_path"""
    try:
        # Open image and convert to RGB (in case it's PNG with transparency)
        img = Image.open(img_path).convert('RGB')
        pixels = np.array(img)
        
        # Convert message to binary
        binary_msg = ''.join(format(ord(char), '08b') for char in str(message))
        
        # Check if message fits
        required_pixels = len(binary_msg)
        available_pixels = pixels.shape[0] * pixels.shape[1]
        if required_pixels > available_pixels:
            raise ValueError(f"Message too large. Needs {required_pixels} pixels but image has {available_pixels}")
        
        # Embed in LSB (red channel)
        msg_index = 0
        for row in pixels:
            for pixel in row:
                if msg_index < len(binary_msg):
                    pixel[0] = (pixel[0] & 254) | int(binary_msg[msg_index])
                    msg_index += 1
        
        # Save the encoded image
        Image.fromarray(pixels).save(output_path)
        print(f"Successfully saved encoded image to {output_path}")
        return True
        
    except Exception as e:
        print(f"Encoding failed: {str(e)}")
        return False


def decode_message(image_path):
    """Extract hidden message from image"""
    img = Image.open(image_path)
    pixels = np.array(img)
    
    binary_msg = ''
    message = ''
    
    # Extract LSBs from red channel
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            binary_msg += str(pixels[i,j,0] & 1)
    
    # Convert binary to string
    for i in range(0, len(binary_msg), 8):
        byte = binary_msg[i:i+8]
        if byte:  # Skip empty bytes
            char = chr(int(byte, 2))
            if char == '\0':  # Null terminator
                break
            message += char
    
    return message



def embed_data(image_path, data):
    """Hide tracking data in image using LSB"""
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Convert data to binary
    binary_data = ''.join(format(ord(c), '08b') for c in data)
    
    # LSB embedding
    for i in range(len(binary_data)):
        x, y = i % img.width, i // img.width
        pixels[y,x,0] = (pixels[y,x,0] & 254) | int(binary_data[i])
    
    return Image.fromarray(pixels)