# -*- coding: utf-8 -*-

from PIL import Image , ImageFilter , ImageDraw

image = Image.open("icon.jpeg")

image_width , image_height = image.size

draw = ImageDraw.Draw(image)

draw.text(xy=(image_width - 40 , 0), text='20', fill='#ff0000')

image.save('icom_num.jpeg' , 'jpeg')




# 给图片增加模糊处理
# image2 = image.filter(ImageFilter.BLUR)
# image2.save('blur.jpeg' , 'jpeg')



