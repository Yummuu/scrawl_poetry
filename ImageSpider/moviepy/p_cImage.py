import MySQLdb
import requests
import time
import cv2 as cv
import random
import numpy as np
import math
from PIL import Image, ImageDraw,ImageFont
class MysqlModel():
    connect = None
    cursor = None
    def __init__(self):
        self.connect = MySQLdb.connect(
            host='localhost',
            db='liyulin',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True)
            # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        pass
    def getPoetryInfo(self, id_Int):
        self.cursor.execute(
            """ SELECT id,title,author,years FROM poetry WHERE id=%s """,
            (id_Int, )
        )
        return self.cursor.fetchone()
        pass
    def dbInsert(self, id_Int, title, author, description):
        self.cursor.execute(
            """INSERT INTO poetry_py (poetry_id, title, author, description) VALUES (%s, %s, %s, %s)""",
            (id_Int, title, author, description)
        )
        self.connect.commit()
        self.cursor = self.connect.cursor()
        pass

def paint_chinese_opencv(im, chinese, pos, color, fontsize):
    img_PIL = Image.fromarray(cv.cvtColor(im, cv.COLOR_BGR2RGB))
    font = ImageFont.truetype('./simsun.ttc',fontsize)
    fillColor = color # 颜色
    position = pos # 位置
    if not isinstance(chinese, str):
        chinese = chinese.decode('utf-8')
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, chinese, font=font, fill=fillColor)
    img = cv.cvtColor(np.asarray(img_PIL), cv.COLOR_RGB2BGR)
    return img

model = MysqlModel()
num = 1
# 标签格式　maskbox = [xl, yl, xr, yr]
maskbox = [0,0,208,208]
#透明度 
opt = 0.6
while num < 100:
    try:
        info = model.getPoetryInfo(num)
        # print(info)
        imgIndex = random.randint(1,48)
        fileName = "./canuse/pt ("+str(imgIndex)+").jpg"
        img = cv.imread(fileName)
        img_w = img.shape[0]
        img_h = img.shape[1]
        zeros = np.zeros((img.shape),dtype=np.uint8)
        maskbox = [math.ceil(img_h*0.2),math.ceil(img_w*0.2),math.ceil(img_h*0.8),math.ceil(img_w*0.8)]
        zeros_mask = cv.rectangle(zeros,(maskbox[0],maskbox[1]),(maskbox[2],maskbox[3]),color=(255,255,255),thickness=-1)
        #cv2.addWeighted 将原始图片与 mask 融合
        new_img = cv.addWeighted(img,1,zeros_mask,opt,0)
        fontsize = (maskbox[2]-maskbox[0])//20
        smallfontsize = (maskbox[2]-maskbox[0])//28
        # cv.imshow('pic title', img)
        # cv.waitKey(0)
        # cv.putText(new_img, info[1], (50, 150), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
        new_img = paint_chinese_opencv(new_img,info[1],((maskbox[0]+fontsize),(maskbox[1]+fontsize)),(0,0,1), fontsize)
        str2 = info[2]+"["+info[3]+"]"
        new_img = paint_chinese_opencv(new_img,str2,((maskbox[0]+fontsize),(maskbox[1]+fontsize*2+smallfontsize)),(0,0,1), smallfontsize)
        cv.imwrite('./poetry/id_'+str(num)+'.jpg', new_img)
        print(num)
        pass
    except Exception as e:
        raise
    else:
        pass
    finally:
        num += 1
        pass
    pass
