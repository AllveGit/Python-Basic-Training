import datetime
import requests
from bs4 import BeautifulSoup

# 펄어비스 주식정보
url = "https://finance.naver.com/item/main.naver?code=263750"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per")
tag = tags[0]
print(tag.text)

tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr:nth-child(2) > td > em")
for tag in tags:
    print(tag.text)

# 코빗 비트코인 정보
korbitBitcoinUrl = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw"
res = requests.get(korbitBitcoinUrl)

bitcoinJson = res.json()
print(bitcoinJson)
print(type(bitcoinJson))

date = datetime.datetime.fromtimestamp(bitcoinJson["timestamp"] / 1000)

print("비트코인 최종 체결가 : %s" % bitcoinJson["last"])
print("비트코인 최종 체결 시각 : %s" % date)