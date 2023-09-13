from bs4 import BeautifulSoup as BS
import requests, json, csv, datetime, time, random


url_pikabu = 'https://pikabu.ru/'
headers = {
    'Accept' : '*/*',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
path_file = 'data/pikabu'

def get__data_string():
    return datetime.datetime.now().strftime('%m_%d_%Y_%Hh%Mm%Ss')


def get_text(text):
    wr = ['\u2060', '\n', '\t',]
    for item in wr:
        if item in text:
            text = text.replace(item, '')
    return text

def get_page_to_file(url, headers):
    req = requests.get(url, headers = headers)
    src = req.text
    file = f'{path_file}_index.html'
    with open(file, 'w', encoding="utf-8") as f:
        f.write(src)
    return file

def get_data_from_html():
    file = f'{path_file}_index.html'
    with open(file, 'r', encoding="utf-8") as f:
        src = f.read()
    soup = BS(src, 'lxml')
    div = soup.find_all(class_ = 'story')
    data = {}
    for i in div:
        auth = i.get("data-author-name")
        persoon_d = {}
        if auth:
            persoon_d['author'] = auth
            persoon_d['title'] = get_text(i.h2.text.strip())
            persoon_d['rating'] = i.find(class_ = 'story__rating-count').text
            persoon_d['href'] = i.h2.a.get('href')
            data[i.get('data-story-id')] = persoon_d
    return data

def put_json(data):
    with open(f'{path_file}_data.json', encoding="utf-8") as f:
        jdata = json.load(f)
    jdata.update(data)
    with open(f'{path_file}_data.json', 'w', encoding="utf-8") as f:
        json.dump(jdata, f,  indent = 4, ensure_ascii = False)
        
def put_table(data):
    for item, idata in data.items():
        inp_data = [item]
        [inp_data.append(idata.get(i)) for i in idata]
        with open(f'{path_file}_data.csv', 'a', encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(inp_data)

def crete_datafiles():
    names = ['post_id', 'author', 'title', 'rating', 'href']
    with open(f'{path_file}_data.csv', 'w', encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(names)
    with open(f'{path_file}_data.json', 'w', encoding="utf-8") as f:
        json.dump({}, f,  indent = 4, ensure_ascii = False)
            
def main():
    file = f'{path_file}_index.html'
    crete_datafiles()
    for i in range(1,8):
        url_now = f'{url_pikabu}?page={i}'
        print(url_now)
        get_page_to_file(url = url_now, headers = headers)
        new_data = get_data_from_html()
        put_table(new_data)
        put_json(new_data)
        print(f'Итерация {i}')
        time.sleep(random.randint(3,6))
    print('compleate')
    
    
        
if __name__ == '__main__':
    main()