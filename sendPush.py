# coding=utf-8
from selenium import webdriver
import time
# http://t.hz.c.m.163.com/admin/jidian/send?t=1619345435068&title=12345&content=67890&deviceIds=qqqq&payload=eweqew
payload = {
    "showType": 0,
    "pushTime": "1606464024452",
    "pushtype": "doc",
    "id": "FSBR44C10529HGFU",
    "stickyTimes": 2,
    "content": "查看更多>>",
    "interest": "nba_push",
    "skipId": "FSBR44C10529HGFU",
    "type": "0",
    "skipType": "docid",
    "thread-id": "fold",
    "msgId": "91d7211696e645b49e261517a8b81b17",
    "title": "官宣！火箭国王交易正式完成，状元之子驰援哈登，高中场均16+9",
    "skip": "docid=FSBR44C10529HGFU",
    "boardid": ""
}
print(type(payload))
driver = webdriver.Chrome(executable_path="/Users/heq/chromedriver")  # 创建浏览器对象

driver.get(
    'http://t.hz.c.m.163.com/admin/login?openid.assoc_handle=%7BHMAC-SHA1%7D%7B5d301462%7D%7BasLLGQ%3D%3D%7D&openid.ax.mode=fetch_response&openid.claimed_id=https%3A%2F%2Flogin.netease.com%2Fopenid%2Fliupanwen%2F&openid.identity=https%3A%2F%2Flogin.netease.com%2Fopenid%2Fliupanwen%2F&openid.mode=id_res&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.op_endpoint=https%3A%2F%2Flogin.netease.com%2Fopenid%2F&openid.response_nonce=2019-07-18T06%3A40%3A34ZBgfq5L&openid.return_to=http%3A%2F%2Ft.hz.c.m.163.com%2Fadmin%2Flogin&openid.sig=bQnnG3L6YlNPL04AyJ321nhk3vw%3D&openid.signed=assoc_handle%2Cax.mode%2Cclaimed_id%2Cidentity%2Cmode%2Cns%2Cns.ax%2Cns.sreg%2Cop_endpoint%2Cresponse_nonce%2Creturn_to%2Csigned%2Csreg.email%2Csreg.fullname%2Csreg.nickname&openid.sreg.email=liupanwen%40corp.netease.com&openid.sreg.fullname=%E5%88%98%E6%94%80%E6%96%87&openid.sreg.nickname=liupanwen#/tool/batchsendpush')  # 打开网页

while True:
    pushType = input('''input push type : 
    quit
    doc
    pic
    ''')
    if pushType == 'quit':
        print('exit!!')
        driver.quit()
        break
    elif pushType == 'doc':
        driver.find_element_by_xpath('//*[@id="neatui-form-title"]').send_keys(('test'))
    else:
        print('invalid input!')
