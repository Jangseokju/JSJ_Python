import os
import pandas as pd

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/covid.xls'

covid_data = pd.read_excel(input_file)

# pip install googlemaps
import googlemaps

# GCP 구글 클라우드 플랫폼
# 1. 구글 로그인
# 2. API KEY 발급

# API KEY 선언
gmaps_api_key = 'AIzaSyDa_9XcZixmykF2y95JyJCZravaIvqdPPU'

# 구글 맵 객체 생성
gmaps = googlemaps.Client(key=gmaps_api_key)

address = input('주소 : ')

g_result = gmaps.geocode(address, language='ko')

latitude = g_result[0]['geometry']['location']['lat']
longitude = g_result[0]['geometry']['location']['lng']

print('위도 : ', latitude)
print('경도 : ', longitude)

import folium

map = folium.Map(location=[latitude,longitude], zoom_start=8)
for index, row in covid_data.iterrows():
    name = row['의료기관명']
    address = row['주소']
    lat = 0
    lng = 0
    h_result = gmaps.geocode(address, language='ko')
    if h_result:
        lat = h_result[0]['geometry']['location']['lat']
        lng = h_result[0]['geometry']['location']['lng']

    print('의료기관명 : ', name)
    print('주소 : ', address)
    print('위도 : ', lat)
    print('경도 : ', lng)
    print('-----------------------------------------------------')

    if lat != 0 and lng !=0:
        pick = [lat, lng]
        # 마커 추가
        folium.Marker(pick, popup=address).add_to(map)

        # 라벨 추가
        style = "font-size : 20px; padding: 10px; text-align: center;"
        style += "width: 120px; height: 30px; line-height: 30px;"
        style += "background-color: white;"
        style += "transform: translate(-50%, 14px);"
        title = '<div style="{}"><b>{}</b><div>'.format(style, name)

        icon = folium.DivIcon(html=title)
        label = folium.Marker(pick, icon=icon)
        label.add_to(map)


map.save(path + "/covid.html")

import webbrowser
webbrowser.open(path + "/covid.html")