"""
===== 집합 자료형 =====
"""

from turtle import update


print("=" * 50)
print("Training_6. SetType")

"""
집합 자료형의 특징
# 중복을 허용하지 않는다.
# 순서가 없다. (Unordered)

딕셔너리처럼 순서가 없기에 인덱싱 불가능
인덱싱으로 접근하려면 리스트나 튜플로 변환후 해야함.
"""

# 집합 자료형 정의법
setTest1 = set([1,2,3])
setTest2 = set("Hello")
print(setTest1)
print(setTest2)



# 교집합 구하기 (중복된 것만)
interSetTest1 = set([1, 2, 3, 4, 5, 6])
interSetTest2 = set([4, 5, 6, 7, 8, 9])
# 두 구문 다 같은 결과를 리턴
print(interSetTest1 & interSetTest2)
print(interSetTest1.intersection(interSetTest2))



# 합집합 구하기 (중복된 건 하나만)
unionSetTest1 = set([1, 2, 3, 4, 5, 6])
unionSetTest2 = set([4, 5, 6, 7, 8, 9])
# 두 구문 다 같은 결과를 리턴
print(unionSetTest1 | interSetTest2)
print(unionSetTest1.union(interSetTest2))



# 차집합 구하기 (중복되지 않은 것만)
diffSetTest1 = set([1, 2, 3, 4, 5, 6])
diffSetTest2 = set([4, 5, 6, 7, 8, 9])
# 두 구문 다 같은 결과를 리턴
print(diffSetTest1 - diffSetTest2)
print(diffSetTest1.difference(interSetTest2))
print(diffSetTest2 - diffSetTest1)
print(diffSetTest2.difference(diffSetTest1))



# 집합 자료형 관련 함수들 (add, update, remove)
# add는 set에 값을 한 개 추가하는 함수이다.
addSetTest = set([1, 2, 3])
addSetTest.add(4)
print(addSetTest)

# update는 set에 값을 여러 개 추가하는 함수이다.
updateSetTest = set([1, 2, 3])
updateSetTest.update([4, 5, 6])
print(updateSetTest)

# remove는 set에 특정 값을 삭제하는 함수이다. 특정 값을 찾지 못하면 에러가 발생한다.
removeSetTest = set([1, 2, 3])
removeSetTest.remove(2)
print(removeSetTest)

print("=" * 50)