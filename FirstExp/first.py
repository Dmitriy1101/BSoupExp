from bs4 import BeautifulSoup as BS
import requests, json


# загрузка страницы url в файл html
# url = 'https://sdelanounas.ru/blogs/'
# headers = {
#     'Accept' : '*/*',
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
# }
# req = requests.get(url, headers = headers)
# src = req.text
# print(src)
# with open('index.html', 'w', encoding="utf-8") as f:
#     f.write(src)

#Обработка файла html проба
# with open('index.html', 'r', encoding="utf-8") as f:
#     src = f.read()
# soup = BS(src, 'lxml')
# to_try = soup.find_all(class_ = 'title')
# for i in to_try:
#     print(i)
#     i_t = i.h2.text
#     i_h = i.a.get('href')
#     print(f'{i.div.a.text}===============>>{i_h}<<================={i_t}')

#Продолжим записав в json
# with open('index.html', 'r', encoding="utf-8") as f:
#     src = f.read()
# soup = BS(src, 'lxml')
# to_try = soup.find_all(class_ = 'title')
# data = {}
# for i in to_try:
#     i_text = i.h2.text
#     i_href = i.a.get('href')
#     i_tag = i.div.a.text
#     data[i_href] = [i_tag, i_text]
# with open('data.json', 'w', encoding="utf-8") as f:
#     # indent = 4 - это отступ, чтобы было не в строку, ensure_ascii = False - отключает экранирование символов
#     json.dump(data, f,  indent = 4, ensure_ascii = False)

#Далее считываем из Json
with open('data.json', encoding="utf-8") as f:
    jdata = json.load(f)
print(jdata)