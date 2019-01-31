import bs4,requests
url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-3'
response=requests.get(url)
bs = bs4.BeautifulSoup(response.text, 'html.parser')
book_list=bs.select('.bang_list li')
print(book_list)
for book in book_list:
    item = {}
    item['num'] = book.find('div', class_='list_num').text.strip()
    item['name'] = book.find('div', class_='name').text.strip()
    # item['star'] = book.find('div',class_='star').text.strip()
    publisher_infos = book.find_all('div', class_='publisher_info')
    publisher_info = []
    for i in publisher_infos:
        publisher_info.append(i.text.strip())
    item['publisher_info'] = '\n'.join(publisher_info)
    item['price'] = book.find('div', class_='price').text.strip()
    print(item)