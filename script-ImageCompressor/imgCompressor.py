#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

# Usage:执行脚本时，在后面跟上一条图片的路径[可选：也可以再跟上一个0~100的整数数字参数作为保存图片的质量参数，如不填则默认为80]
#       转换后的图片将命名为原图片名称+“-convert”，放在与原图同一个目录下
#       请事先将gif2webp程序加入环境变量，否则无法使用gif转webp的功能
#

from PIL import Image
import os, sys, platform

if sys.argv[1] is not None:
    imgFile = sys.argv[1]
else:
    print("You should give a path of a pic")
    exit()
qua = -1
if len(sys.argv) == 3:
    qua = int(sys.argv[2])
if qua < 0 or qua > 100:
    alert = """
The quality parameter should be between 0 and 100.
If you don't enter or enter the wrong value, it will be the default 80.
Now the image is convert with the default value 80...
        """
    print(alert)

if not os.path.exists(imgFile):
    print("\nERR: File doesn't exist.")
    exit(0)

inputName = os.path.splitext(imgFile.split("/")[-1])
suffix = inputName[1]  # 图片后缀名
outputName = inputName[0] + "-convert"
path = imgFile.split(inputName[0])[0]

# 如果是gif图片的话则用gif2webp处理
if suffix == ".gif":
    try:
        if platform.platform().lower().find("windows"):
            os.system("gif2webp.exe " + imgFile + " -o " + outputName + ".webp")
        else:
            os.system("gif2webp " + imgFile + " -o " + outputName + ".webp")
        print("Compression succeed.\n")
    except Exception as e:
        print(e + "\nCompression gif file failed.\n")

# 否则直接用Image模块处理
else:
    try:
        image = Image.open(imgFile)
        # 对RGBA和LA模式进行兼容
        if image.mode in ('RGBA', 'LA'):
            fill_color = "#000"  # 使用黑色进行填充
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background

        outputName = path + outputName + suffix
        if -1 < qua < 101:
            image.save(outputName, quality=qua)
        else:
            image.save(outputName, quality=80)
        print("Compression succeed.\n")
    except Exception as e:
        print(e + "\nCompression failed.\n")
