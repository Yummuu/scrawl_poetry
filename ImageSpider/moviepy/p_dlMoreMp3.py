from selenium import webdriver
import time
import win32clipboard
from selenium.webdriver.common.keys import Keys
import os
import requests


#模拟文件复制粘贴
def copyText(Text):
    #打开粘贴板
    win32clipboard.OpenClipboard()
    #清空粘贴板
    win32clipboard.EmptyClipboard()
    #设置复制的内容为Text
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,Text)
    #关闭粘贴板线程
    win32clipboard.CloseClipboard()
    #打开粘贴板
    win32clipboard.OpenClipboard()
    #获取粘贴板内容，传给参数data
    # data=win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    #输出粘贴板内容
    # print(data)
    #需要关闭一下粘贴板线程
    win32clipboard.CloseClipboard()
    pass

#下载mp3
def downloadFile(mp3_url, save_url,file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('pagram is error')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        res = requests.get(mp3_url,stream=True)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name+' 成功下载！')
    except:
        print("程序错误")

id_name = None
base_url = "https://www.ffkuaidu.com/"
xpath_pth_1 = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[2]"
xpath_pth_2 = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[3]/div[1]/div/ul/li[3]/div"
xpath_cp_1 = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[4]"
xpath_cp_2 = "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[5]/div[1]/div/ul/li[1]/div"
xpath_yy_1 = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[4]'
xpath_yy_2 = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[5]/div[1]/div/ul/li[3]/div'
xpath_play = '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]'
xpath_stop = '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]'
xpath_audio = '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/audio'
type_lists = ['pth','cp','yy']

#先手动微信登录
driver = webdriver.Firefox()
driver.get(base_url)
time.sleep(20)
#手动微信登录end

num = 83
fp1 = None
fp2 = open('success.txt','w',encoding="utf-8")
while num < 500:
    try:
        id_name = "id_"+str(num)
        #读取字幕
        with open('./text_v2/'+str(id_name)+'.txt', 'r', encoding='UTF-8') as f:
            lines = f.read()
            f.close()
        copyText(lines)
        driver.find_element_by_id("textarea").clear()
        driver.find_element_by_id("textarea").click()
        #在网页输入Control+v模拟粘贴
        driver.find_element_by_id('textarea').send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        type_name = ''
        for t in type_lists:
            type_name = str(id_name)+"_"+str(t)
            if t=='pth':
                #选择普通话
                driver.find_element_by_xpath(xpath_pth_1).click()
                time.sleep(2)
                driver.find_element_by_xpath(xpath_pth_2).click()
                time.sleep(2)
            elif t=='cp':
                driver.find_element_by_xpath(xpath_cp_1).click()
                time.sleep(2)
                driver.find_element_by_xpath(xpath_cp_2).click()
                time.sleep(2)
            elif t=='yy':
                driver.find_element_by_xpath(xpath_yy_1).click()
                time.sleep(2)
                driver.find_element_by_xpath(xpath_yy_2).click()
                time.sleep(2)
            else:
                continue

            if type_name=='':
                type_name = str(id_name)
                continue
            #语音合成--播放按钮
            driver.find_element_by_xpath(xpath_play).click()
            time.sleep(20)
            #获取音频链接
            mp3_url = driver.find_element_by_xpath(xpath_audio).get_attribute('src')
            if mp3_url == base_url:
                time.sleep(20)
                mp3_url = driver.find_element_by_xpath(xpath_audio).get_attribute('src')
                pass
            mp3_url = None if mp3_url==base_url else mp3_url
            print(mp3_url)
            #下载
            downloadFile(mp3_url,r"D:/python/ImageDeal/mp3_v2/",str(type_name)+".mp3")
            fp2.write("mp3:"+str(type_name)+";url:"+str(mp3_url)+"\n")

            #有可能还在播放中-先暂停
            stop_btn = driver.find_element_by_xpath(xpath_stop)
            if stop_btn.is_displayed():
                stop_btn.click()
            time.sleep(2)
            pass

        pass   
    except Exception as e:
        fp1 = open('error.txt','w',encoding="utf-8")
        fp1.write("error_id:"+str(num)+',err:'+str(e)+"\n")
        fp1.close()
        pass
    else:
        pass
    finally:
        num += 1
        pass
    pass

fp2.close()
driver.quit()
