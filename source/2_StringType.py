"""
===== 문자열 자료형 =====
"""

from dataclasses import replace


print("=" * 50)
print("Training_2. StringType")

# 파이썬 문자열 표현방식
s1 = "Hello"
s2 = 'Hello'
s3 = """
    H
    e
    l
    l
    o
    """
s4 = '''
    H
    e
    l
    l
    o
    '''

print(s1)
print(s2)
print(s3)
print(s4)

# s1은 작은따옴표(')를 문자열로 넣을 수 있음.
# s2는 큰따옴표(")를 문자열로 넣을 수 있음.
# s3는 s1과 똑같지만 여러줄을 한번에 문자열로 넣을 수 있음.
# s4는 s2와 똑같지만 여러줄을 한번에 문자열로 넣을 수 있음.
# 이스케이프(\) 문자를 사용해서 따옴표를 표시가능함.

# 파이썬 문자열 연산
a1 = "python"
a2 = " is fun!"

# 문자열을 더하면 python is fun이 나옴
print(a1 + a2)
# 문자열을 3번 곱하면 똑같은 문자열 3번이 나옴
print(a1 * 3)


# 문자열 길이 구하는 함수 len
print(len(a1))

# 문자열 인덱싱, c++의 문자열 배열처럼 첨자연산자([])로 인덱싱 가능, 파이썬도 숫자를 0부터 센다.
print(a1[4])
# 인덱스 번호에 -가 붙으면 뒤에서부터 인덱싱을 하게 된다. 즉, 원래 배열의 마지막 요소가 -1이 된다.
print(a1[-1])

# 문자열 슬라이싱, (:)을 기준으로 왼쪽이 시작인덱스, 오른쪽이 끝인덱스이며 이 인덱스에 포함된 문자열을 잘라 값을 리턴한다.
# 이 구문의 경우에는 0 <= index < 3 에 포함된 인덱스들만 출력한다.
print(a1[0:3])
# 끝 인덱스를 비워놓으면 시작 인덱스를 기준으로 끝 요소까지 자른다.
print(a1[1:])
# 시작 인덱스를 비워놓으면 처음요소부터 끝 인덱스까지 자른다.
print(a1[:4])
# 마찬가지로 슬라이싱에서도 -를 쓸수 있다.
print(a1[3:-1])

# 문자열 formatting, c++이랑 똑같은 구분자 사용
# 하나만 대입
fs1 = "I Learning %s." % a1
# 여러 개 대입
fs2 = "%s%s" % (a1, a2)

print(fs1)
print(fs2)

# 문자열 정렬
# 전체 길이가 16인 문자열에서 오른쪽 정렬, 나머지는 공백으로 채움
fs3 = "%16s" % a1
# 전체 길이가 16인 문자열에서 왼쪽 정렬, 나머지는 공백으로 채움
fs4 = "%-16s %s" % (a1, a2) 

print(fs3)
print(fs4)

# 소수점 표현
# 소수점 4자리까지 표현
fs5 = "%0.4f" % 3.42134234
# 전체길이가 10인 문자열에서 오른쪽 정렬후, 소수점 4자리까지 표현
fs6 = "%10.4f" % 3.42134234

print(fs5)
print(fs6) 

# format 함수를 사용한 formating
fs7 = "I Want {0} Gold".format(100)
fs8 = "I Want {0} Gold".format("Hundred")
fs9 = "I Want {0} Gold and {1} Gem".format(100, "Hundred")
fs10 = "I Want {Gold} Gold and {Gem} Gem".format(Gold=100, Gem=100)
fs11 = "I Want {0} Gold and {1} Gem and {Dia} Diamond".format(100, 100, Dia=200)

print(fs7)
print(fs8)
print(fs9)
print(fs10)
print(fs11)

# format 함수를 이용한 정렬
# 10길이의 문자열에서 왼쪽 정렬
fs12 = "{0:<10}".format("Hello")
# 10길이의 문자열에서 오른쪽 정렬
fs13 = "{0:>10}".format("Hello")
# 10길이의 문자열에서 가운데 정렬
fs14 = "{0:^10}".format("Hello")
# 10길이의 문자열에서 가운데 정렬을 하고 공백은 =로 채운다.
fs15 = "{0:=^10}".format("Hello")
# 10길이의 문자열에서 왼쪽 정렬을 하고 공백은 !로 채운다.
fs16 = "{0:!<10}".format("Hello")

print(fs12)
print(fs13)
print(fs14)
print(fs15)
print(fs16)

# format 함수를 이용한 소수점 표현
fs17 = "{0:0.4f}".format(3.42134234)
fs18 = "{0:10.4f}".format(3.42134234)

print(fs17)
print(fs18)

# format 함수를 이용한 { 또는 } 문자 표현
fs19 = "{{ and }}".format()

print(fs19)

# f 문자열 Formating (Python 3.6 부터)
fs20Name = "홍길동"
fs20Age = 22
fs20Per = 0.23435;
fs20 = f"나의 이름은 {fs20Name}입니다. 나이는 {fs20Age} 살입니다."
fs21 = f'내년이면 {fs20Age+1} 살입니다.'
# 길이가 10인 문자열에서 오른쪽 정렬
fs22 = f"{fs20Name:>10}"
fs23 = f"{fs20Name:=^10}"
fs24 = f"{fs20Per:10.4f}"

print(fs20)
print(fs21)
print(fs22)
print(fs23)
print(fs24)

# 문자 개수 세는 함수(count)
lenTestStr = "whatwhatwhatwhat"
wCount = lenTestStr.count('w')

print(wCount)

# 문자의 위치 인덱스 알려주는 함수(find, index)
# find는 찾으면 인덱스반환, 못찾으면 -1 리턴
findSuccessIdx = lenTestStr.find('a')
findFailIdx = lenTestStr.find('b')

print(findSuccessIdx)
print(findFailIdx)

# index는 찾으면 인덱스반환, 못찾으면 에러 발생
indexSuccessIdx = lenTestStr.index('a')

print(indexSuccessIdx)

# indexFailIdx = lenTestStr.index('b')

# print(indexFailIdx)

# 문자열 삽입해주는 함수 (join)
# abcd 각각 문자사이에 ,를 삽입한다.
joinTestStr = ",".join("abcd")

print(joinTestStr)

# 대/소문자 바꾸는 함수 (upper, lower)
upperTestStr = "hello"
lowerTestStr = "HELLO"

print(upperTestStr.upper())
print(lowerTestStr.lower())

# 공백 지우는 함수 (lstrip, rstrip, strip)
stripTestStr = "   striptest   "
# 왼쪽 공백 지우기
print(stripTestStr.lstrip())
# 오른쪽 공백 지우기
print(stripTestStr.rstrip())
# 양쪽 공백 지우기
print(stripTestStr.strip())

# 문자열 바꾸는 함수 (replace)
replaceTestStr = "My life is good"

print(replaceTestStr.replace("life", "project"))

# 문자열 나누는 함수 (split)
defaultSplitTestStr = "I want play game zelda"
wordSplitTestStr = "a:b:c:d"
sentSplitTestStr = "HeyWOWDoWOWyouWOWSomeWOWCoffee"

print(defaultSplitTestStr.split())
print(wordSplitTestStr.split(':'))
print(sentSplitTestStr.split("WOW"))

print("=" * 50)