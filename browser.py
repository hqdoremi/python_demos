# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/heq/chromedriver")  # 创建浏览器对象

driver.get('https://www.baidu.com/')  # 打开网页
# driver.maximize_window()   #最大化窗口
time.sleep(2)  # 加载等待
driver.set_window_size(1400, 800)

# 1.定位一组元素
elements = driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')

# 2.循环遍历
for t in elements:
    print(t.text)
    # element = driver.find_element_by_link_text(t.text)
    # element.click()
    # time.sleep(3)

driver.find_element_by_id('kw').send_keys("小米")
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)

time.sleep(5)
driver.quit()
