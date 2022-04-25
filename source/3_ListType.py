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

print("=" * 50)