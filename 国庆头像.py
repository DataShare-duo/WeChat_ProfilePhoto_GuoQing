"""
===========================
@Time : 2022/9/30 13:24
@File : 国庆头像.py
@Software: PyCharm
@Platform: Win10
@Author : DataShare
===========================
"""
from PIL import Image

guoqi = Image.open('国旗.jpg')
touxiang = Image.open('自己头像.jpg')

# 获取国旗的尺寸
x,y = guoqi.size
# 根据需求，设置左上角坐标和右下角坐标（截取的是正方形）
quyu = guoqi.crop((60,20, x-40-280,y))


# 获取头像的尺寸
w,h = touxiang.size
# 将区域尺寸重置为头像的尺寸
quyu = quyu.resize((w,h))
# 透明渐变设置
for i in range(w):
    for j in range(h):
        color = quyu.getpixel((i, j))
        alpha = 255-i*2//5
        if alpha < 0:
            alpha=0
        color = color[:-1] + (alpha, )
        quyu.putpixel((i, j), color)


touxiang.paste(quyu,(0,0),quyu)

touxiang.save('自己头像-国庆.png')


