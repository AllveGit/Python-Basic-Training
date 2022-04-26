"""
===== 튜플 자료형 =====
"""

print("=" * 50)
print("Training_4. TupleType")

# 튜플 정의법
"""
기본적으로 리스트와 비슷하지만 몇가지가 다름

# 리스트는 []으로 둘러싸지만, 튜플은 ()으로 둘러쌈. ()를 생략할수도 있다.
# 리스트는 요소의 수정, 삭제가 가능하지만, 튜플은 불가능하다.
# 튜플에서 요소의 수정 및 삭제를 하려할 때 에러가 발생한다.
""" 

tupleTest1 = ()
tupleTest2 = (1,)
tupleTest3 = (1, 2, 3)
tupleTest4 = 1, 2, 3
tupleTest5 = ('a', 'b', ('ab', 'cd'))
print(tupleTest5)



# 튜플 인덱싱
tupleIndexTest = (1, 2, 'a', 'b')
print(tupleIndexTest[0])



# 튜플 슬라이싱
tupleSliceTest = (1, 2, 3, 4, 5)
print(tupleSliceTest[1:4])
print(tupleSliceTest[2:])
print(tupleSliceTest[:3])



# 튜플 연산자
# 더하기 (+)
tuplePlusTest1 = (1, 2)
tuplePlusTest2 = (3, 'd')
print(tuplePlusTest1 + tuplePlusTest2)

# 곱하기 (*)
tupleMultiplyTest = (3, 'd')
print(tupleMultiplyTest * 5)



# 튜플 길이 구하는 함수 (len)
tupleLenTest = (1, 2, 'c', 'd', 5)
print(len(tupleLenTest))

print("=" * 50)