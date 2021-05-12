# coding=utf-8
# downloads every single xkcd comic

import requests, os, bs4

xkcdUrl = 'http://xkcd.com'
url = xkcdUrl
downloadDir = 'xkcdComics'
os.makedirs(downloadDir, exist_ok=True)
count = 0
while True:
    if url.endswith('#') or count >= 10:
        break
    print('Downloading page %s ......' % url)
    res = requests.get(url)
    # raise_for_status确保程序在下载失败时停止
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    comicElem = soup.select('#comic > img')
    if not comicElem:
        print('Could not find comic image!!')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s ......' % comicUrl)
        res = requests.get(comicUrl)
        # save image
        with open(os.path.join(downloadDir, os.path.basename(comicUrl)), 'wb') as fp:
            for chunk in res.iter_content(10000):
                fp.write(chunk)

        # previous
        preLink = soup.select('a[rel="prev"]')[0]
        url = xkcdUrl + preLink.get('href')
    print('Done!')
    count += 1
