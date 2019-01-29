from selenium import  webdriver
import time
import bs4

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(2)

content = driver.find_elements_by_class_name('content')
print('==============方法一=======================')
print(content[0].text)
print(content[1].text)
print('==============方法二=======================')


page_source=driver.page_source
#print(page_source)
bs=bs4.BeautifulSoup(page_source,'html.parser')
content=bs.find_all(class_='content')
print(content[0].text.strip())
print(content[1].text.strip())

driver.close()