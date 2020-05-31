import requests
from bs4 import BeautifulSoup

# headers에 있는 브라우저 정보들을 제대로 안 넣으면 보안문제로 정보를 모두 불러오지 않으려고 한다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200329', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

print(soup)

# 곡에 대한 정보가 모두 담겨있는 태그 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
songs = soup.select(
    '#body-content > div.newest-list > div > table > tbody > tr')
print(len(songs))  # 50개 (1페이지)

for song in songs:
    rank_raw = song.select_one('td.number')
    # decompse는 return값 없이 동작만 시키는 함수이기 때문에 chain(.)으로 쭉 연결시키면 작동하지 않음.
    rank_raw.span.decompose()
    rank = rank_raw.text.strip()

    title = song.select_one(
        'td.info > a.title.ellipsis').text.strip()  # 앞뒤 공백 삭제
    singer = song.select_one('td.info > a.artist.ellipsis').text

    print(rank, title, singer)
