import requests
import json
import re
import time
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.cls.cn/api/sw?app=CailianpressWeb&os=web&sv=7.7.5&sign=bf0f367462d8cd70917ba5eab3853bce'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"}
    data = {"type": "telegram", "keyword": "你需要知道的隔夜全球要闻", "page": 0, "rn": 20, "os": "web", "sv": "7.7.5",
            "app": "CailianpressWeb"}
    response = requests.post(url=url, headers=headers, data=data)
    news = json.loads(response.text)['data']['telegram']['data'][0]['descr']
    timeStamp = json.loads(response.text)['data']['telegram']['data'][0]['time']
    timeArray = time.localtime(timeStamp)
    formatTime = time.strftime("%Y%m%d", timeArray)
    # news = re.sub(r'(\d+、)', r'\n\1', news)
    news = re.split(r'\d+、', news)
    title = ''.join(etree.HTML(news[0]).xpath('//text()'))[1:-2]
    title_wek = title[:2]  

    # print(title)
    # print(title_wek)
    # print(news)
    param = {
            #  "title": f"{formatTime} {title}",
             "title": f"{formatTime} {title_wek}",
             "content": f"{'<br>&#9728;'.join(news)}",
            # "content": f"{'6'}",
             "template": "html",
             "channel": "wechat",
             "token": "c9f9ea9f28434ff9a0139c349d0358dd",
             "topic": "lys2024",
             }
    requests.post(url="https://www.pushplus.plus/send", headers=headers, data=param)
