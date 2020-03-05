import glob
from exchange.models import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

font = ImageFont.truetype("Spartan-Regular.ttf", 16)
subtitlefont = ImageFont.truetype("Spartan-SemiBold.ttf", 10)


image_names = glob.glob("reddit/*.*")
for image_name in image_names:
    img = Image.open(image_name)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    #Should we use black or white text? 
    text_area = img.crop((20, img.height-40, 230, img.height-20)) #get the background of the text area
    text_area.thumbnail((1, 1))
    pixel = text_area.getpixel((0,0)) #shrink it to one pixel
    gray_scale = (pixel[0]*0.2989 + pixel[1]*0.5870 + pixel[2]*0.1140) / 255 #calculate the grayscale val
    if gray_scale < 0.5:
        rgb = (255, 255, 255)
    else:
        rgb = (0,0,0)
    draw.text((20, img.height-55),"Sign up for the March Exchange at",rgb,font=subtitlefont)
    draw.text((20, img.height-40),"GraffExchange.com",rgb,font=font)
    img.save("reddit/marked/"+image_name.split("reddit/")[1])
