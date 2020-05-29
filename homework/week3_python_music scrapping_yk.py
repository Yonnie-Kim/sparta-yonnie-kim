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
    rank = song.select_one('td.number').text.split('\n')[0]  # n계단 상승/하강 내용 삭제
    '''
    rank = song.select_one('td.number').span.decompose().text

    https://studyforus.com/innisfree/650714
    td.number 에서 text를 선택해오면 상승, 하강 등 텍스트가 따라와서, 숫자부분만 따오려고
    검색해서 decompose라는 함수를 찾긴 했는데.. 실행 시 None을 출력해서 에러가 발생하네요! 어떻게 고치면 될까요?
    '''
    title = song.select_one(
        'td.info > a.title.ellipsis').text.strip()  # 앞뒤 공백 삭제
    singer = song.select_one('td.info > a.artist.ellipsis').text

    print(rank, title, singer)
