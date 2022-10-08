from PIL import Image
import sys

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
image = Image.open(sys.argv[1])
resized = image.resize((width, height))
resized.save('output.jpeg')
