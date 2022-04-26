"""
===== 리스트 자료형 =====
"""

print("=" * 50)
print("Training_3. ListType")

# 리스트 정의법
testList = [1, 2, 3, 4, 5]
# 특정한 자료형만이 아닌 다양한 자료형을 포함 가능
testList2 = [1, 2, "Three", "Four"]
# 리스트도 요소로 포함 가능
testList3 = [1, 2, ["Three", "Four"]]
# 비어있는 리스트도 생성가능
testList4 = []
testList5 = list()



# 리스트의 인덱싱과 슬라이싱
# 리스트를 print하면 리스트의 요소 전부 출력
listIndexTestList1 = [1, 2, 3]
print(listIndexTestList1)
# 배열처럼 인덱싱
print(listIndexTestList1[0])
# 인덱스번호에 -를 붙이면 역순으로 인덱싱
print(listIndexTestList1[-1])

# 리스트가 배열요소로 있으면 그 요소로 인덱싱했을 때 리스트로 취급
listIndexTestList2 = [1, 2, 3, ['a', 'b', 'c']]
print(listIndexTestList2[0])
print(listIndexTestList2[-1])
print(listIndexTestList2[3])
# 이렇게 되면 2차원배열처럼 인덱싱해서 값 추출 가능
print(listIndexTestList2[3][1])

# 리스트도 문자열과 똑같이 슬라이싱이 가능하다.
listSliceTestList1 = [1, 2, 3, 4, 5]
print(listSliceTestList1[0:2])
print(listSliceTestList1[:2])
print(listSliceTestList1[2:])

listSliceTestList2 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(listSliceTestList2[2:5])
print(listSliceTestList2[3][:2])



# 리스트에서 쓰일수있는 연산자도 있다 (+, *)
listOperatorTestList1 = [1, 2, 3]
listOperatorTestList2 = [4, 5, 6]
# 리스트는 더하기 연산자로 요소들을 합칠 수 있다.
print(listOperatorTestList1 + listOperatorTestList2)
# 리스트는 곱하기 연산자로 요소들을 반복하여 새로운 리스트를 만든다.
print(listOperatorTestList1 * 3)



# 리스트 길이 구하는 함수 (len)
lenTestList = [1, 4, 6]
print(len(lenTestList))



# 리스트의 수정과 삭제
listModTestList = [1, 2, 3]
# 배열처럼 첨자 연산자로 값을 수정할 수 있다.
listModTestList[2] = 4
print(listModTestList)

listDelTestList1 = [1, 2, 3]
# del로 리스트 요소 삭제 가능, del은 파이썬 내장 삭제 함수이며 객체들을 삭제할 수 있는 함수이다.
del listDelTestList1[1]
print(listDelTestList1)

listDelTestList2 = [1, 2, 3, 4, 5]
# 슬라이싱으로 여러가지 요소를 삭제할수도 있다.
del listDelTestList2[2:]
print(listDelTestList2)



# 리스트 관련 함수들 (append, sort, reverse, index, insert, remove, pop, count, extemd)

listAppendTestList = [1, 2, 3]
# append는 리스트의 맨마지막에 요소를 추가하는 함수이다. 어떤 자료형이든 가능
listAppendTestList.append(4)
print(listAppendTestList)
listAppendTestList.append(['a', 'b'])
print(listAppendTestList)


listSortTestList1 = [1, 4, 2, 5]
# sort는 요소들을 정해진 기준의 순서대로 정렬해주는 함수이다.
# 무조건 같은 자료형끼리 모인 리스트여야 한다.
listSortTestList1.sort()
print(listSortTestList1)

listSortTestList2 = ['z', 'd', 'a', 'e']
listSortTestList2.sort()
print(listSortTestList2)


listReverseTestList = [1, 2, 3]
# reverse는 리스트의 요소들의 순서를 모두 뒤집는 함수이다.
listReverseTestList.reverse()
print(listReverseTestList)


listIndexFuncTestList = [1, 2, 3]
# index는 검색한 리스트 요소의 위치를 찾아서 리턴해주는 함수이다. 검색한 요소가 없다면 에러를 리턴한다.
print(listIndexFuncTestList.index(2))
print(listIndexFuncTestList.index(1))


listInsertTestList = [1, 2, 3]
# insert는 리스트 요소사이에 새로운 요소를 삽입하는 함수이다.
# 어떤 위치에 어떤 요소를 넣을지 정해줘야 한다.
listInsertTestList.insert(0, 4)
print(listInsertTestList)

listInsertTestList.insert(2, 5)
print(listInsertTestList)


listRemoveTestList = [1, 2, 3, 1]
# remove는 리스트에서 첫번째로 발견되는 요소를 삭제하는 함수이다.
listRemoveTestList.remove(1)
print(listRemoveTestList)


listPopTestList = [1, 2, 3]
# pop은 리스트의 맨 마지막 요소를 리턴하고 그 요소를 리스트에서 삭제한다.
print(listPopTestList.pop())
print(listPopTestList)


listCountTestList = ['a', 'b', 'c', 'a', 'a', 'e', 'a']
# count는 리스트 안에 확인할 요소가 몇개 있는지 알려주는 함수이다.
print(listCountTestList.count('a'))


listExtendTestList = ['a', 'b', 'c']
# extend는 리스트끼리 더하는 연산과 똑같이 리스트끼리 합치는 함수이다.
# 리스트끼리 += 하는 것과 동일
listExtendTestList.extend(['d', 'e', 'f'])
print(listExtendTestList)

print("=" * 50)