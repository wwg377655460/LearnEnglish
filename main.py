# -*- coding: utf-8 -*-
import xlrd
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

"""
英语单词生成图片，便于桌面展示
"""
class PrintWordImage:
    font_size_to_px = 1.3

    def __init__(self, imageFile, sourceFile, font_size=24, font="fonts\BreeSerif_Reg.otf"):
        self.font_size = font_size
        self.imageFile = imageFile
        self.sourceFile = sourceFile
        self.font = font

    def __createImage(self):
        # 设置字体，如果没有，也可以不设置
        self.font = ImageFont.truetype("fonts\BreeSerif_Reg.otf", self.font_size)
        self.font_px = self.font_size * self.font_size_to_px
        # 打开底版图片
        imageFile = self.imageFile
        self.im = Image.open(imageFile)

    def __readFile(self):
        self.data = xlrd.open_workbook('1.xlsx')

    def __printImage(self):
        table = self.data.sheets()[0]  # 通过索引顺序获取
        nrows = table.nrows

        # 在图片上添加文字 1
        draw = ImageDraw.Draw(self.im)
        print(self.im.size)
        height = self.im.size[1]
        height_num = int(height // self.font_px / 3 * 2)
        width_num = int(nrows // height_num)
        for i in range(width_num):
            x = 20 + i * 170
            for k in range(height_num):
                y = 20 + k * self.font_px * 3 / 2
                text = table.row_values(k + i * height_num)[0]
                draw.text((x, y), text, (255, 255, 255), font=self.font)

    def go(self):
        self.__createImage()
        self.__readFile()
        self.__printImage()
        draw = ImageDraw.Draw(self.im)
        # 保存
        self.im.save("target.png")

printWordImage = PrintWordImage("3235-106.jpg", "1.xlsx")
printWordImage.go()

