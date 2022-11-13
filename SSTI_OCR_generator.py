#!/bin/python3

import os
from PIL import Image, ImageDraw

nameCount = 0

# Creates .png images that contain SSTI payloads
# These images will be read by online OCR and saved as text on the server

with open('payload.txt', 'r') as file:
    for line in file:

        img = Image.new('RGB', (1300, 100), color = (255, 255, 255))
 
        d = ImageDraw.Draw(img)
        d.text((30, 30), line, fill=(0,0,0))
         
        img.save('pil_text'+ str(nameCount) + '.png')

        nameCount = nameCount + 1
