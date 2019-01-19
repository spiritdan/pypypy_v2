from selenium import  webdriver # 调用selenium模块、webdriver模块
from selenium.webdriver.chrome.options import Options # 调用Option模块
from bs4 import BeautifulSoup
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 声明浏览器对象
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒


comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 循环
    sweet = comment.find_element_by_tag_name('p') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论