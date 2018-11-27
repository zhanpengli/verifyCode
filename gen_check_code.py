from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
from PIL import Image
import random
# import matplotlib.pyplot as plt
import os
from random import choice

root_dir = "taiwanCode/train"

def gen_list():
    img_list = []
    for parent, dirnames, filenames in os.walk(root_dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            img_list.append(filename.replace(".png", ""))
    return img_list

img_list = gen_list()

def get_list():
    return img_list

def gen_captcha_text_and_image_new():
    # print(img_list)
    img = choice(img_list)
    captcha_image = Image.open(root_dir + "/" + img + ".png")
    from PIL import ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    captcha_image = captcha_image.resize((162, 54))
    # captcha_image = np.array(captcha_image)
    return img, captcha_image
