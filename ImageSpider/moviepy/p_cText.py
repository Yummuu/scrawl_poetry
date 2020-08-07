# -*- coding: utf-8 -*-
import MySQLdb
import re
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
            """ SELECT id,title,author,years,content FROM poetry WHERE id=%s """,
            (id_Int, )
        )
        return self.cursor.fetchone()
        pass

def textWritePoetryIn(fileName, poetry):
    fp=open('./text/'+str(fileName)+'.txt','w',encoding="utf-8")
    title = poetry[1]+'[1秒]'
    des = poetry[2]+'【'+poetry[3]+'】[1秒]'
    fp.write(title+'\n')
    fp.write(des+'\n')
    result = re.split('[,。；，.]', poetry[4])
    for line in result:
        if line=='\n':
            continue
        fp.write(str(line)+'[0.5秒]\n')
        pass
    fp.close()
    pass

model = MysqlModel()
num = 4890
fp1 = None
while num < 75132:
    try:
        info = model.getPoetryInfo(num)
        textWritePoetryIn('id_'+str(num), info)
        print('success id:'+str(num))
        pass
    except Exception as e:
        fp1 = open('error.txt','w',encoding="utf-8")
        fp1.write("error_id:"+str(num)+"\n")
        fp1.close()
        pass
    else:
        pass
    finally:
        num += 1
        pass
    pass