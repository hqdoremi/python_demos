# coding=utf-8
from selenium import webdriver
import time
import re
import requests
import hashlib
from datetime import datetime
import os

bingImgDir = 'bingImgs'
driver = webdriver.Chrome(executable_path="/Users/heq/chromedriver")


def download_img():
    driver.get('https://cn.bing.com/')
    try:
        time.sleep(2)
        element = driver.find_element_by_xpath('//*[@id="bgDiv"]')
        url = str(element.value_of_css_property('background-image'))
        # url("https://cn.bing.com/th?id=OHR.LimosaLimosa_ZH-CN8008396927_UHD.jpg&pid=hp&w=3840&h=2160&rs=1&c=4&r=0")
        url = re.compile("url\(\"(.*)\"\)").findall(url)[0]
        md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
        print('正在保存 md5 = %s url = %s ' % (md5, url))
        image = requests.get(url).content
        if not os.path.exists(bingImgDir):
            os.mkdir(bingImgDir)
        with open(bingImgDir + '/bing_' + md5 + '.jpeg', 'wb') as fp:
            fp.write(image)
    finally:
        driver.quit()


if __name__ == '__main__':
    download_img()
