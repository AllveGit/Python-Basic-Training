from pandas import Series

# 리스트를 Series로 변환하면 index-value 형식으로 바뀜
# Series() 에서 index= 인덱스로 할 리스트도 정할 수 있음. 0부터 시작하는 정수 인덱스도 추가로 가지며, 인덱스 리스트를 정하지 않으면 이것이 기본으로 쓰임

# 정수 인덱스를 가지는 Series
data = [100, 200, 300, 400]
s = Series(data)
print(type(s))
print(s)

# 날짜를 인덱스로 가지는 Series
date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
xrp_close = [512, 508, 512, 507, 500] 
xrpSeries = Series(xrp_close, index=date)
print(xrpSeries)
# 정수 인덱스도 내부적으로 쓰이기에 이런식으로 가능
print(xrpSeries[0])
# 일반 인덱스 탐색
print(xrpSeries['2018-08-01'])
# 인덱스들 출력
print(xrpSeries.index)
# 값들 출력
print(xrpSeries.values)

# Series는 한번에 여러 요소를 가져오는 인덱싱도 가능하다.
print(xrpSeries[['2018-08-02', '2018-08-04']])
# Series도 슬라이싱이 가능하다.
print(xrpSeries['2018-08-01': '2018-08-03'])
print(xrpSeries[1:3])

# Series에 값 추가하는법은 딕셔너리와 동일
xrpSeries['2018-08-06'] = 200
print(xrpSeries)

# Series에 값을 삭제하는법은 series의 함수 drop을 이용한다.
# drop을해도 원본객체는 유지되고 새로운 series를 리턴하므로 값을 완전히 삭제시킬거면 대입해야한다.
xrpSeries = xrpSeries.drop('2018-08-06')
print(xrpSeries)

# Series 객체는 사칙연산이 가능하다.
# Series 객체에 사칙연산을 하면 저장된 모든 '값' 에 연산이 된다.
print(s + 10)
print(s - 10)
print(s * 10)
print(s / 10)