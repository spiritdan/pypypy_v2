import requests,json
from urllib.request import quote
def translation():
    #添加请求头，避免被反爬虫。
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #url ='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #登录的网址。

    data={
        "i": "吃饭",
        "from": "zh-CHS",
        "to": "en",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    #登录的参数。
    req=requests.post(url, data=data)
    print(req.text)
    eng=json.loads(req.text)
    return eng

trans=translation()
