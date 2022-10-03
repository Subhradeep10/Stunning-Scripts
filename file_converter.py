from PIL import Image

filePath = input('Enter the path to the image: ')
ext = filePath.split('/')[-1].split('.')[-1]
folderPath = '/'.join(filePath.split('/')[:-1])

# im1 = Image.open('file name.jpg')  # path where the JPG is stored
# im1.save('new file name.png')   # path where the PNG will be stored