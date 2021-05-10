# coding=utf-8
from bs4 import BeautifulSoup
import requests
import hashlib
from datetime import datetime
import os

bingImgDir = 'bingImgs'
bingUrl = 'https://cn.bing.com'


def download_img():
    strhtml = requests.get(bingUrl)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#bgImgProgLoad')[0]
    url = bingUrl + data.get('data-ultra-definition-src')
    md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
    print('正在保存 md5 = %s url = %s ' % (md5, url))
    image = requests.get(url).content
    if not os.path.exists(bingImgDir):
        os.mkdir(bingImgDir)
    with open(bingImgDir + '/bing_' + str(datetime.now().date()) + '_' + md5 + '.jpeg', 'wb') as fp:
        fp.write(image)


if __name__ == '__main__':
    download_img()
