# <center>Requirements</center> 
1. Step-I :
    At first you need the Pillow package which is required of the conversion of the file.
   
     `pip install Pillow`

2. Step-II :
    Locate the path where the image is stored.
    
    For example, suppose we have a jpg file named 'test' and it the stored under the following path:
    
    >C:\Users\Example\Desktop\Test\test.jpg
3. Step-III :
   Use the following format-
   
   >from PIL import Image

   >image_1 = Image.open(r'path where the image is stored\file name.png')
   im_1 = image_1.convert('RGB')

   >im_1.save(r'path where the pdf will be stored\new file name.pdf')     
