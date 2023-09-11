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

#Далее считываем из Json и редактируем
# with open('data.json', encoding="utf-8") as f:
#     jdata = json.load(f)
# #print(jdata)
# wr = [',', ' ', '-',]
# for jd_href, jd_list in jdata.items():
#     for item in wr:
#         if item in jd_list[1]:
#             jd_list[1] = jd_list[1].replace(item, '_')
#     print(jd_list[1])

#
url_pikabu = 'https://pikabu.ru/'
headers = {
    'Accept' : '*/*',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

def get_page_to_file(url, headers):
    req = requests.get(url, headers = headers)
    src = req.text
    file = f'data/index_pikabu.html'
    with open(file, 'w', encoding="utf-8") as f:
        f.write(src)
    return file

def get_json_from_html(file):
    with open(file, 'r', encoding="utf-8") as f:
        src = f.read()
    soup = BS(src, 'lxml')
    div = soup.find_all(class_ = 'story')
    data = {}
    for i in div:
        auth = i.get("data-author-name")
        persoon_d = {}
        if auth:
            print(i.contents)
            persoon_d['title'] = i.h2.text
            persoon_d['rating'] = i.h2.text
            data[auth] = persoon_d

file = 'data/index_pikabu.html'
#file = get_page_to_file(url = url_pikabu, headers = headers)
jfile = get_json_from_html(file)