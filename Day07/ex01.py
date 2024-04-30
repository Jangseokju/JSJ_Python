import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=74977"
html = requests.get(url)

print(html)

soup = BeautifulSoup(html.text, 'lxml')

h3 = soup.find('h3', class_='h_movie')
print(h3)

span = soup.find('span', class_='area_text_title')
print(span)
'''
    <span class="area_text_title">
        <strong class ="_text">아바타: 물의 길</strong>
    </span>
'''
strong = span.find('strong', class_='_text')
print(strong)
'''
    <strong class ="_text">아바타: 물의 길</strong>
'''

movie_title = strong.get_text()
print(movie_title)
