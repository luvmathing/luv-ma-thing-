
# 순위 제목 가수

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.nbshi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20220301',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# rank #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# title #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# artist #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rank = music.select_one('td.number').text[0:2].strip()
    title = music.select_one('a.title.ellipsis').text.strip()
    artist = music.select_one('a.artist.ellipsis').text

    print(rank, title, artist)