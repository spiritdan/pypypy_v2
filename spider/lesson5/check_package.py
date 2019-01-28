import requests, json


def auto_check(code):
    url = 'https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + code
    # url='https://www.kuaidi100.com/autonumber/autoComNum'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.kuaidi100.com',
        'Origin': 'https://www.kuaidi100.com',
        'Referer': 'https://www.kuaidi100.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'resultv2': 1,
        'text': code
    }
    req = requests.get(url, headers=headers)
    return req.content


def check_package_info(code, company):
    url = 'https://www.kuaidi100.com/query?type={0}&postid={1}'.format(company, code)
    print(url)
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Host':'www.kuaidi100.com',
        'Referer':'https://www.kuaidi100.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    req = requests.get(url, headers=headers)
    #print(req.content)
    return json.loads(req.content)


if __name__ == '__main__':
    code = '3832310001987'
    com_code = json.loads(auto_check(code))
    #print(com_code['auto'])
    for com in com_code['auto']:
        company = com['comCode']
        package_info=check_package_info(code, company)
        #package_info=check_package_info(code, 'zhongtong')
        #print(package_info['data'])
        if not package_info['data']:
            continue
        for info in package_info['data']:
            print(info['time'])
            print(info['context'])
            print(info['location'])
            print('============================')