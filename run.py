import requests
from bs4 import BeautifulSoup

url = "https://daryo.uz"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

img_links = soup.find_all('div', class_='article__pic')
title_names = soup.find_all('div', class_='article__link-title')
title_link = soup.find_all('a', class_='article__link')


img_data_links = []
title_name_data = []
a_title_link =[]



for line in img_links: 
   img_data_links.append(line.img.get('src'))

   

for line in title_names[:-2]:
   title_name_data.append(line.text)
   

for line in title_link[:-2]:
   if url is not None and line.get('href') is not None:
   
        a_title_link.append(url+line.get('href'))  



   
