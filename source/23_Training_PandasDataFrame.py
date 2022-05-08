# from pandas import DataFrame

# read excel을 위한 import
import pandas as pd

# Series가 1차원 데이터를 저장한다면, DataFrmae은 가로축, 세로축이 있는 2차원 데이터를 저장하는 자료구조
# 행열의 구조를 가짐

# 기본적인 정수 인덱스만 생성
# data = {"open" : [100, 200], "high": [110, 210]}
# df = DataFrame(data)
# print(df)

# DataFrame을 생성할 때 기본적인 정수 인덱스를 사용하지 않고 날짜를 인덱스로 지정한다.
# df2 = DataFrame(data, index=["2022-01-01", "2022-01-02"])
# print(df2)

# index= 를 사용하지 않고 set_index 함수를 호출하여 원래 있던 Column이름을 인덱스로 사용할수도 있다.
# data = {"date" : ["2022-01-01", "2022-01-02"], "open" : [100, 200], "high": [110, 210]}
# df3 = DataFrame(data)
# df3 = df3.set_index("date")
# print(df3)


# 엑셀에서 읽어오는 법
# df4 = pd.read_excel("Test.xlsx")
# print(df4)



# 펄어비스 주가 일별 시세 정보 DataFrame으로 받아오기
# read_html 함수는 html 코드안에 <table> 태그를 찾아야 수집이 가능함.
# 네이버 일별 시세의 웹페이지가 변경되어 read_html로 불러올수없음.. 브라우저가 아닐때 응답을 하지 않기때문에, request와 beautifulsoup을 이용하여 가져올것이다.

"""
변경되기전에는 이렇게 불러올 수 있었음
# pearlUrl = "https://finance.naver.com/item/sise_day.nhn?code=263750"
# df5 = pd.read_html(pearlUrl, encoding=str)
# print(df5[0])
"""

import requests
from bs4 import BeautifulSoup as bs

pearlUrl = "https://finance.naver.com/item/sise_day.nhn?code=263750"
# 브라우저인것을 알리기위해 헤더에 사파리 브라우저로 요청을 보냈다라고 요청
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

res = requests.get(pearlUrl, headers=headers)
html = bs(res.text, "lxml")

# <table> 태그 찾기
htmlTable = html.select("table")

table = pd.read_html(str(htmlTable))
# table[0]을 출력하면 NaN만 있는 행이 나오는데 이는 네이버의 HTML Table에 숨겨진 코드때문에 출력된다.
# dropna로 이런 결측값들이 있는 행이나 열 자체들을 제거할 수 있다. axis가 0일경우 행을 삭제하며, 1일 경우 열을 삭제한다.
print(table[0].dropna(axis=0))



# dataframe 인덱싱 슬라이싱
data = {"open": [730, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]} 
df = pd.DataFrame(data , index=["2022-01-01", "2022-01-02"])
# Dictionary가 key를 이용하여 값에 접근하는 것처럼 DataFrame의 열이름을 사용하여 값을 가져온다.
# 이때 가져온 값은 DataSeries이다.
print(df["open"])

# 열 데이터가 아닌 행 데이터를 가져오려면 dataframe의 loc 함수를 사용하여 행 인덱스를 전달하면 된다.
print(df.loc["2022-01-01"])

# 기본적으로 정의되는 행의 정수인덱스를 사용하여 값을 가져올 때는 iloc 함수를 사용해야 한다.
print(df.iloc[1])

# 인덱스를 리스트로 넣으면 여러개의 Series값을 가져올수도 있다.
print(df[["open", "high"]])
print(df.loc[["2022-01-01", "2022-01-02"]])
print(df.iloc[[0, 1]])



# DataFrame 추가하기
data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]} 
df = pd.DataFrame(data)

# 딕셔너리처럼 Series값을 대입하면 새로운 열 데이터를 만들 수 있다.
df["volume"] = pd.Series([300, 400]) 

# 새로운 행 데이터를 만들기 위해서는 loc를 이용하여 (iloc는 안된다) Series값을 대입하면 된다.
# 행 데이터의 행의 데이터 개수와 똑같은 개수의 데이터를 가진 Series 값이어야 한다.
df.loc[2] = (100, 200, 300, 400, 500)
print(df)



# 칼럼 시프트
# 비트 시프트를 생각하면 된다.
# 시리즈의 길이에 벗어난 요소는 삭제되며 빈 요소칸은 Nan으로 채워진다.

shiftTestSeries = pd.Series([100, 200, 300])
# 오른쪽으로 값을 시프트 한다.
shiftTestSeries2 = shiftTestSeries.shift(1)
print(shiftTestSeries2)
# 왼쪽으로 값을 시프트한다.
shiftTestSeries3 = shiftTestSeries.shift(-1)
print(shiftTestSeries3)