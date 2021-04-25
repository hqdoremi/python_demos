import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.cntour.cn'
# 伪造ua
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.110 Safari/537.36'}
strhtml = requests.get(url, headers=headers)
# Beautiful Soup 选择最合适的解析器来解析这段文档，此处指定 lxml。解析后便将复杂的 HTML 文档转换成树形结构，并且每个节点都是 Python 对象
soup = BeautifulSoup(strhtml.text, 'lxml')

data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
# print("select data:"+data.__str__())
for item in data:
    result = {
        # 提取标签的正文用 get_text()
        'title': item.get_text(),
        'link': item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
    print(result)
