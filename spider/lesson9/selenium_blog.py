from selenium import  webdriver # 调用selenium模块、webdriver模块
from selenium.webdriver.chrome.options import Options # 调用Option模块
from bs4 import BeautifulSoup
import time

chrome_options = Options() # 实例化Option对象
driver = webdriver.Chrome()
#chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
#driver = webdriver.Chrome(options = chrome_options) # 声明浏览器对象
#chrome_options = Options() # 实例化Option对象
#chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
#driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器

driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php') # 访问页面
time.sleep(2)

user=driver.find_element_by_id('user_login') # 根据类名找到【点击加载更多】
user.send_keys('spiderman')

user=driver.find_element_by_id('user_pass') # 根据类名找到【点击加载更多】
user.send_keys('crawler334566')

button = driver.find_element_by_id('wp-submit') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

driver.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_03/') # 访问页面
time.sleep(2)

comment = driver.find_element_by_id('comment')
comment.send_keys('人人都是selenium俠')

btn_submit = driver.find_element_by_id('submit')
btn_submit.click() # 点击


driver.close()
