from selenium import  webdriver # 调用selenium模块、webdriver模块
from selenium.webdriver.chrome.options import Options # 调用Option模块
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome设置为无头模式
driver = webdriver.Chrome(options = chrome_options) # 声明浏览器对象
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待两秒

label = driver.find_element_by_class_name('teacher') # 根据类名找到元素
print(type(label)) # 打印label的数据类型
print(label.get_attribute('type')) # 获取type这个属性的值