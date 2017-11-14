# resize yysGAN.py
import os
from PIL import Image

src = "../input" 
dst = "./resized" # resized

if not os.path.exists(dst):
    os.mkdir(dst)


for each in os.listdir(src):
    try:
        img = Image.open(os.path.join(src,each))
        out = img.resize((128, 128),Image.ANTIALIAS) 
        out.save(os.path.join(dst,each))
    except:
        pass
    
    
