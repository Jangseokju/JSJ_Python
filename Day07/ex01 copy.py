import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/news?oid=076&aid=0004126813"
html = requests.get(url)

print(html)

soup = BeautifulSoup(html.text, 'lxml')

h4 = soup.find('h4', class_='title')
print(h4)

'''
    <span class="area_text_title">
        <strong class ="_text">맨유 그만해!</strong>
    </span>
'''
h4=h4.get_text()
print(h4)