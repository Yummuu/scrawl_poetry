import MySQLdb
import requests
import time
from selenium import webdriver

class MysqlModel():
    connect = None
    cursor = None
    def __init__(self):
        self.connect = MySQLdb.connect(
            host='localhost',
            db='liyulin',
            user='root',
            passwd='liyulin',
            charset='utf8',
            use_unicode=True)
            # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        pass
    
    def updateYi(self, yi, id_Int):
        self.cursor.execute(
            """UPDATE poetry_v3 SET yi=%s WHERE id=%s""",
            (yi, id_Int, )
        )
        self.connect.commit()
        self.cursor = self.connect.cursor()
        pass

    def updateZhu(self, zhu, id_Int):
        self.cursor.execute(
            """UPDATE poetry_v3 SET zhu=%s WHERE id=%s""",
            (zhu, id_Int, )
        )
        self.connect.commit()
        self.cursor = self.connect.cursor()
        pass

    def updateDes(self, des, id_Int):
        self.cursor.execute(
            """UPDATE poetry_v3 SET description=%s WHERE id=%s""",
            (des, id_Int, )
        )
        self.connect.commit()
        self.cursor = self.connect.cursor()
        pass

    def getNextIdGuid(self, id_Int):
        self.cursor.execute(
            """ SELECT id_guid,link FROM poetry_v3 WHERE id=%s """,
            (id_Int, )
        )
        return self.cursor.fetchone()
        pass

model = MysqlModel()
driver = webdriver.Edge()
num = 3893

while num < 7934:
    try:
        item = model.getNextIdGuid(num)
        id_guid = item[0].replace('contson','')
        driver.get(item[1])
        time.sleep(1)
        driver.execute_script("OnYiwen('%s')"%id_guid)
        yi = driver.find_element_by_id('contson%s'%id_guid).get_attribute('innerHTML')
        # time.sleep(1)
        driver.execute_script("OnYiwen('%s')"%id_guid)
        # time.sleep(1)
        driver.execute_script("OnZhushi('%s')"%id_guid)
        zhu = driver.find_element_by_id('contson%s'%id_guid).get_attribute('innerHTML')
        # time.sleep(1)
        driver.execute_script("OnZhushi('%s')"%id_guid)
        driver.execute_script("OnShangxi('%s')"%id_guid)
        description = driver.find_element_by_id('contson%s'%id_guid).get_attribute('innerHTML')
        model.updateYi(yi,num)
        model.updateZhu(zhu,num)
        model.updateDes(description,num)
        pass
    except Exception as e:
        raise
    else:
        pass
    finally:
        num += 1
        pass
    pass

driver.quit()