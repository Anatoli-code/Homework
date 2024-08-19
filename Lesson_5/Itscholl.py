import json
import pandas as pd
import requests
from collections import Counter
#Test
response = requests.get("https://belarusbank.by/api/news_info")
print(response.status_code)
api_text = json.loads(response.text)
last_news = api_text[-20:]
counter = Counter(last_news)
# for news in last_news:
    # print(news["name_ru"])
    # print(news["html_ru"])
    # print(news["start_date"])

#1 def
def news_func():
    response = requests.get("https://belarusbank.by/api/news_info")
    list_1 = []
    if response.status_code == 200:
        api_text = json.loads(response.text)
        last_news = api_text[:20]
        for news in last_news:
            new_dict = {
                'name_ru': news['name_ru'],
                # 'html_ru': news['html_ru'],
                'start_date': news['start_date']
            }
            list_1.append(new_dict)
    return list_1
# print(news_func())

# 2 def
def odd_func():
    new_list = []
    news = news_func()
    for i in news:
        # print(i['start_date'])
        if i['start_date'][-1] not in "02468":
            new_list.append(i)
            print(new_list)

print(odd_func())
# def 3.1
def dlina():
    new_list = []
    news = news_func()
    long = max(news, key=len)
    if long:
        new_list.append(long)
        print(new_list)

# print(dlina())

# def 3.2

#def 3.3

