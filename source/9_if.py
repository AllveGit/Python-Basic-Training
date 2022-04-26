"""
===== 제어문 : if =====
"""

print("=" * 50)
print("Training_9. if")

# if 정의법
"""
# : 으로 문단을 구분한다.
# 무조건 한 문장마다 들여쓰기(Tab)가 필요하다. 같은 너비로..
# C++이나 C#처럼 {}로 감싸지 않는다.
"""

ifTest = True

if ifTest:
    print("Test : True")
else:
    print("Test : False")



# and, or, not
# C++이나 C#은 각각 &&, ||, !으로 나타내었다.

operTest1 = True
operTest2 = False

if operTest1 and operTest2:
    print("AND Test : True")
else:
    print("AND Test : False")

if operTest1 or operTest2:
    print("OR Test : True")
else:
    print("OR Test : False")

if not operTest1:
    print("NOT Test : True")
else: 
    print("NOT Test : False")



# in, not in
# 리스트, 튜플, 문자열, 딕셔너리, 집합 같은 컨테이너형 객체에 사용할 수 있는 명령어이다.

# in 은 이 객체에 찾는 요소가 있는지 참, 거짓을 리턴해주는 함수이다.
print(1 in [1, 2, 3])
# not in은 이 객체에 찾는 요소가 없는지 참, 거짓을 리턴해주는 함수이다.
print('j' not in "python")



# 조건문에 아무일도 안하고 넘어가게 설정하는 pass
# pass를 하면 그 조건문의 실행문단을 패스하고 넘어간다
passTest = [1, 2, 3]
if 1 in passTest:
    pass
else:
    print("네~")



# elif
# else if랑 똑같음
elifTest = [1, 2, 3]
if 4 in elifTest:
    print("if!!")
elif 1 in elifTest:
    print("elif!!")
else:
    print("else!!")


print("=" * 50)