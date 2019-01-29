import requests,json
from urllib.request import quote
import base64
def get_token(mobile):
    captcha_hash=validate_img(mobile)
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
    data={"mobile":mobile,"captcha_value":input('输入验证码：'),"captcha_hash":captcha_hash,"scf":"ms"}
    #登录的参数。
    req=requests.post(url, headers=headers, data=json.dumps(data))
    #token=json.loads(req.content)['validate_token']
    token=json.loads(req.content)['validate_token']
    print(req.status_code)
    print(req.text)
    if req.status_code!=200:
        return get_token(mobile)
    return token

def login(mobile):
    token = get_token(mobile)
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
    data = {'mobile': mobile, 'validate_code': input('输入手机验证码：'), 'validate_token': token, 'scf': 'ms'}

    print(data)
    # 登录的参数。
    session.post(url, headers=headers, data=json.dumps(data))
    return session

def find_foods(mobile):
    session=login(mobile)
    address="松鹤楼(观前店)"
    url = 'https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=wttdpcwn012n&keyword={0}&limit=20&type=nearby'.format(quote(address))
    res = session.get(url)
    json_value = json.loads(res.text)[0]
    print(json_value['geohash'])
    print(json_value['latitude'])
    print(json_value['longitude'])
    restaurant_url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={0}&latitude={1}&limit=24&longitude={2}&offset=0&terminal=web'.format(
    json_value['geohash'], json_value['latitude'], json_value['longitude'])
    resturant_request = session.get(restaurant_url)
    print(resturant_request.text)
    resturant_list=json.loads(resturant_request.text)
    for restaurant in resturant_list:
        print(restaurant['name'])
        print(restaurant['address'])
        print('===============================')
def validate_img(mobile):
    # 创建会话。
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://h5.ele.me',
        'referer': 'https://h5.ele.me/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url='https://h5.ele.me/restapi/eus/v3/captchas'
    data = {"captcha_str":mobile}
    req=requests.post(url, headers=headers, data=json.dumps(data))
    capture=json.loads(req.text)
    print(capture['captcha_hash'])
    print(capture['captcha_image'])
    codeImg_str = capture['captcha_image'].split(',')[1]
    print(codeImg_str)
    # 对图片请求,content取图片二进制数据值
    with open("code.jpg", "wb") as fh:
        fh.write(base64.b64decode(codeImg_str))

    return capture['captcha_hash']

if __name__ == '__main__':
    mobile = '17706210570'
    #validate_img(mobile)
    #login(mobile)
    find_foods(mobile)
    #get_token(mobile)
    #test()
