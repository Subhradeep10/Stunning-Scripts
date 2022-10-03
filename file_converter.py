from PIL import Image

filePath = input('Enter the path to the image: ')
ext = filePath.split('/')[-1].split('.')[-1]
folderPath = '/'.join(filePath.split('/')[:-1])
fileName = ''.join(filePath.split('/')[-1].split('.')[:-1])

if ext == 'png':
    img = Image.open(filePath)
    img.save(f'{folderPath}/{fileName}.jpg')
else:
    img = Image.open(filePath)
    img.save(f'{folderPath}/{fileName}.png')