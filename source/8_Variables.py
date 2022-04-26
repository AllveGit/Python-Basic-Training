"""
===== 변수 =====
"""

print("=" * 50)
print("Training_8. Variables")

# 변수 정의법
"""
# (변수 이름 = 변수에 저장할 값) 폼으로 정의한다.
# 변수를 정의하면 객체를 자동으로 메모리에 생성시키고 그 주소를 변수가 가리키게 된다.
"""

varAddrTest = [1, 2, 3]
# id는 객체의 메모리 주소값을 리턴해주는 파이썬 내장 함수이다.
print(id(varAddrTest))



# 리스트를 복사하는법
"""
기본적으로 python에서 리스트, 튜플, 딕셔너리, 변수 같은 객체들은 다 ReferenceType이다.
그렇기에 변수에 변수를 대입하여도 값이 복사가 되는것이 아닌 그 객체의 주소를 참조하도록 되는 것이다.
그 현상은 변수가 가리키고 있는 메모리 주소로 확인이 가능하다.
"""

varReferTest1 = [1,2,3]
varReferTest2 = varReferTest1

# 둘의 메모리 주소가 똑같다!!
print(id(varReferTest1))
print(id(varReferTest2))
# 동일한 객체인지 판단하는 명령어로도 똑같다고 리턴됨
print(varReferTest1 is varReferTest2)

# 일반 변수는 대입해서 변경해도 새로운 값이 대입되는 것으로 취급하여 괜찮지만..
# 리스트같이 주소접근을 하여 요소를 수정하는 경우 varReferTest2를 변경해도 varReferTest1이 변경되고 반대도 마찬가지다.
varReferTest2[2] = 1

print(varReferTest1)
print(varReferTest2)

# 1. [:] 를 이용하여 복사
listCopyTest1_1 = [1, 2, 3]
listCopyTest1_2 = listCopyTest1_1[:]
listCopyTest1_2[1] = 10

print(listCopyTest1_1)
print(listCopyTest1_2)

# 2. copy 모듈 이용하여 복사
from copy import copy
listCopyTest2_1 = [1, 2, 3]
listCopyTest2_2 = copy(listCopyTest2_1)
listCopyTest2_2[1] = 20

print(listCopyTest2_1)
print(listCopyTest2_2)



# 변수를 만드는 방법들

# 튜플의 요소들을 각각 변수로 만들수도 있다.
a1, b1 = ("python", "go")
print(a1)
print(b1)

# 리스트의 요소들을 각각 변수로 만들수도 있다.
[a2, b2] = ["python", "go"]
print(a2)
print(b2)

# 이를 이용해 swap도 간단히 구현가능하다.
swap1 = 1
swap2 = 2
swap1, swap2 = swap2, swap1
print(swap1)
print(swap2)

print("=" * 50)