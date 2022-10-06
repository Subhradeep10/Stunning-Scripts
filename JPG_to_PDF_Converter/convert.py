from PIL import Image

image_1 = Image.open(r'path') # here path = path where the image is stored\file name.png

im_1 = image_1.convert('RGB')

im_1.save(r'path') # here path = path where the pdf will be stored\new file name.pdf