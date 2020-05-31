import requests
'''
r : requests.get해서 데이터를 갖고오는데, 얘가 json형식의 데이터가 아닌거지.
r.jason() 해서 r변수에 넣어둔 데이터를 json화 하는것. 이게 javascript에서의 response랑 비슷하다고 보면 됨. 이제 rjason에서부터 데이터를 뽑아오면 되는 것!
'''

r = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']
for gu in gus:
    if gu['IDEX_MVL'] < 70:
        print(gu['MSRSTE_NM'], gu['IDEX_MVL'])
