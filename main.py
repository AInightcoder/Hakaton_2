import requests
from run import a_title_link, title_name_data, img_data_links
from bs4 import BeautifulSoup
import json

# empty dict o'zgaruvchi ochish
data_dict = {}

# example uchun 10ta linkdan data
text_data = []
print("Ma'lumot yozish boshlandi......")
for url in a_title_link[:10]:
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', class_='default__section border')
    text_data.append(data.text)

# dict o'zgaruvchisiga ma'lumotlarni qo'shish
for i in range(len(text_data)):
    if url is not None and img_data_links[i] is not None:
       data_dict[title_name_data[i]] = [url+img_data_links[i], text_data[i]]

# dict fileni jsonga o'zgartirish
json_data = json.dumps(data_dict, ensure_ascii=False, indent=6)


# json fileni yozish
with open('jsondata.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

    print('Jaroayon tugadi.....')