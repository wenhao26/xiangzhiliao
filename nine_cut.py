# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 14:43
# @Author  : 胡椒
# @FileName: nine_cut.py
# @Software: PyCharm
from PIL import Image
import os
import time


def file_exists(file_path):
    """
    Picture presence detection
    :param file_path:Picture path
    :return:
    """
    return os.path.exists(file_path)


def fill_image(im):
    """
    Picture filled with square
    :param im:Picture object
    :return:
    """
    width, height = im.size
    # Select the larger value of the length and width of the original picture
    # as the radius of the nine palace grid of the new picture
    new_image_len = width if width > height else height
    # Create a white canvas
    new_image = Image.new(im.mode, (new_image_len, new_image_len), color="white")
    # Paste the original image on the canvas at the center
    if width > height:
        new_image.paste(im, (0, int((new_image_len - height) / 2)))
    else:
        new_image.paste(im, (int((new_image_len - width) / 2), 0))
    return new_image


def cut_image(im):
    """
    Cut the picture into nine palaces
    :param im:Picture object
    :return:
    """
    width, height = im.size
    # Three pictures in a row
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [im.crop(box) for box in box_list]
    return image_list


def save_image(files):
    """
    Save pictures
    :param files:File list
    :return:
    """
    i = 1
    for file in files:
        file.save(str(i) + ".png", "PNG")
        i += 1


if __name__ == '__main__':
    while True:
        image_path = str(input("Please enter the picture path, and enter “exit” if you want to exit："))
        if image_path == "exit":
            print("The program has ended, welcome to use next time！")
            time.sleep(2)
            break

        if file_exists(image_path):
            image = Image.open(image_path)
            image = fill_image(image)
            images = cut_image(image)
            save_image(images)
            print("(*^▽^*)Image clipping complete.")
        else:
            print("Not a valid picture path")
