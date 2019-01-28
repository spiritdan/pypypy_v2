import requests,json
from urllib.request import quote
def get_token(mobile):
    #添加请求头，避免被反爬虫。
    url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
    #登录的网址。
    headers = {
        'authority': 'h5.ele.me',
        'method': 'POST',
        'path': '/restapi/eus/login/login_by_mobile',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '144',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://h5.ele.me',
        'referer': 'https://h5.ele.me/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    data={"mobile":mobile,"captcha_value":"","captcha_hash":"","scf":"ms"}
    #登录的参数。
    req=requests.post(url, headers=headers, data=json.dumps(data))
    #token=json.loads(req.content)['validate_token']
    token=json.loads(req.content)
    print(req.status_code)
    return token

def login(mobile):
    token=get_token(mobile)
    session = requests.session()
    # 创建会话。
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '144',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://h5.ele.me',
        'referer': 'https://h5.ele.me/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # 添加请求头，避免被反爬虫。
    url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    # 登录的网址。
    data={'mobile':mobile,'validate_code':input('输入验证码：'),'validate_token':token,'scf':'ms'}
    # 登录的参数。
    session.post(url, headers=headers, data=json.dumps(data))
    # 在会话下，用post发起登录请求。
    return session
def find_foods():
    address="松鹤楼(观前店)"
    name_list=[]
    mobile=input('输入手机号码：')
    session=login(mobile)
    url = 'https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=wttdpcwn012n&keyword={0}&limit=20&type=nearby'.format(quote(address))
    res = session.get(url)
    json_value = json.loads(res.text)
    for i in json_value:
        i['address'] = '苏州市观前街太监弄旁边的小路进去左转'
        name_list.append(i['name'])
def test():
    address="松鹤楼(观前店)"
    url = 'https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=wttdpcwn012n&keyword={0}&limit=20&type=nearby'.format(quote(address))
    res = requests.get(url)
    json_value = json.loads(res.text)[0]
    print(json_value['geohash'])
    print(json_value['latitude'])
    print(json_value['longitude'])
    restaurant_url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={0}&latitude={1}&limit=24&longitude={2}&offset=0&terminal=web'.format(json_value['geohash'],json_value['latitude'],json_value['longitude'])
    resturant_request=requests.get(restaurant_url)
    print(resturant_request.content)
if __name__ == '__main__':


    #mobile='18068426375'
    #get_token(mobile)
    test()
