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

id_name = input("please input id_name:")
#先微信登录
driver = webdriver.Firefox()
driver.get("https://www.ffkuaidu.com/")
time.sleep(20)
# 检查是否登录
# token = driver.execute_script('return localStorage.getItem("token");')
# is_login = driver.execute_script('return localStorage.getItem("is_login");')
# userId = driver.execute_script('return localStorage.getItem("userId");')
# print(token)
# print(is_login)
# print(userId)
#读取字幕
with open('./text/'+str(id_name)+'.txt', 'r', encoding='UTF-8') as f:
    lines = f.read()
    f.close()
print(lines)
copyText(lines)
driver.find_element_by_id("textarea").click()
#在网页输入Control+v模拟粘贴
driver.find_element_by_id('textarea').send_keys(Keys.CONTROL, 'v')
time.sleep(2)

first_handle = driver.current_window_handle
type_lists = ['pth','cp','yy']
type_name = ''
for t in type_lists:
    type_name = str(id_name)+"_"+str(t)
    if t=='pth':
        #选择普通话
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[3]/div[1]/div/ul/li[3]/div").click()
        time.sleep(2)
    elif t=='cp':
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[4]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[5]/div[1]/div/ul/li[1]/div").click()
        time.sleep(2)
    elif t=='yy':
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[1]/div[1]/div/ul/li[4]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[5]/div[1]/div/ul/li[3]/div").click()
        time.sleep(2)
    else:
    	continue

    if type_name=='':
        type_name = str(id_name)
        print('error')
    #语音合成
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]").click()
    time.sleep(20)
    #保存为Mp3--会点击出新页面
    driver.find_element_by_id("save_btn").click()
    time.sleep(3)

    #切换新页面
    w = driver.window_handles
    print(w)
    driver.switch_to.window(w[1])
    #下载
    #driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[4]/div[1]").click()
    mp3_url = driver.find_element_by_xpath("/html/body/div[2]/div/audio").get_attribute('src')
    print(mp3_url)
    downloadFile(mp3_url,r"D:/python/ImageDeal/mp3_v2/",str(type_name)+".mp3")
    time.sleep(5)
    #关闭当前页面
    driver.close()
    #切换到首页
    driver.switch_to.window(first_handle)
    time.sleep(2)
    pass

driver.quit()
