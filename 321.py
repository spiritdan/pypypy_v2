import requests, random, bs4,csv,openpyxl,time

def get_movie():
    movie_list = []
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
        res = requests.get(url)
        #print(res.text)
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view").select('li')
        for titles in bs:
            num = titles.find('em', class_="").text
            title = titles.find('span', class_="title").text
            comment = titles.find('span', class_="rating_num").text
            url_movie = titles.find('a')['href']

            if titles.find('span', class_="inq") != None:
                tes = titles.find('span', class_="inq").text
                print(num + '.' + title + '——' + comment  + '\n' + url_movie)
                movie_list.append([num,title,comment ,url_movie])
            else:
                print(num + '.' + title + '——' + comment +'\n' + url_movie)
                movie_list.append([num, title, comment, url_movie])
        time.sleep(1)
    return movie_list

def w_csv():
    csv_file = open('demo.csv', 'w', newline='')
    writer=csv.writer(csv_file)
    movie_list=get_movie()
    print(movie_list)
    writer.writerow(['编号','标题','评分','链接'])
    for movie in movie_list:
        print(movie)
        writer.writerow(movie)
    csv_file.close()
def w_csv():
    csv_file = open('demo.csv', 'w', newline='')
    writer=csv.writer(csv_file)
    movie_list=get_movie()
    print(movie_list)
    writer.writerow(['编号','标题','评分','链接'])
    for movie in movie_list:
        print(movie)
        writer.writerow(movie)
    csv_file.close()

def w_xls():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '电影列表'
    sheet['A1'] = '编号'
    sheet['B1'] = '标题'
    sheet['C1'] = '评分'
    sheet['D1'] = '链接'
    movie_list = get_movie()
    for i in movie_list:
        sheet.append(i)
    wb.save('Movie.xlsx')
w_csv()
w_xls()