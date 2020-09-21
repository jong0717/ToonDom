import requests
from bs4 import BeautifulSoup
import json
import re


list_toon = []
  

# 에피소드
genre = 'episode'

URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/genre.nhn?genre=' + genre

response = requests.get(URL_TOTAL_LIST)

soup = BeautifulSoup(response.text, 'html.parser')

class_list = soup.select('ul.img_list')
class_list = class_list[0].select('li')

for a in class_list:
    art = a.find('div', attrs={'class':'thumb'})
    ratings = a.find('div', attrs={'class': 'rating_type'})
    rating_text = float(ratings.strong.get_text('a'))
    a_href = 'https://comic.naver.com' + art.a.get('href') # a['href']
    a_id = int(a_href.split('titleId=')[1])
    a_text = art.a.get('title')
    genres = ""
    p = ""
    
    # 여기서 웹툰 내부로 들어감
    response2 = requests.get(a_href)
    soup = BeautifulSoup(response2.text, 'html.parser')
    class_webtoon = soup.select('div.detail')
    class_thumb = soup.select('div.thumb')
    a_img = class_thumb[0].a.img.get('src')
    
    
    for tag in class_webtoon:
        artists = tag.find('span', attrs={'class':'wrt_nm'})
        artists_temp = artists.get_text('span').split('\t')[-1]
        artists_text = re.split(' / |,', artists_temp)

        if tag.select('span.genre'):
            genres = str(tag.select('span.genre')[0]).split('<span class="genre">')[1].split('</span>')[0]
            genres = genres.split(", ")

        # class 없는 p 태그만
        if tag.find_all('p', attrs={'class':''}):
            p = str(tag.find_all('p', attrs={'class':''})[0]).split('<p>')[1].split('</p>')[0]

    
    result = {'origin_id': a_id, 'title': a_text,'description':p, 'genres':genres, 'artists': artists_text, 'rating': rating_text, 'link': a_href, 'thumb_img': a_img, 'distinct': 1}
    list_toon.append(result)       

    
    
# 옴니버스
genre = 'omnibus'

URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/genre.nhn?genre=' + genre

response = requests.get(URL_TOTAL_LIST)

soup = BeautifulSoup(response.text, 'html.parser')

class_list = soup.select('ul.img_list')
class_list = class_list[0].select('li')

for a in class_list:
    art = a.find('div', attrs={'class':'thumb'})
    ratings = a.find('div', attrs={'class': 'rating_type'})
    rating_text = float(ratings.strong.get_text('a'))
    a_href = 'https://comic.naver.com' + art.a.get('href') # a['href']
    a_id = int(a_href.split('titleId=')[1])
    a_text = art.a.get('title')
    genres = ""
    p = ""
    
    # 여기서 웹툰 내부로 들어감
    response2 = requests.get(a_href)
    soup = BeautifulSoup(response2.text, 'html.parser')
    class_webtoon = soup.select('div.detail')
    class_thumb = soup.select('div.thumb')
    a_img = class_thumb[0].a.img.get('src')
    
    
    for tag in class_webtoon:
        artists = tag.find('span', attrs={'class':'wrt_nm'})
        artists_temp = artists.get_text('span').split('\t')[-1]
        artists_text = re.split(' / |,', artists_temp)
        
        if tag.select('span.genre'):
            genres = str(tag.select('span.genre')[0]).split('<span class="genre">')[1].split('</span>')[0]
            genres = genres.split(", ")

        # class 없는 p 태그만
        if tag.find_all('p', attrs={'class':''}):
            p = str(tag.find_all('p', attrs={'class':''})[0]).split('<p>')[1].split('</p>')[0]

    
    result = {'origin_id': a_id, 'title': a_text,'description':p, 'genres':genres, 'artists': artists_text, 'rating': rating_text, 'link': a_href, 'thumb_img': a_img, 'distinct': 1}
    list_toon.append(result)   
    
    
    

# 스토리
genre = 'story'

URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/genre.nhn?genre=' + genre

response = requests.get(URL_TOTAL_LIST)

soup = BeautifulSoup(response.text, 'html.parser')

class_list = soup.select('ul.img_list')
class_list = class_list[0].select('li')

for a in class_list:
    art = a.find('div', attrs={'class':'thumb'})
    ratings = a.find('div', attrs={'class': 'rating_type'})
    rating_text = float(ratings.strong.get_text('a'))
    a_href = 'https://comic.naver.com' + art.a.get('href') # a['href']
    a_id = int(a_href.split('titleId=')[1])
    a_text = art.a.get('title')
    genres = ""
    p = ""
    
    # 여기서 웹툰 내부로 들어감
    response2 = requests.get(a_href)
    soup = BeautifulSoup(response2.text, 'html.parser')
    class_webtoon = soup.select('div.detail')
    class_thumb = soup.select('div.thumb')
    a_img = class_thumb[0].a.img.get('src')
    
    
    for tag in class_webtoon:
        artists = tag.find('span', attrs={'class':'wrt_nm'})
        artists_temp = artists.get_text('span').split('\t')[-1]
        artists_text = re.split(' / |,', artists_temp)
        
        if tag.select('span.genre'):
            genres = str(tag.select('span.genre')[0]).split('<span class="genre">')[1].split('</span>')[0]
            genres = genres.split(", ")

        # class 없는 p 태그만
        if tag.find_all('p', attrs={'class':''}):
            p = str(tag.find_all('p', attrs={'class':''})[0]).split('<p>')[1].split('</p>')[0]

    
    result = {'origin_id': a_id, 'title': a_text,'description':p, 'genres':genres, 'artists': artists_text, 'rating': rating_text, 'link': a_href, 'thumb_img': a_img, 'distinct': 1}
    list_toon.append(result)    
    

print(list_toon)    
    
with open('naver_webtoon.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(list_toon, ensure_ascii=False))