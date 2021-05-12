# coding=utf-8
from PIL import Image
import os
import shutil


def resize(img, size1, size2, prefix, dir_name="iosicons"):
    result_name = "%s%sx%s@%sx.png" % (prefix, size1, size1, size2)
    print("resize %s" % result_name)
    out = img.resize((int(size1 * size2), int(size1 * size2)))
    out.save("%s/%s" % (dir_name, result_name))


def process_ios_icons():
    orn_img_path = input("input origin img path: ")
    orn_img_path = orn_img_path.strip()
    prefix = input("input img prefix (default is Icon-App-) : ")
    if prefix == '':
        prefix = "Icon-App-"

    shutil.rmtree("iosicons")
    os.mkdir("iosicons")
    img = Image.open(orn_img_path)

    resize(img, 20, 1, prefix)
    resize(img, 20, 2, prefix)
    resize(img, 20, 3, prefix)

    resize(img, 29, 1, prefix)
    resize(img, 29, 2, prefix)
    resize(img, 29, 3, prefix)

    resize(img, 40, 1, prefix)

    resize(img, 60, 2, prefix)

    resize(img, 76, 1, prefix)
    resize(img, 76, 2, prefix)

    resize(img, 83.5, 2, prefix)

    resize(img, 1024, 1, prefix)


if __name__ == '__main__':
    process_ios_icons()
