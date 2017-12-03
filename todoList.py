# -*- coding: utf-8 -*-
import codecs

import xlrd
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

"""
Todolist
"""


class PrintWordImage:
    font_size_to_px = 1.3

    def __init__(self, imageFile, sourceFile, font_size=52, font="fonts\BreeSerif_Reg.otf"):
        self.font_size = font_size
        self.imageFile = imageFile
        self.sourceFile = sourceFile
        self.font = font

    def __createImage(self):
        # 设置字体，如果没有，也可以不设置
        self.font = ImageFont.truetype("fonts\simsun.ttc", self.font_size)
        self.font_px = self.font_size * self.font_size_to_px
        # 打开底版图片
        imageFile = self.imageFile
        self.im = Image.open(imageFile)

    def __readFile(self):
        self.data = open(self.sourceFile, 'r', encoding='utf-8')

    def __printImage(self):
        message = []
        for line in self.data:
            if line[0] == 't' or line[0] == '2':
                line = line.strip('\n').strip()
                message.append(line)

        # 在图片上添加文字 1
        draw = ImageDraw.Draw(self.im)
        length = len(message)
        print(length)
        for i in range(length):
            y = 90 + i * self.font_px * 3 / 2
            splitStr = message[i].split(' ')
            mes = splitStr[0].strip()
            color = (82, 82, 82)
            for str in splitStr[1:]:
                if str.strip() == 'important':
                    mes += ' !!! '
                    color = (238, 4, 108)
                if str.strip() == 'ok':
                    mes += '√✈'
                    color = (64, 167, 152)
                if str.strip() == 'error':
                    mes += '×'
                    color = (96, 125, 139)
            draw.text((20, y), mes, color, font=self.font)

    def go(self):
        self.__createImage()
        self.__readFile()
        self.__printImage()
        draw = ImageDraw.Draw(self.im)
        # 保存
        self.im.save("todoList.png")


printWordImage = PrintWordImage("1.jpg", "todolist.txt")
printWordImage.go()
