"""
===== 부울 자료형 =====
"""

print("=" * 50)
print("Training_7. BoolType")

# 부울 자료형은 항상 True, False 값만 가진다. (무조건 첫 문자만 대문자이어야 한다.)
# 조건문의 리턴값으로도 사용이 된다.

# 부울 자료형 정의법
boolTest1 = True
boolTest2 = False
print(type(boolTest1))
print(boolTest1)
print(type(boolTest2))
print(boolTest2)



# 자료형의 참과 거짓
"""
# 문자열 : 비워져있으면 거짓, 문자 하나라도 채워져있으면 참
# 리스트, 튜플, 딕셔너리 : 비워져있으면 거짓, 요소 하나라도 채워져있으면 참
# 1 : 참
# 0 : 거짓
# None : 거짓
"""

# 그래서 아래와 같은 구문이 가능하다.
# typeReturnTest에 pop을 하다보면 요소가 비워질것이며 비워진 리스트는 거짓이 리턴되기에 while문이 종료된다.
typeReturnTest = [1,2,3,4]
while typeReturnTest:
    print(typeReturnTest.pop())



# 부울 변환
boolConvertTest1 = bool("python")
boolConvertTest2 = bool("")
boolConvertTest3 = bool([])
boolConvertTest4 = bool(0)

print(boolConvertTest1)
print(boolConvertTest2)
print(boolConvertTest3)
print(boolConvertTest4)

print("=" * 50)