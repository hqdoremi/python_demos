# coding=utf-8
from bs4 import BeautifulSoup
import requests
import hashlib
from datetime import datetime
import os
from selenium import webdriver
import time
import re

bingImgDir = 'bingImgs'
bingUrl = 'https://cn.bing.com'


def parse_url_use_requests():
    strhtml = requests.get(bingUrl)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#bgImgProgLoad')[0]
    return bingUrl + data.get('data-ultra-definition-src')


def parse_url_use_selenuim():
    driver = webdriver.Chrome(executable_path="/Users/heq/chromedriver")
    driver.get('https://cn.bing.com/')
    try:
        time.sleep(2)
        element = driver.find_element_by_xpath('//*[@id="bgDiv"]')
        url = str(element.value_of_css_property('background-image'))
        # url("https://cn.bing.com/th?id=OHR.LimosaLimosa_ZH-CN8008396927_UHD.jpg&pid=hp&w=3840&h=2160&rs=1&c=4&r=0")
        url = re.compile("url\(\"(.*)\"\)").findall(url)[0]
        return url
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    finally:
        driver.quit()


if __name__ == '__main__':
    imgUrl = parse_url_use_requests()
    # url = parse_url_use_selenuim()
    md5 = hashlib.md5(imgUrl.encode('utf-8')).hexdigest()
    print('正在保存 md5 = %s url = %s ' % (md5, imgUrl))
    res = requests.get(imgUrl)
    os.makedirs(bingImgDir,exist_ok=True)
    # if not os.path.exists(bingImgDir):
    #     os.mkdir(bingImgDir)
    with open(bingImgDir + '/bing_' + str(datetime.now().date()) + '_' + md5 + '.jpeg', 'wb') as fp:
        for chunk in res.iter_content(10000):
            fp.write(chunk)
