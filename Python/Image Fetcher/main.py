import requests;
from PIL import Image

def img_requests(txt):
    response=requests.get("https://source.unsplash.com/random{0}".format(txt))
    file=open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close

#Main Function
print("""Please provide an option for Image
     # 1, HD Random Picture
     # 2, FHD Random Picture
     # 3, 2K Random Picture
     # 4, 4k Random Picture
     # 5, Picture with User Provided Keywords """)
#Takes User Choice
ans=input()

if 'one' in ans or '1' in ans:
     print("Please wait while we fetch the images from our database.")
     img_requests('/1280x720')
elif 'two' in ans or '2' in ans:        
     print("Please wait while we fetch the images from our database.")    
     img_requests('/1920x1080')
elif 'three' in ans or '3' in ans:
     print("Please wait while we fetch the images from our database.")
     img_requests('/2048x1080')
elif 'four' in ans or '4' in ans:
     print("Please wait while we fetch the images from our database.")
     img_requests('/4096x2160')
elif 'five' in ans or '5' in ans:    
     print("speak keywords seperated by commas ")
     st=input()
     if 'comma' in st:
          st.replace('comma',',')
     st="?"+st
     print("Please wait while we fetch the images from our database.")
     img_requests(st)
else:
     print("Please provide a valid Input")