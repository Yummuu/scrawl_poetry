import MySQLdb
import requests
import time
import re
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
    def updateInfo(self, description,content, id_Int):
        self.cursor.execute(
            """UPDATE poetry_author_detail SET description=%s,content=%s WHERE id=%s""",
            (description, content, id_Int, )
        )
        self.connect.commit()
        self.cursor = self.connect.cursor()
        pass

    def getLink(self, id_Int):
        self.cursor.execute(
            """ SELECT id,link FROM poetry_author_detail WHERE id=%s """,
            (id_Int, )
        )
        return self.cursor.fetchone()
        pass

model = MysqlModel()
driver = webdriver.Edge()
num = 1096

while num < 1312:
    try:
        item = model.getLink(num)
        if item is None:
            continue
        id_Int = item[0]
        driver.get(item[1])
        source = driver.find_elements_by_xpath("//div[@class='main3']/div[@class='left']/div[2]/div[@class='cont']/p[@class='source']/a")
        if len(source)==2:
            aLink = source[1].get_attribute('href')
        else:
            continue
        time.sleep(1)
        driver.get(aLink)
        description = driver.find_element_by_css_selector("div.main3 div.left textarea").get_attribute('value')
        description = description.replace(aLink,'')
        #获取content
        alle = driver.find_elements_by_xpath("//div[@class='main3']/div[@class='left']/div[starts-with(@id,'fanyi')]/div[@class='contyishang']/div/a")
        pattern = r'ziliaoShow'
        hasContent = 0
        for aItem in alle:
            jsStr = aItem.get_attribute('href').replace('javascript:','')
            if re.match(pattern,jsStr):
                driver.execute_script(jsStr)
                hasContent+=1
            pass
        time.sleep(1)
        content = ''
        if hasContent>0:
            allInfo = driver.find_elements_by_xpath("//div[@class='main3']/div[@class='left']/div[starts-with(@id,'fanyiquan')]/div[@class='contyishang']/p")
            for info in allInfo:
                infoStr = info.get_attribute('outerHTML')
                content += infoStr.replace(aLink,'#')
                pass
        model.updateInfo(description,content,id_Int)
        time.sleep(1)
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