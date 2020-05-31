import requests
from pprint import pprint
pi
r = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print(rjson['RealtimeCityAir']['row'][0]['NO2'])

# 모든 구의 IDEX_MVL 값 찍기

gus = rjson['RealtimeCityAir']['row']
pprint(gus)

for gu in gus:
    print(gu["MSRSTE_NM"], gu["IDEX_MVL"])

# 미세먼지 수치가 100 이하인 경우에만 프린트

for gu in gus:
    gu_name = gu["MSRSTE_NM"]
    gu_mise = gu["IDEX_MVL"]
    if gu_mise <= 100:
        print(gu_name, gu_mise)
